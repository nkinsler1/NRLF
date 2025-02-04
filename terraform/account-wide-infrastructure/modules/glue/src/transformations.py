from pyspark.sql.functions import (
    col,
    from_unixtime,
    regexp_replace,
    to_date,
    to_timestamp,
)
from pyspark.sql.types import (
    BooleanType,
    DoubleType,
    StringType,
    StructField,
    StructType,
)

logSchema = StructType(
    [
        StructField("time", DoubleType(), True),
        StructField("index", StringType(), True),
        StructField("host", StringType(), True),
        StructField("source", StringType(), True),
        StructField(
            "event",
            StructType(
                [
                    StructField("level", StringType(), True),
                    StructField("location", StringType(), True),
                    StructField("message", StringType(), True),
                    StructField("timestamp", StringType(), True),
                    StructField("service", StringType(), True),
                    StructField("cold_start", BooleanType(), True),
                    StructField("function_name", StringType(), True),
                    StructField("function_memory_size", StringType(), True),
                    StructField("function_arn", StringType(), True),
                    StructField("function_request_id", StringType(), True),
                    StructField("correlation_id", StringType(), True),
                    StructField("method", StringType(), True),
                    StructField("path", StringType(), True),
                    StructField(
                        "headers",
                        StructType(
                            [
                                StructField("accept", StringType(), True),
                                StructField("accept-encoding", StringType(), True),
                                StructField("Authorization", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-Id", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Request-Id", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("log_reference", StringType(), True),
                    StructField("xray_trace_id", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)


def flatten_df(df):
    def flatten(schema, prefix=""):
        """
        Recursively traverse the schema to extract all nested fields.
        """
        fields = []
        for field in schema.fields:
            name = f"{prefix}.{field.name}" if prefix else field.name
            if isinstance(field.dataType, StructType):
                fields += flatten(field.dataType, name)
            else:
                alias_name = name.replace(".", "_")
                fields.append((name, alias_name))
        return fields

    flat_columns = flatten(df.schema)

    return df.select([col(c).alias(n) for c, n in flat_columns])


def dtype_conversion(df):
    df = (
        df.withColumn(
            "event_timestamp_cleaned", regexp_replace(col("event_timestamp"), ",", ".")
        )
        .withColumn(
            "event_timestamp",
            to_timestamp(col("event_timestamp_cleaned"), "yyyy-MM-dd HH:mm:ss.SSSZ"),
        )
        .withColumn("time", from_unixtime(col("time")).cast("timestamp"))
        .withColumn("date", to_date(col("time")))
    )
    return df.drop("event_timestamp_cleaned")
