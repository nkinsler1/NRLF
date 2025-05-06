import sys

from awsglue.utils import getResolvedOptions
from pipeline import LogPipeline
from pyspark.context import SparkContext
from transformations import dtype_conversion, rename_cols, resolve_dupes

# Get arguments from AWS Glue job
args = getResolvedOptions(
    sys.argv, ["job_name", "source_path", "target_path", "partition_cols"]
)

# Start Glue context
sc = SparkContext()

partition_cols = args["partition_cols"].split(",") if "partition_cols" in args else []

host_prefixes = [
    "consumer--countDocumentReference",
    "consumer--searchPostDocumentReference",
    "consumer--searchDocumentReference",
    "consumer--readDocumentReference",
    "producer--searchPostDocumentReference",
    "producer--searchDocumentReference",
    "producer--readDocumentReference",
    "producer--upsertDocumentReference",
    "producer--updateDocumentReference",
    "producer--deleteDocumentReference",
    "producer--createDocumentReference",
]

# Initialize ETL process
etl_job = LogPipeline(
    spark_context=sc,
    source_path=args["source_path"],
    target_path=args["target_path"],
    host_prefixes=host_prefixes,
    job_name=args["job_name"],
    partition_cols=partition_cols,
    transformations=[rename_cols, resolve_dupes, dtype_conversion],
)

# Run the job
etl_job.run()
