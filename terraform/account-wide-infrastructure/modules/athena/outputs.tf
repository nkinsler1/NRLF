output "workgroup" {
  value = aws_athena_workgroup.athena
}

output "bucket" {
  value = aws_s3_bucket.athena
}

output "database" {
  value = aws_athena_database.reporting-db
}