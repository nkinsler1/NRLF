from pyspark.sql.types import (
    ArrayType,
    BooleanType,
    DoubleType,
    LongType,
    StringType,
    StructField,
    StructType,
)

upsertDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                                StructField("content-type", StringType(), True),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
                                StructField(
                                    "Nhsd-End-User-Organisation-Ods", StringType(), True
                                ),
                                StructField("X-Correlation-Id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                                StructField(
                                    "nrl_permissions",
                                    ArrayType(StringType(), True),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("id", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField(
                                                "coding",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "coding",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "system",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "code",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "display",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "author",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "identifier",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "value",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "content",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "attachment",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "contentType",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "url",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "creation",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "format",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "extension",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "valueCodeableConcept",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "coding",
                                                                                ArrayType(
                                                                                    StructType(
                                                                                        [
                                                                                            StructField(
                                                                                                "system",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "code",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "display",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "id",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                    True,
                                                                                ),
                                                                                True,
                                                                            )
                                                                        ]
                                                                    ),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "url",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "coding",
                                                            ArrayType(
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "code",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "display",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            ),
                                                            True,
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "period",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "start", StringType(), True
                                                        ),
                                                        StructField(
                                                            "end", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "related",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "identifier",
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "value",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            )
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "masterIdentifier",
                                    StructType(
                                        [
                                            StructField("system", StringType(), True),
                                            StructField("value", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("resource", StringType(), True),
                    StructField("resource_type", StringType(), True),
                    StructField("step", StringType(), True),
                    StructField("required_fields", ArrayType(StringType(), True), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("pointer_id", StringType(), True),
                    StructField(
                        "indexes",
                        StructType(
                            [
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
                                StructField("masterid_key", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("source", StringType(), True),
                    StructField("version", LongType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
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
                                                        )
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "masterid_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "CapacityUnits",
                                                                        DoubleType(),
                                                                        True,
                                                                    )
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
                                StructField(
                                    "headers",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("error", StringType(), True),
                    StructField("exception", StringType(), True),
                    StructField("exception_name", StringType(), True),
                    StructField(
                        "stack_trace",
                        StructType(
                            [
                                StructField("type", StringType(), True),
                                StructField("value", StringType(), True),
                                StructField("module", StringType(), True),
                                StructField(
                                    "frames",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField("file", StringType(), True),
                                                StructField("line", LongType(), True),
                                                StructField(
                                                    "function", StringType(), True
                                                ),
                                                StructField(
                                                    "statement", StringType(), True
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("bucket", StringType(), True),
                    StructField("key", StringType(), True),
                    StructField("ods_code", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("date", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)

updateDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                    StructField(
                        "path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
                    StructField(
                        "headers",
                        StructType(
                            [
                                StructField("accept", StringType(), True),
                                StructField("accept-encoding", StringType(), True),
                                StructField("Authorization", StringType(), True),
                                StructField("content-type", StringType(), True),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("id", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField(
                                                "coding",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "coding",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "system",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "code",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "display",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "author",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "identifier",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "value",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "content",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "attachment",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "contentType",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "url",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "creation",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "format",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "extension",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "valueCodeableConcept",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "coding",
                                                                                ArrayType(
                                                                                    StructType(
                                                                                        [
                                                                                            StructField(
                                                                                                "system",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "code",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "display",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                    True,
                                                                                ),
                                                                                True,
                                                                            )
                                                                        ]
                                                                    ),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "url",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "coding",
                                                            ArrayType(
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "code",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "display",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            ),
                                                            True,
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "period",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "start", StringType(), True
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "related",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "identifier",
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "value",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            )
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "parsed_path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("resource_type", StringType(), True),
                    StructField("step", StringType(), True),
                    StructField("required_fields", ArrayType(StringType(), True), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("id", StringType(), True),
                                StructField("nhs_number", StringType(), True),
                                StructField("custodian", StringType(), True),
                                StructField("producer_id", StringType(), True),
                                StructField("category_id", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("type_id", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("author", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("version", LongType(), True),
                                StructField("document", StringType(), True),
                                StructField("created_on", StringType(), True),
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
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
                                                        )
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        )
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
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("updated_on", StringType(), True),
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
                            ]
                        ),
                        True,
                    ),
                    StructField("field", StringType(), True),
                    StructField("provided", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)

searchPostDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                                StructField("content-type", StringType(), True),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("subject_identifier", StringType(), True),
                                StructField("type", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField("nhs_number", StringType(), True),
                    StructField("expression", StringType(), True),
                    StructField("values", ArrayType(StringType(), True), True),
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
                                            StructField(
                                                ":custodian", StringType(), True
                                            ),
                                            StructField(":type_0", StringType(), True),
                                            StructField(":type_1", StringType(), True),
                                            StructField(":type_2", StringType(), True),
                                            StructField(":type_3", StringType(), True),
                                            StructField(":type_4", StringType(), True),
                                            StructField(":type_5", StringType(), True),
                                            StructField(":type_6", StringType(), True),
                                            StructField(":type_7", StringType(), True),
                                            StructField(":type_8", StringType(), True),
                                            StructField(":type_9", StringType(), True),
                                            StructField(":type_10", StringType(), True),
                                            StructField(":type_11", StringType(), True),
                                            StructField(":type_12", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "ReturnConsumedCapacity", StringType(), True
                                ),
                                StructField("FilterExpression", StringType(), True),
                                StructField(
                                    "ExpressionAttributeNames",
                                    StructType(
                                        [
                                            StructField(
                                                "#pointer_type", StringType(), True
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("table", StringType(), True),
                    StructField(
                        "stats",
                        StructType(
                            [
                                StructField("count", LongType(), True),
                                StructField("scanned_count", LongType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField(
                                    "Items",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "nhs_number", StringType(), True
                                                ),
                                                StructField(
                                                    "version", StringType(), True
                                                ),
                                                StructField(
                                                    "category_id", StringType(), True
                                                ),
                                                StructField(
                                                    "producer_id", StringType(), True
                                                ),
                                                StructField(
                                                    "source", StringType(), True
                                                ),
                                                StructField(
                                                    "patient_key", StringType(), True
                                                ),
                                                StructField(
                                                    "type_id", StringType(), True
                                                ),
                                                StructField(
                                                    "schemas",
                                                    ArrayType(StringType(), True),
                                                    True,
                                                ),
                                                StructField(
                                                    "category", StringType(), True
                                                ),
                                                StructField("sk", StringType(), True),
                                                StructField(
                                                    "patient_sort", StringType(), True
                                                ),
                                                StructField("id", StringType(), True),
                                                StructField("pk", StringType(), True),
                                                StructField(
                                                    "document", StringType(), True
                                                ),
                                                StructField(
                                                    "custodian", StringType(), True
                                                ),
                                                StructField(
                                                    "author", StringType(), True
                                                ),
                                                StructField("type", StringType(), True),
                                                StructField(
                                                    "created_on", StringType(), True
                                                ),
                                                StructField(
                                                    "updated_on", StringType(), True
                                                ),
                                                StructField(
                                                    "master_identifier",
                                                    StringType(),
                                                    True,
                                                ),
                                                StructField(
                                                    "masterid_key", StringType(), True
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
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
                                            StructField("Table", StructType([]), True),
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        )
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
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("count", LongType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
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

searchDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField(
                        "params",
                        StructType(
                            [
                                StructField("subject:identifier", StringType(), True),
                                StructField("type", StringType(), True),
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
                                StructField("type", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField("nhs_number", StringType(), True),
                    StructField("expression", StringType(), True),
                    StructField("values", ArrayType(StringType(), True), True),
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
                                            StructField(
                                                ":custodian", StringType(), True
                                            ),
                                            StructField(":type_0", StringType(), True),
                                            StructField(":type_1", StringType(), True),
                                            StructField(":type_2", StringType(), True),
                                            StructField(":type_3", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "ReturnConsumedCapacity", StringType(), True
                                ),
                                StructField("FilterExpression", StringType(), True),
                                StructField(
                                    "ExpressionAttributeNames",
                                    StructType(
                                        [
                                            StructField(
                                                "#pointer_type", StringType(), True
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("table", StringType(), True),
                    StructField(
                        "stats",
                        StructType(
                            [
                                StructField("count", LongType(), True),
                                StructField("scanned_count", LongType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField(
                                    "Items",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "nhs_number", StringType(), True
                                                ),
                                                StructField(
                                                    "version", StringType(), True
                                                ),
                                                StructField(
                                                    "category_id", StringType(), True
                                                ),
                                                StructField(
                                                    "producer_id", StringType(), True
                                                ),
                                                StructField(
                                                    "source", StringType(), True
                                                ),
                                                StructField(
                                                    "patient_key", StringType(), True
                                                ),
                                                StructField(
                                                    "type_id", StringType(), True
                                                ),
                                                StructField(
                                                    "schemas",
                                                    ArrayType(StringType(), True),
                                                    True,
                                                ),
                                                StructField(
                                                    "category", StringType(), True
                                                ),
                                                StructField("sk", StringType(), True),
                                                StructField(
                                                    "patient_sort", StringType(), True
                                                ),
                                                StructField("id", StringType(), True),
                                                StructField("pk", StringType(), True),
                                                StructField(
                                                    "document", StringType(), True
                                                ),
                                                StructField(
                                                    "custodian", StringType(), True
                                                ),
                                                StructField(
                                                    "author", StringType(), True
                                                ),
                                                StructField("type", StringType(), True),
                                                StructField(
                                                    "created_on", StringType(), True
                                                ),
                                                StructField(
                                                    "master_identifier",
                                                    StringType(),
                                                    True,
                                                ),
                                                StructField(
                                                    "masterid_key", StringType(), True
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
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
                                            StructField("Table", StructType([]), True),
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        )
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
                                        ]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("count", LongType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("type", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)

readDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                    StructField(
                        "path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("id", StringType(), True),
                                StructField("nhs_number", StringType(), True),
                                StructField("custodian", StringType(), True),
                                StructField("producer_id", StringType(), True),
                                StructField("category_id", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("type_id", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("author", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("version", LongType(), True),
                                StructField("document", StringType(), True),
                                StructField("created_on", StringType(), True),
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
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

deleteDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                    StructField(
                        "path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_path",
                        StructType([StructField("id", StringType(), True)]),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("id", StringType(), True),
                                StructField("nhs_number", StringType(), True),
                                StructField("custodian", StringType(), True),
                                StructField("producer_id", StringType(), True),
                                StructField("category_id", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("type_id", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("author", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("version", LongType(), True),
                                StructField("document", StringType(), True),
                                StructField("created_on", StringType(), True),
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
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
                                                        )
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        )
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
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("updated_on", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("partition_key", StringType(), True),
                    StructField("sort_key", StringType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("pointer_id", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)

createDocumentReferenceSchema = StructType(
    [
        StructField("raw_message", StringType(), True),
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
                                StructField("content-type", StringType(), True),
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
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-request-id", StringType(), True),
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
                                StructField("nrl_app_id", StringType(), True),
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
                    StructField("pointer_types", ArrayType(StringType(), True), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField(
                                                "coding",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "coding",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "system",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "code",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "display",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "author",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "identifier",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "value",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                )
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            )
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "content",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "attachment",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "contentType",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "url",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "creation",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "size", LongType(), True
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "format",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "system",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "code",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "display",
                                                                StringType(),
                                                                True,
                                                            ),
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "extension",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "valueCodeableConcept",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "coding",
                                                                                ArrayType(
                                                                                    StructType(
                                                                                        [
                                                                                            StructField(
                                                                                                "system",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "code",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                            StructField(
                                                                                                "display",
                                                                                                StringType(),
                                                                                                True,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                    True,
                                                                                ),
                                                                                True,
                                                                            )
                                                                        ]
                                                                    ),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "url",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        ),
                                                        True,
                                                    ),
                                                    True,
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "coding",
                                                            ArrayType(
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "code",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "display",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            ),
                                                            True,
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "period",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "start", StringType(), True
                                                        ),
                                                        StructField(
                                                            "end", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "related",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "identifier",
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "system",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                        StructField(
                                                                            "value",
                                                                            StringType(),
                                                                            True,
                                                                        ),
                                                                    ]
                                                                ),
                                                                True,
                                                            )
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "event",
                                                ArrayType(
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "coding",
                                                                ArrayType(
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "system",
                                                                                StringType(),
                                                                                True,
                                                                            ),
                                                                            StructField(
                                                                                "code",
                                                                                StringType(),
                                                                                True,
                                                                            ),
                                                                            StructField(
                                                                                "display",
                                                                                StringType(),
                                                                                True,
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    True,
                                                                ),
                                                                True,
                                                            )
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                True,
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("id", StringType(), True),
                                StructField(
                                    "meta",
                                    StructType(
                                        [StructField("lastUpdated", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "masterIdentifier",
                                    StructType(
                                        [
                                            StructField("system", StringType(), True),
                                            StructField("value", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "identifier",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "type",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "text",
                                                                StringType(),
                                                                True,
                                                            )
                                                        ]
                                                    ),
                                                    True,
                                                ),
                                                StructField(
                                                    "value", StringType(), True
                                                ),
                                            ]
                                        ),
                                        True,
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                                StructField(
                                    "relatesTo",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField("code", StringType(), True),
                                                StructField(
                                                    "target",
                                                    StructType(
                                                        [
                                                            StructField(
                                                                "type",
                                                                StringType(),
                                                                True,
                                                            ),
                                                            StructField(
                                                                "identifier",
                                                                StructType(
                                                                    [
                                                                        StructField(
                                                                            "value",
                                                                            StringType(),
                                                                            True,
                                                                        )
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
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("resource", StringType(), True),
                    StructField("resource_type", StringType(), True),
                    StructField("step", StringType(), True),
                    StructField("required_fields", ArrayType(StringType(), True), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("producer_id", StringType(), True),
                    StructField("document_id", StringType(), True),
                    StructField("custodian", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("pointer_id", StringType(), True),
                    StructField(
                        "indexes",
                        StructType(
                            [
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
                                StructField("masterid_key", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("source", StringType(), True),
                    StructField("version", LongType(), True),
                    StructField(
                        "result",
                        StructType(
                            [
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
                                                        )
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
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "masterid_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "CapacityUnits",
                                                                        DoubleType(),
                                                                        True,
                                                                    )
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
                                StructField(
                                    "headers",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                            ]
                        ),
                        True,
                    ),
                    StructField("error", StringType(), True),
                    StructField("ods_code", StringType(), True),
                    StructField("relatesTo", ArrayType(StringType(), True), True),
                    StructField("related_identifier", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)

producerSchemaList = {
    "producer--searchPostDocumentReference": searchPostDocumentReferenceSchema,
    "producer--searchDocumentReference": searchDocumentReferenceSchema,
    "producer--readDocumentReference": readDocumentReferenceSchema,
    "producer--upsertDocumentReference": upsertDocumentReferenceSchema,
    "producer--updateDocumentReference": updateDocumentReferenceSchema,
    "producer--deleteDocumentReference": deleteDocumentReferenceSchema,
    "producer--createDocumentReference": createDocumentReferenceSchema,
}
