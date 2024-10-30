resource "aws_kms_key" "ods-table-key" {
  description             = "Document ods table KMS key"
  deletion_window_in_days = var.kms_deletion_window_in_days

}

resource "aws_kms_alias" "ods-table-alias" {
  name          = "alias/${var.name_prefix}-ods-table-key"
  target_key_id = aws_kms_key.ods-table-key.key_id
}
