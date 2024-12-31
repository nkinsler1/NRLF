locals {
  s3 = {
    transition_storage = {
      infrequent_access = {
        storage_class = "STANDARD_IA"
        days          = 150
      }
      glacier = {
        storage_class = "GLACIER"
        days          = 200
      }
    }

    expiration = {
      days = 1095
    }
  }

  cloudwatch = {
    retention = {
      days = 30
    }
  }

  s3_configuration = {
    # Note could add partition key info to prefix to help debug, requires more investigation
    prefix              = "!{timestamp:yyyy}/!{timestamp:MM}/!{timestamp:dd}/!{timestamp:HH}/"
    error_output_prefix = "${var.error_prefix}/!{timestamp:yyyy}/!{timestamp:MM}/!{timestamp:dd}/!{timestamp:HH}/!{firehose:error-output-type}/"
    buffer_size         = 5
    buffer_interval     = 300
    compression_format  = "GZIP"
  }

  iam_firehose = {
    cloudwatch_reporting_log_group_arn  = var.reporting_infra_toggle ? aws_cloudwatch_log_group.firehose_reporting[0].arn : null
    cloudwatch_reporting_log_stream_arn = var.reporting_infra_toggle ? aws_cloudwatch_log_stream.firehose_reporting[0].arn : null
  }

  iam_subscriptions = {
    firehose_reporting_stream_arn = var.reporting_infra_toggle ? aws_kinesis_firehose_delivery_stream.reporting_stream[0].arn : null
  }

  iam_kms_resources = compact([
    aws_kms_key.firehose.arn,
    var.reporting_kms_arn
  ])

}
