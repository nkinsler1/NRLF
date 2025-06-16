module "qa-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--qa"
  target_bucket_name = module.qa-glue.target_bucket_name
  glue_database      = module.qa-glue.glue_database
}

module "int-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--int"
  target_bucket_name = module.int-glue.target_bucket_name
  glue_database      = module.int-glue.glue_database
}

module "int-sandbox-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--int-sandbox"
  target_bucket_name = module.int-sandbox-glue.target_bucket_name
  glue_database      = module.int-sandbox-glue.glue_database
}

module "ref-athena" {
  source             = "../modules/athena"
  name_prefix        = "nhsd-nrlf--ref"
  target_bucket_name = module.ref-glue.target_bucket_name
  glue_database      = module.ref-glue.glue_database
}
