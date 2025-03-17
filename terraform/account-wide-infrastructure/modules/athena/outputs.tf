output "workgroup" {
  value = aws_athena_workgroup.athena
}

output "bucket" {
  value = aws_s3_bucket.athena
}
