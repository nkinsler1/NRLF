import sys

from awsglue.utils import getResolvedOptions
from pipeline import LogPipeline
from pyspark.context import SparkContext
from transformations import dtype_conversion, flatten_df, logSchema

# Get arguments from AWS Glue job
args = getResolvedOptions(sys.argv, ["job_name", "source_path", "target_path"])

# Start Glue context
sc = SparkContext()

partition_cols = args["partition_cols"].split(",") if "partition_cols" in args else []

# Initialize ETL process
etl_job = LogPipeline(
    spark_context=sc,
    source_path=args["source_path"],
    target_path=args["target_path"],
    schema=logSchema,
    partition_cols=partition_cols,
    transformations=[flatten_df, dtype_conversion],
)

# Run the job
etl_job.run()
