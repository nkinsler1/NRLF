locals {
  # Adjust these as required
  project_name     = "nrlf-test-backup"
  environment_name = "test"

  source_account_id      = var.source_account_id
  destination_account_id = var.assume_account
}
