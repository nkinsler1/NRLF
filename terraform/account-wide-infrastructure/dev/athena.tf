module "dev-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--dev"
  target_bucket_name = module.dev-glue.target_bucket_name
}
