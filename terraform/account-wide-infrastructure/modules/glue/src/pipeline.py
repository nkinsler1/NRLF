import boto3
from instances import GlueContextSingleton, LoggerSingleton
from pyspark.sql.functions import col


class LogPipeline:
    def __init__(
        self,
        spark_context,
        source_path,
        target_path,
        schemas,
        job_name,
        partition_cols=[],
        transformations=[],
    ):
        """Initialize Glue context, Spark session, logger, and paths"""
        self.glue_context = GlueContextSingleton(spark_context).context
        self.spark = GlueContextSingleton(spark_context).spark
        self.logger = LoggerSingleton().logger
        self.source_path = source_path
        self.target_path = target_path
        self.schemas = schemas
        self.partition_cols = partition_cols
        self.transformations = transformations
        self.glue = boto3.client(
            service_name="glue",
            region_name="eu-west-2",
            endpoint_url="https://glue.eu-west-2.amazonaws.com",
        )
        self.name_prefix = "-".join(job_name.split("-")[:4])

    def run(self):
        """Runs ETL"""
        try:
            self.logger.info("ETL Process started.")
            data = self.extract()
            self.logger.info(f"Data extracted from {self.source_path}.")
            for name, df in data.items():
                data[name] = self.transform(df)
            self.logger.info("Data transformed successfully.")
            self.load(data)
            self.logger.info(f"Data loaded into {self.target_path}.")
            self.logger.info("Trigger glue crawler")
            self.trigger_crawler()
        except Exception as e:
            self.logger.error(f"ETL process failed: {e}")
            raise e

    def extract(self):
        """Extract JSON data from S3"""
        self.logger.info(f"Extracting data from {self.source_path} as JSON")
        data = {}
        for name, schema in self.schemas.items():
            data[name] = (
                self.spark.read.option("recursiveFileLookup", "true")
                .schema(schema)
                .json(self.source_path)
            ).where(col("host").contains(name))
        return data

    def transform(self, dataframe):
        """Apply a list of transformations on the dataframe"""
        for transformation in self.transformations:
            self.logger.info(f"Applying transformation: {transformation.__name__}")
            dataframe = transformation(dataframe)
        return dataframe

    def load(self, data):
        """Load transformed data into Parquet format"""
        self.logger.info(f"Loading data into {self.target_path} as Parquet")
        for name, dataframe in data.items():
            name = name.replace("--", "_")
            dataframe.write.mode("append").partitionBy(*self.partition_cols).parquet(
                f"{self.target_path}{name}"
            )

    def trigger_crawler(self):
        self.glue.start_crawler(Name=f"{self.name_prefix}-log-crawler")
