resource "aws_glue_catalog_database" "example" {
 name = "example"
}

resource "aws_glue_job" "example" {
 name = "example"
 role_arn = aws_iam_role.glue.arn
 command {
  script_location = "s3://my-script-location/script.py"
  python_version = "3"
 }
}