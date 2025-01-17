from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import (
    BooleanType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

logSchema = StructType(
    [
        StructField("time", TimestampType(), True),
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
    cols = []
    for c in df.dtypes:
        if "struct" in c[1]:
            nested_col = c[0]
        else:
            cols.append(c[0])
    return df.select(*cols, f"{nested_col}.*")


def dtype_conversion(df):
    df = df.withColumn(
        "timestamp", to_timestamp(df["timestamp"], "yyyy-MM-dd HH:mm:ss,SSSXXX")
    )
    return df
