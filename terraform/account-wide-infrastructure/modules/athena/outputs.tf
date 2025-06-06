output "workgroup" {
  value = aws_athena_workgroup.athena
}

output "bucket" {
  value = aws_s3_bucket.athena
}

output "bucket_arn" {
  value = aws_s3_bucket.athena.arn
}

output "kms_key_arn" {
  value = aws_kms_key.athena.arn
}
