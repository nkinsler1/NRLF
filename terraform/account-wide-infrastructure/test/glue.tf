module "int-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--int"
  python_version = 3
}
