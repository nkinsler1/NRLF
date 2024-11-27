output "bucket_name" {
  description = "Name of the truststore S3 bucket"
  value       = aws_s3_bucket.reporting.bucket
}

output "certificates_object_key" {
  description = "Key of the truststore certificates object"
  value       = aws_s3_object.reporting.key
}
