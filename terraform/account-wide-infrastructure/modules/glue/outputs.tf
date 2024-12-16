output "target_bucket_name" {
  description = "Name of destination bucket"
  value       = aws_s3_bucket.target-data-bucket.id
}

output "source_bucket_name" {
  description = "Name of source bucket"
  value       = aws_s3_bucket.source-data-bucket.id
}

output "glue_crawler_name" {
  value = "s3//${aws_s3_bucket.source-data-bucket.id}/"
}
