resource "aws_kms_key" "athena" {
}

resource "aws_kms_alias" "athena" {
  name          = "alias/${var.prefix}-athena"
  target_key_id = aws_kms_key.athena.key_id
}
