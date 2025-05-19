module "int-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--int"
  target_bucket_name = module.int-glue.target_bucket_name
}
