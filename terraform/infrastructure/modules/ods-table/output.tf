output "table_name" {
  description = "Name of the ods table"
  value       = aws_dynamodb_table.ods.name
}

output "read_policy_arn" {
  description = "Policy to read from the ods table"
  value       = aws_iam_policy.ods-table-read.arn
}

output "write_policy_arn" {
  description = "Policy to write to the ods table"
  value       = aws_iam_policy.ods-table-write.arn
}

output "kms_read_write_policy_arn" {
  description = "Policy to encrypt and decrypt the ods table with the kms key"
  value       = aws_iam_policy.ods-kms-read-write.arn
}
