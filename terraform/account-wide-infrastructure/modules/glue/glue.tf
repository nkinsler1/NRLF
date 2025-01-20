# Create Glue Data Catalog Database
resource "aws_glue_catalog_database" "log_database" {
  name         = "${var.name_prefix}-reporting"
  location_uri = "${aws_s3_bucket.target-data-bucket.id}/logs/"
}

# Create Glue Crawler
resource "aws_glue_crawler" "log_crawler" {
  name          = "${var.name_prefix}-log-crawler"
  database_name = aws_glue_catalog_database.log_database.name
  role          = aws_iam_role.glue_service_role.name
  s3_target {
    path = "${aws_s3_bucket.target-data-bucket.id}/logs/"
  }
  schema_change_policy {
    delete_behavior = "LOG"
  }
  configuration = jsonencode({
    "Version" : 1.0,
    "Grouping" : {
      "TableGroupingPolicy" : "CombineCompatibleSchemas"
    }
  })
}
resource "aws_glue_trigger" "log_trigger" {
  name = "${var.name_prefix}-org-report-trigger"
  type = "ON_DEMAND"
  actions {
    crawler_name = aws_glue_crawler.log_crawler.name
  }
}

resource "aws_glue_job" "glue_job" {
  name              = "${var.name_prefix}-glue-job"
  role_arn          = aws_iam_role.glue_service_role.arn
  description       = "Transfer logs from source to bucket"
  glue_version      = "4.0"
  worker_type       = "G.1X"
  timeout           = 2880
  max_retries       = 1
  number_of_workers = 2
  command {
    name            = "glueetl"
    python_version  = var.python_version
    script_location = "s3://${aws_s3_bucket.code-bucket.id}/main.py"
  }

  default_arguments = {
    "--enable-auto-scaling"             = "true"
    "--enable-continous-cloudwatch-log" = "true"
    "--datalake-formats"                = "delta"
    "--source_path"                     = "s3://${aws_s3_bucket.source-data-bucket.id}/"     # Specify the source S3 path
    "--target_path"                     = "s3://${aws_s3_bucket.target-data-bucket.id}/logs" # Specify the destination S3 path
    "--job_name"                        = "${var.name_prefix}-glue-job"
    "--enable-continuous-log-filter"    = "true"
    "--enable-metrics"                  = "true"
    "--extra-py-files"                  = "s3://${aws_s3_bucket.code-bucket.id}/src.zip"
  }
}
