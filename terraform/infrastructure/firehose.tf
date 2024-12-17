module "firehose__processor" {
  source               = "./modules/firehose"
  assume_account       = local.aws_account_id
  prefix               = local.prefix
  region               = local.region
  environment          = local.environment
  cloudwatch_kms_arn   = module.kms__cloudwatch.kms_arn
  splunk_environment   = local.splunk_environment
  splunk_index         = local.splunk_index
  destination          = "splunk"
  reporting_bucket_arn = data.aws_s3_bucket.source-data-bucket.arn[count.index]
}
