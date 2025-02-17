from pyspark.sql.types import (
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
                                StructField("cache-control", StringType(), True),
                                StructField("content-type", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("id", StringType(), True),
                                StructField("meta", StringType(), True),
                                StructField("implicitRules", StringType(), True),
                                StructField("language", StringType(), True),
                                StructField("text", StringType(), True),
                                StructField(
                                    "masterIdentifier",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField("use", StringType(), True),
                                            StructField("type", StringType(), True),
                                            StructField("system", StringType(), True),
                                            StructField("value", StringType(), True),
                                            StructField("period", StringType(), True),
                                            StructField("assigner", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("identifier", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField("docStatus", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "coding",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "Location",
                                                            StringType(),
                                                            True,
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("text", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                                StructField(
                                    "author",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField("authenticator", StringType(), True),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("relatesTo", StringType(), True),
                                StructField("description", StringType(), True),
                                StructField("securityLabel", StringType(), True),
                                StructField(
                                    "content",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "encounter", StringType(), True
                                            ),
                                            StructField("event", StringType(), True),
                                            StructField(
                                                "period",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
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
                                                "facilityType", StringType(), True
                                            ),
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "coding",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "Location",
                                                                        StringType(),
                                                                        True,
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "text", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "sourcePatientInfo", StringType(), True
                                            ),
                                            StructField(
                                                "related",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "Location",
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
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("resource", StringType(), True),
                    StructField("resource_type", StringType(), True),
                    StructField("step", StringType(), True),
                    StructField("required_fields", StringType(), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("issue_count", LongType(), True),
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
                    StructField("error", StringType(), True),
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
                                StructField("isBase64Encoded", BooleanType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("status_code", StringType(), True),
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
                                    StructType(
                                        [StructField("Location", StringType(), True)]
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
                                StructField("cache-control", StringType(), True),
                                StructField("content-type", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("id", StringType(), True),
                                StructField("meta", StringType(), True),
                                StructField("implicitRules", StringType(), True),
                                StructField("language", StringType(), True),
                                StructField("text", StringType(), True),
                                StructField("masterIdentifier", StringType(), True),
                                StructField("identifier", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField("docStatus", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "coding",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("text", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                                StructField(
                                    "author",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
                                StructField("authenticator", StringType(), True),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("relatesTo", StringType(), True),
                                StructField("description", StringType(), True),
                                StructField("securityLabel", StringType(), True),
                                StructField(
                                    "content",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "encounter", StringType(), True
                                            ),
                                            StructField("event", StringType(), True),
                                            StructField(
                                                "period",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
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
                                                "facilityType", StringType(), True
                                            ),
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "coding",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "id",
                                                                        StringType(),
                                                                        True,
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "text", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "sourcePatientInfo", StringType(), True
                                            ),
                                            StructField(
                                                "related",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
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
                    StructField("required_fields", StringType(), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("issue_count", LongType(), True),
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
                                StructField("custodian_suffix", StringType(), True),
                                StructField("producer_id", StringType(), True),
                                StructField("category_id", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("type_id", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("master_identifier", StringType(), True),
                                StructField("author", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("version", LongType(), True),
                                StructField("document", StringType(), True),
                                StructField("created_on", StringType(), True),
                                StructField("updated_on", StringType(), True),
                                StructField("schemas", StringType(), True),
                                StructField("pk", StringType(), True),
                                StructField("sk", StringType(), True),
                                StructField("patient_key", StringType(), True),
                                StructField("patient_sort", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("field", StringType(), True),
                    StructField("provided", StringType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                                StructField(
                                    "headers",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
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
                                StructField("cache-control", StringType(), True),
                                StructField("content-type", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("subject_identifier", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("next_page_token", StringType(), True),
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
                    StructField("categories", StringType(), True),
                    StructField("expression", StringType(), True),
                    StructField("values", StringType(), True),
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
                                            StructField(
                                                ":custodian", StringType(), True
                                            ),
                                            StructField(
                                                ":patient_sort", StringType(), True
                                            ),
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
                                StructField("last_evaluated_key", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("Items", StructType([]), True),
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
                                StructField("headers", StructType([]), True),
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
                                StructField("cache-control", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
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
                                StructField("category", StringType(), True),
                                StructField("next_page_token", StringType(), True),
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
                    StructField("categories", StringType(), True),
                    StructField("expression", StringType(), True),
                    StructField("values", StringType(), True),
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
                                            StructField(":type_0", StringType(), True),
                                            StructField(":type_1", StringType(), True),
                                            StructField(":type_2", StringType(), True),
                                            StructField(":type_3", StringType(), True),
                                            StructField(
                                                ":custodian", StringType(), True
                                            ),
                                            StructField(
                                                ":patient_sort", StringType(), True
                                            ),
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
                                StructField("last_evaluated_key", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "result",
                        StructType(
                            [
                                StructField("Items", StructType([]), True),
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
                                StructField("headers", StructType([]), True),
                                StructField("isBase64Encoded", BooleanType(), True),
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
                                StructField("cache-control", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
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
                                StructField(
                                    "headers",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
                                StructField("isBase64Encoded", BooleanType(), True),
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
                                StructField("custodian_suffix", StringType(), True),
                                StructField("producer_id", StringType(), True),
                                StructField("category_id", StringType(), True),
                                StructField("category", StringType(), True),
                                StructField("type_id", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("master_identifier", StringType(), True),
                                StructField("author", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("version", LongType(), True),
                                StructField("document", StringType(), True),
                                StructField("created_on", StringType(), True),
                                StructField("updated_on", StringType(), True),
                                StructField("schemas", StringType(), True),
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
                                StructField("cache-control", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
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
                    StructField("pointer_id", StringType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statusCode", StringType(), True),
                                StructField("body", StringType(), True),
                                StructField(
                                    "headers",
                                    StructType([StructField("id", StringType(), True)]),
                                    True,
                                ),
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
                                StructField("cache-control", StringType(), True),
                                StructField("content-type", StringType(), True),
                                StructField("Host", StringType(), True),
                                StructField(
                                    "NHSD-Client-RP-Details", StringType(), True
                                ),
                                StructField(
                                    "NHSD-Connection-Metadata", StringType(), True
                                ),
                                StructField("NHSD-Correlation-ID", StringType(), True),
                                StructField(
                                    "NHSD-End-User-Organisation-ODS", StringType(), True
                                ),
                                StructField("NHSD-Request-ID", StringType(), True),
                                StructField("Postman-Token", StringType(), True),
                                StructField("User-Agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("X-Forwarded-For", StringType(), True),
                                StructField("X-Forwarded-Port", StringType(), True),
                                StructField("X-Forwarded-Proto", StringType(), True),
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
                                StructField("pointer_types", StringType(), True),
                                StructField("ods_code", StringType(), True),
                                StructField("ods_code_extension", StringType(), True),
                                StructField("nrl_permissions", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField("error", StringType(), True),
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
                                StructField("isBase64Encoded", BooleanType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("resourceType", StringType(), True),
                                StructField("id", StringType(), True),
                                StructField(
                                    "meta",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "versionId", StringType(), True
                                            ),
                                            StructField(
                                                "lastUpdated", StringType(), True
                                            ),
                                            StructField("source", StringType(), True),
                                            StructField("profile", StringType(), True),
                                            StructField("security", StringType(), True),
                                            StructField("tag", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("implicitRules", StringType(), True),
                                StructField("language", StringType(), True),
                                StructField("text", StringType(), True),
                                StructField(
                                    "masterIdentifier",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField("use", StringType(), True),
                                            StructField("type", StringType(), True),
                                            StructField("system", StringType(), True),
                                            StructField("value", StringType(), True),
                                            StructField("period", StringType(), True),
                                            StructField("assigner", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("identifier", StringType(), True),
                                StructField("status", StringType(), True),
                                StructField("docStatus", StringType(), True),
                                StructField(
                                    "type",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "coding",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "Location",
                                                            StringType(),
                                                            True,
                                                        )
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("text", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "category",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "subject",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("date", StringType(), True),
                                StructField(
                                    "author",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField("authenticator", StringType(), True),
                                StructField(
                                    "custodian",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "reference", StringType(), True
                                            ),
                                            StructField("type", StringType(), True),
                                            StructField(
                                                "identifier",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "use", StringType(), True
                                                        ),
                                                        StructField(
                                                            "type", StringType(), True
                                                        ),
                                                        StructField(
                                                            "system", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "period", StringType(), True
                                                        ),
                                                        StructField(
                                                            "assigner",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField("display", StringType(), True),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("relatesTo", StringType(), True),
                                StructField("description", StringType(), True),
                                StructField("securityLabel", StringType(), True),
                                StructField(
                                    "content",
                                    StructType(
                                        [StructField("Location", StringType(), True)]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "context",
                                    StructType(
                                        [
                                            StructField("id", StringType(), True),
                                            StructField(
                                                "encounter", StringType(), True
                                            ),
                                            StructField(
                                                "event",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "Location",
                                                            StringType(),
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
                                                            "id", StringType(), True
                                                        ),
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
                                                "facilityType", StringType(), True
                                            ),
                                            StructField(
                                                "practiceSetting",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "id", StringType(), True
                                                        ),
                                                        StructField(
                                                            "coding",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "Location",
                                                                        StringType(),
                                                                        True,
                                                                    )
                                                                ]
                                                            ),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "text", StringType(), True
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "sourcePatientInfo", StringType(), True
                                            ),
                                            StructField(
                                                "related",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "Location",
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
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("resource", StringType(), True),
                    StructField("resource_type", StringType(), True),
                    StructField("step", StringType(), True),
                    StructField("required_fields", StringType(), True),
                    StructField("reason", StringType(), True),
                    StructField("is_valid", BooleanType(), True),
                    StructField("issue_count", LongType(), True),
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
                    StructField("ods_code", StringType(), True),
                    StructField("relatesTo", StringType(), True),
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
