locals {
  # Adjust these as required
  project_name     = "nrlf-test-backup"
  environment_name = "dev"

  source_account_id      = data.aws_arn.source_terraform_role.account
  destination_account_id = data.aws_caller_identity.current.account_id
}
