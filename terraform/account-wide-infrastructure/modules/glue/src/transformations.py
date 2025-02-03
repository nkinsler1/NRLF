from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import (
    BooleanType,
    DoubleType,
    LongType,
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
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-Id", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Request-Id", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("log_reference", StringType(), True),
                    StructField("xray_trace_id", StringType(), True),
                    StructField(
                        "config",
                        StructType(
                            [
                                StructField("AWS_REGION", StringType(), True),
                                StructField("PREFIX", StringType(), True),
                                StructField("ENVIRONMENT", StringType(), True),
                                StructField("SPLUNK_INDEX", StringType(), True),
                                StructField("SOURCE", StringType(), True),
                                StructField("AUTH_STORE", StringType(), True),
                                StructField("TABLE_NAME", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "metadata",
                        StructType(
                            [
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_app_id", StringType(), True),
                                StructField("is_test_event", BooleanType(), True),
                                StructField(
                                    "client_rp_details",
                                    StructType(
                                        [
                                            StructField(
                                                "developer_app_name", StringType(), True
                                            ),
                                            StructField(
                                                "developer_app_id", StringType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "params",
                        StructType(
                            [
                                StructField("subject:identifier", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_params",
                        StructType(
                            [
                                StructField("subject_identifier", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("nhs_number", StringType(), True),
                    StructField(
                        "query",
                        StructType(
                            [
                                StructField("IndexName", StringType(), True),
                                StructField(
                                    "KeyConditionExpression", StringType(), True
                                ),
                                StructField(
                                    "ExpressionAttributeValues",
                                    StructType(
                                        [
                                            StructField(
                                                ":patient_key", StringType(), True
                                            ),
                                            StructField(
                                                ":patient_sort", StringType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("Select", StringType(), True),
                                StructField(
                                    "ReturnConsumedCapacity", StringType(), True
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("count", LongType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("Count", LongType(), True),
                                StructField("ScannedCount", LongType(), True),
                                StructField(
                                    "ConsumedCapacity",
                                    StructType(
                                        [
                                            StructField(
                                                "TableName", StringType(), True
                                            ),
                                            StructField(
                                                "CapacityUnits", DoubleType(), True
                                            ),
                                            StructField(
                                                "Table",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "CapacityUnits",
                                                            DoubleType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "GlobalSecondaryIndexes",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "patient_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "CapacityUnits",
                                                                        DoubleType(),
                                                                        True,
                                                                    ),
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "ResponseMetadata",
                                    StructType(
                                        [
                                            StructField(
                                                "RequestId", StringType(), True
                                            ),
                                            StructField(
                                                "HTTPStatusCode", LongType(), True
                                            ),
                                            StructField(
                                                "HTTPHeaders",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "server", StringType(), True
                                                        ),
                                                        StructField(
                                                            "date", StringType(), True
                                                        ),
                                                        StructField(
                                                            "content-type",
                                                            StringType(),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "content-length",
                                                            StringType(),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "connection",
                                                            StringType(),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "x-amzn-requestid",
                                                            StringType(),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "x-amz-crc32",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "RetryAttempts", LongType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                                StructField("isBase64Encoded", BooleanType(), True),
                            ]
                        ),
                        True,
                    ),
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
