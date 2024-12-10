from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# from awsglue.job import Job
from pyspark.context import SparkContext

# from pyspark.sql import DataFrame


def create_glue_context():
    # Initialize the SparkContext and GlueContext
    sc = SparkContext()
    glueContext = GlueContext(sc)

    return glueContext


def load_data_from_s3(
    glueContext, s3_path: str, file_type: str = "json", format_options: dict = {}
):
    """
    Loads data from S3 into a Glue DynamicFrame.
    """
    if file_type == "json":
        return glueContext.create_dynamic_frame.from_options(
            connection_type="s3",
            connection_options={"paths": [s3_path]},
            format=file_type,
        )
    else:
        raise ValueError(f"Unsupported file_type: {file_type}")


def transform_data(dynamic_frame: DynamicFrame) -> DynamicFrame:
    """
    Example transformation function. Modify this to suit your transformation logic.
    """
    # Convert DynamicFrame to DataFrame to leverage Spark SQL operations if needed
    df = dynamic_frame.toDF()

    # Perform any necessary transformations using Spark DataFrame API
    df_transformed = df.filter(df["x"] == "placeholder")

    # Convert DataFrame back to DynamicFrame for Glue compatibility
    transformed_dynamic_frame = DynamicFrame.fromDF(
        df_transformed, dynamic_frame.glue_ctx, "transformed_dynamic_frame"
    )

    return transformed_dynamic_frame


def write_data_to_s3(
    dynamic_frame: DynamicFrame,
    s3_path: str,
    file_type: str = "csv",
    partition_keys: list = None,
):
    """
    Writes a DynamicFrame to S3 with partitioning support for scalability.
    """
    if file_type == "csv":
        dynamic_frame.toDF().write.option("header", "true").mode(
            "overwrite"
        ).partitionBy(*partition_keys).csv(s3_path)
    elif file_type == "parquet":
        dynamic_frame.toDF().write.mode("overwrite").partitionBy(
            *partition_keys
        ).parquet(s3_path)
    elif file_type == "json":
        dynamic_frame.toDF().write.mode("overwrite").partitionBy(*partition_keys).json(
            s3_path
        )
    else:
        raise ValueError(f"Unsupported file_type: {file_type}")


def handle_error(exception: Exception):
    # Custom error handling for logging
    raise exception


def main():
    try:
        # Initialize Glue Context
        glueContext = create_glue_context()

        # Example paths and configurations
        input_path = "s3://source-data-bucket/input-data/"  # probs worth using one bucket and different folders? Cuts costs
        output_path = "s3://target-data-bucket/output-data/"

        # Load data from S3 (adjust format if needed)
        dynamic_frame = load_data_from_s3(glueContext, input_path, format="json")

        # Transform data
        transformed_dynamic_frame = transform_data(dynamic_frame)

        # Write the transformed data back to S3, partitioned by 'date'
        write_data_to_s3(
            transformed_dynamic_frame,
            output_path,
            format="csv",
            partition_keys=["date"],
        )

    except Exception as e:
        handle_error(e)


# Entry point for Glue job
if __name__ == "__main__":
    main()
