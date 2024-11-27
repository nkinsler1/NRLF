output "bucket_name" {
  description = "Name of the reporting S3 bucket"
  value       = aws_s3_bucket.api_truststore.bucket
}

output "certificates_object_key" {
  description = "Key of the reporting certificates object"
  value       = aws_s3_object.api_truststore_certificate.key
}
