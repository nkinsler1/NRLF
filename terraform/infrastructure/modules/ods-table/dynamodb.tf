resource "aws_dynamodb_table" "ods" {
  name                        = "${var.name_prefix}-ods-table"
  billing_mode                = "PAY_PER_REQUEST"
  hash_key                    = "pk"
  range_key                   = "sk"
  deletion_protection_enabled = var.enable_deletion_protection

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }

  server_side_encryption {
    enabled     = true
    kms_key_arn = aws_kms_key.ods-table-key.arn
  }

  point_in_time_recovery {
    enabled = var.enable_pitr
  }
}
