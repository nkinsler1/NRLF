#terraform {
#  backend "s3" {
#    bucket         = "project-env-backup-tf-bucket"  # change this to the destination account terraform state s3 bucket name
#    key            = "project-env-backup.tfstate"  # change this to the destination account terraform state s3 key name
#    dynamodb_table = "project-env-backup-lock-table"  # change this to the destination account terraform state dynamodb table name
#    region = "eu-west-2"
#  }
#}


provider "aws" {
  alias  = "source"
  region = "eu-west-2"
}
