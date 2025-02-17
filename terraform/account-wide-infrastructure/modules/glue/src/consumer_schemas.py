from pyspark.sql.types import (
    BooleanType,
    DoubleType,
    LongType,
    StringType,
    StructField,
    StructType,
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
                                StructField("authorization", StringType(), True),
                                StructField("content-type", StringType(), True),
                                StructField("host", StringType(), True),
                                StructField(
                                    "nhsd-client-rp-details", StringType(), True
                                ),
                                StructField(
                                    "nhsd-connection-metadata", StringType(), True
                                ),
                                StructField("nhsd-correlation-id", StringType(), True),
                                StructField(
                                    "nhsd-end-user-organisation-ods", StringType(), True
                                ),
                                StructField("nhsd-request-id", StringType(), True),
                                StructField("user-agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-forwarded-for", StringType(), True),
                                StructField("x-forwarded-port", StringType(), True),
                                StructField("x-forwarded-proto", StringType(), True),
                                StructField("x-request-id", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("postman-token", StringType(), True),
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
                                StructField("aws_region", StringType(), True),
                                StructField("prefix", StringType(), True),
                                StructField("environment", StringType(), True),
                                StructField("splunk_index", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("auth_store", StringType(), True),
                                StructField("table_name", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField("body", StringType(), True),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_body",
                        StructType(
                            [
                                StructField("subject_identifier", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("custodian_identifier", StringType(), True),
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
                                StructField("indexname", StringType(), True),
                                StructField(
                                    "keyconditionexpression", StringType(), True
                                ),
                                StructField(
                                    "expressionattributevalues",
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
                                                ":patient_sort", StringType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField(
                                    "returnconsumedcapacity", StringType(), True
                                ),
                                StructField("filterexpression", StringType(), True),
                                StructField(
                                    "expressionattributenames",
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
                                StructField("items", StructType([]), True),
                                StructField("count", LongType(), True),
                                StructField("scannedcount", LongType(), True),
                                StructField(
                                    "consumedcapacity",
                                    StructType(
                                        [
                                            StructField(
                                                "tablename", StringType(), True
                                            ),
                                            StructField(
                                                "capacityunits", DoubleType(), True
                                            ),
                                            StructField("table", StructType([]), True),
                                            StructField(
                                                "globalsecondaryindexes",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "patient_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "capacityunits",
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
                                    "responsemetadata",
                                    StructType(
                                        [
                                            StructField(
                                                "requestid", StringType(), True
                                            ),
                                            StructField(
                                                "httpstatuscode", LongType(), True
                                            ),
                                            StructField(
                                                "httpheaders",
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
                    StructField("custodian", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("count", LongType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statuscode", StringType(), True),
                                StructField("body", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("error", StringType(), True),
                    StructField("document", StringType(), True),
                    StructField("exception", StringType(), True),
                    StructField("exception_name", StringType(), True),
                    StructField(
                        "stack_trace",
                        StructType(
                            [
                                StructField("type", StringType(), True),
                                StructField("value", StringType(), True),
                                StructField("module", StringType(), True),
                                StructField("frames", StructType([]), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("bucket", StringType(), True),
                    StructField("key", StringType(), True),
                    StructField("subject_identifier", StringType(), True),
                    StructField("type", StringType(), True),
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
                                StructField("authorization", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("host", StringType(), True),
                                StructField(
                                    "nhsd-client-rp-details", StringType(), True
                                ),
                                StructField(
                                    "nhsd-connection-metadata", StringType(), True
                                ),
                                StructField("nhsd-correlation-id", StringType(), True),
                                StructField(
                                    "nhsd-end-user-organisation-ods", StringType(), True
                                ),
                                StructField("nhsd-request-id", StringType(), True),
                                StructField("postman-token", StringType(), True),
                                StructField("user-agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-forwarded-for", StringType(), True),
                                StructField("x-forwarded-port", StringType(), True),
                                StructField("x-forwarded-proto", StringType(), True),
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
                                StructField("aws_region", StringType(), True),
                                StructField("prefix", StringType(), True),
                                StructField("environment", StringType(), True),
                                StructField("splunk_index", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("auth_store", StringType(), True),
                                StructField("table_name", StringType(), True),
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
                            ]
                        ),
                        True,
                    ),
                    StructField("table_name", StringType(), True),
                    StructField("item_type", StringType(), True),
                    StructField("original_kwargs_keys", StringType(), True),
                    StructField("filtered_kwargs_keys", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("status_code", StringType(), True),
                    StructField(
                        "response",
                        StructType(
                            [
                                StructField("statuscode", StringType(), True),
                                StructField("body", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("nhs_number", StringType(), True),
                    StructField(
                        "query",
                        StructType(
                            [
                                StructField("indexname", StringType(), True),
                                StructField(
                                    "keyconditionexpression", StringType(), True
                                ),
                                StructField(
                                    "expressionattributevalues",
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
                                                ":patient_sort", StringType(), True
                                            ),
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
                                    "returnconsumedcapacity", StringType(), True
                                ),
                                StructField("filterexpression", StringType(), True),
                                StructField(
                                    "expressionattributenames",
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
                                StructField("items", StructType([]), True),
                                StructField("count", LongType(), True),
                                StructField("scannedcount", LongType(), True),
                                StructField(
                                    "consumedcapacity",
                                    StructType(
                                        [
                                            StructField(
                                                "tablename", StringType(), True
                                            ),
                                            StructField(
                                                "capacityunits", DoubleType(), True
                                            ),
                                            StructField("table", StructType([]), True),
                                            StructField(
                                                "globalsecondaryindexes",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "patient_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "capacityunits",
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
                                    "responsemetadata",
                                    StructType(
                                        [
                                            StructField(
                                                "requestid", StringType(), True
                                            ),
                                            StructField(
                                                "httpstatuscode", LongType(), True
                                            ),
                                            StructField(
                                                "httpheaders",
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
                    StructField("custodian", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("count", LongType(), True),
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
                                StructField("authorization", StringType(), True),
                                StructField("cache-control", StringType(), True),
                                StructField("host", StringType(), True),
                                StructField(
                                    "nhsd-client-rp-details", StringType(), True
                                ),
                                StructField(
                                    "nhsd-connection-metadata", StringType(), True
                                ),
                                StructField("nhsd-correlation-id", StringType(), True),
                                StructField(
                                    "nhsd-end-user-organisation-ods", StringType(), True
                                ),
                                StructField("nhsd-request-id", StringType(), True),
                                StructField("postman-token", StringType(), True),
                                StructField("user-agent", StringType(), True),
                                StructField("x-correlation-id", StringType(), True),
                                StructField("x-forwarded-for", StringType(), True),
                                StructField("x-forwarded-port", StringType(), True),
                                StructField("x-forwarded-proto", StringType(), True),
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
                                StructField("aws_region", StringType(), True),
                                StructField("prefix", StringType(), True),
                                StructField("environment", StringType(), True),
                                StructField("splunk_index", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("auth_store", StringType(), True),
                                StructField("table_name", StringType(), True),
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
                                StructField("statuscode", StringType(), True),
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

countDocumentReferenceSchema = StructType(
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
                                StructField("authorization", StringType(), True),
                                StructField("host", StringType(), True),
                                StructField(
                                    "nhsd-client-rp-details", StringType(), True
                                ),
                                StructField(
                                    "nhsd-connection-metadata", StringType(), True
                                ),
                                StructField("nhsd-correlation-id", StringType(), True),
                                StructField("user-agent", StringType(), True),
                                StructField("x-forwarded-for", StringType(), True),
                                StructField("x-request-id", StringType(), True),
                                StructField(
                                    "nhsd-end-user-organisation-ods", StringType(), True
                                ),
                                StructField("nhsd-request-id", StringType(), True),
                                StructField("x-forwarded-port", StringType(), True),
                                StructField("x-forwarded-proto", StringType(), True),
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
                                StructField("aws_region", StringType(), True),
                                StructField("prefix", StringType(), True),
                                StructField("environment", StringType(), True),
                                StructField("splunk_index", StringType(), True),
                                StructField("source", StringType(), True),
                                StructField("auth_store", StringType(), True),
                                StructField("table_name", StringType(), True),
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
                    StructField("pointer_types", StringType(), True),
                    StructField(
                        "params",
                        StructType(
                            [StructField("subject:identifier", StringType(), True)]
                        ),
                        True,
                    ),
                    StructField("model", StringType(), True),
                    StructField(
                        "parsed_params",
                        StructType(
                            [StructField("subject_identifier", StringType(), True)]
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
                                StructField("indexname", StringType(), True),
                                StructField(
                                    "keyconditionexpression", StringType(), True
                                ),
                                StructField(
                                    "expressionattributevalues",
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
                                StructField("select", StringType(), True),
                                StructField(
                                    "returnconsumedcapacity", StringType(), True
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
                                StructField("count", LongType(), True),
                                StructField("scannedcount", LongType(), True),
                                StructField(
                                    "consumedcapacity",
                                    StructType(
                                        [
                                            StructField(
                                                "tablename", StringType(), True
                                            ),
                                            StructField(
                                                "capacityunits", DoubleType(), True
                                            ),
                                            StructField("table", StructType([]), True),
                                            StructField(
                                                "globalsecondaryindexes",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "patient_gsi",
                                                            StructType(
                                                                [
                                                                    StructField(
                                                                        "capacityunits",
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
                                    "responsemetadata",
                                    StructType(
                                        [
                                            StructField(
                                                "requestid", StringType(), True
                                            ),
                                            StructField(
                                                "httpstatuscode", LongType(), True
                                            ),
                                            StructField(
                                                "httpheaders",
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
                                StructField("statuscode", StringType(), True),
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

consumerSchemaList = {
    "consumer--countDocumentReference": countDocumentReferenceSchema,
    "consumer--searchPostDocumentReference": searchPostDocumentReferenceSchema,
    "consumer--searchDocumentReference": searchDocumentReferenceSchema,
    "consumer--readDocumentReference": readDocumentReferenceSchema,
}
