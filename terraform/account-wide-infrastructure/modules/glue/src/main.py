import sys

from awsglue.utils import getResolvedOptions
from pipeline import LogPipeline
from pyspark.context import SparkContext
from schemas.consumer_schemas import consumerSchemaList
from schemas.producer_schemas import producerSchemaList
from transformations import dtype_conversion, flatten_df

# Get arguments from AWS Glue job
args = getResolvedOptions(
    sys.argv, ["job_name", "source_path", "target_path", "partition_cols"]
)

# Start Glue context
sc = SparkContext()

partition_cols = args["partition_cols"].split(",") if "partition_cols" in args else []

schema_list = consumerSchemaList.extend(producerSchemaList)

# Initialize ETL process
etl_job = LogPipeline(
    spark_context=sc,
    source_path=args["source_path"],
    target_path=args["target_path"],
    schemas=schema_list,
    job_name=args["job_name"],
    partition_cols=partition_cols,
    transformations=[flatten_df, dtype_conversion],
)

# Run the job
etl_job.run()
