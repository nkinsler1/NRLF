output "target_bucket_name" {
  description = "Name of destination bucket"
  value       = aws_s3_bucket.target-data-bucket.id
}
