data "aws_arn" "source_terraform_role" {
  arn = var.source_terraform_role_arn
}

data "aws_caller_identity" "current" {}
