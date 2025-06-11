module "int-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--int"
  python_version = 3
}

module "int-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--int-sandbox"
  python_version = 3
}

module "int-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--qa"
  python_version = 3
}

module "int-glue" {
  source         = "../modules/glue"
  name_prefix    = "nhsd-nrlf--ref"
  python_version = 3
}
