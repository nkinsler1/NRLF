module "prod-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--prod"
  python_version = 3
}
