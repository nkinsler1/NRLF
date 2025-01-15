from instances import GlueContextSingleton, LoggerSingleton


class LogPipeline:
    def __init__(
        self,
        spark_context,
        source_path,
        target_path,
        schema,
        partition_cols=[],
        transformations=[],
    ):
        """Initialize Glue context, Spark session, logger, and paths"""
        self.glue_context = GlueContextSingleton(spark_context).context
        self.spark = GlueContextSingleton(spark_context).spark
        self.logger = LoggerSingleton().logger
        self.source_path = source_path
        self.target_path = target_path
        self.schema = schema
        self.partition_cols = partition_cols
        self.transformations = transformations

    def run(self):
        """Runs ETL"""
        try:
            self.logger.info("ETL Process started.")
            df = self.extract()
            self.logger.info(f"Data extracted from {self.source_path}.")
            df = self.transform(df)
            self.logger.info("Data transformed successfully.")
            self.load(df)
            self.logger.info(f"Data loaded into {self.target_path}.")
        except Exception as e:
            self.logger.error(f"ETL process failed: {e}")
            raise e

    def extract(self):
        """Extract JSON data from S3"""
        self.logger.info(f"Extracting data from {self.source_path} as JSON")
        return (
            self.spark.read.option("recursiveFileLookup", "true")
            .schema(self.schema)
            .json(self.source_path)
        )

    def transform(self, dataframe):
        """Apply a list of transformations on the dataframe"""
        for transformation in self.transformations:
            self.logger.info(f"Applying transformation: {transformation.__name__}")
            dataframe = transformation(dataframe)
        return dataframe

    def load(self, dataframe):
        """Load transformed data into Parquet format"""
        self.logger.info(f"Loading data into {self.target_path} as Parquet")
        dataframe.write.mode("append").partitionBy(*self.partition_cols).parquet(
            self.target_path
        )
