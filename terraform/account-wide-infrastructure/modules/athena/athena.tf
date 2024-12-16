resource "aws_athena_database" "reporting-db" {
  name = var.database

  bucket = var.target_bucket_name

  #   encryption_configuration {
  #     encryption_option = "SSE_KMS"
  #     kms_key           = aws_kms_key.athena.arn
  #   }

  force_destroy = true
}

resource "aws_athena_workgroup" "athena" {
  name = "${var.name_prefix}-athena-wg"

  configuration {
    enforce_workgroup_configuration    = true
    publish_cloudwatch_metrics_enabled = true

    result_configuration {
      output_location = "s3://{aws_s3_bucket.athena.bucket}/output/"

      encryption_configuration {
        encryption_option = "SSE_KMS"
        kms_key_arn       = aws_kms_key.athena.arn
      }
    }
  }

}
