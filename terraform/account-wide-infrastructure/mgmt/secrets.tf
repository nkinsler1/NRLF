resource "aws_secretsmanager_secret" "identities_account_id" {
  name = "${local.project}--nhs-identities-account-id"
}
