module "prod-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--prod"
  target_bucket_name = module.prod-glue.target_bucket_name
}
