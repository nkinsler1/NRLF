import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

# Get arguments from AWS Glue job
args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "SOURCE_PATH", "TARGET_PATH", "PARTITION_COLS"]
)

# Start Glue context
sc = SparkContext()

partition_cols = args["PARTITION_COLS"].split(",") if "PARTITION_COLS" in args else []

# Initialize ETL process
etl_job = ETLTemplate(
    spark_context=sc,
    source_path=args["SOURCE_PATH"],
    target_path=args["TARGET_PATH"],
    partition_cols=partition_cols,
    transformations=[placeholder],
)

# Run the job
etl_job.run()
