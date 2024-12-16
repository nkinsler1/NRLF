resource "aws_kms_key" "glue" {
}

resource "aws_kms_alias" "glue" {
  name          = "alias/${var.name_prefix}-glue"
  target_key_id = aws_kms_key.glue.key_id
}
