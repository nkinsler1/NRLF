module "dev-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--dev"
  python_version = 3
}
