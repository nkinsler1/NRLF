resource "aws_athena_database" "reporting-db" {
  name = var.database

  bucket = aws_s3_bucket.target-data-bucket.bucket

#   encryption_configuration {
#     encryption_option = var.encryption_option
#     kms_key           = var.kms_key_arn
#   }

  force_destroy = true
}

resource "aws_athena_workgroup" "athena" {
  name = var.name_prefix

  configuration {
    enforce_workgroup_configuration    = true
    publish_cloudwatch_metrics_enabled = true

    result_configuration {
      output_location = "s3://{aws_s3_bucket.example.bucket}/output/"

      encryption_configuration {
        encryption_option = "SSE_KMS"
        kms_key_arn       = var.kms_key_arn
      }
    }
  }

  tags = var.common_tags
}