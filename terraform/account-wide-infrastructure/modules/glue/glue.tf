# Create Glue Data Catalog Database
resource "aws_glue_catalog_database" "raw_log_database" {
  name         = "raw_log"
  location_uri = "${aws_s3_bucket.source-data-bucket.id}/"
}

# Create Glue Crawler
resource "aws_glue_crawler" "raw_log_crawler" {
  name          = "raw-log-crawler"
  database_name = aws_glue_catalog_database.raw_log_database.name
  role          = aws_iam_role.glue_service_role.name
  s3_target {
    path = "${aws_s3_bucket.source-data-bucket.id}/"
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
resource "aws_glue_trigger" "raw_log_trigger" {
  name = "org-report-trigger"
  type = "ON_DEMAND"
  actions {
    crawler_name = aws_glue_crawler.raw_log_crawler.name
  }
}

resource "aws_glue_job" "glue_job" {
  name              = "poc-glue-job"
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
    "--source-path"                     = "s3://${aws_s3_bucket.source-data-bucket.id}/" # Specify the source S3 path
    "--destination-path"                = "s3://${aws_s3_bucket.target-data-bucket.id}/" # Specify the destination S3 path
    "--job-name"                        = "poc-glue-job"
    "--enable-continuous-log-filter"    = "true"
    "--enable-metrics"                  = "true"
    "--extra-py-files"                  = "s3://${aws_s3_bucket.code-bucket.id}/src.zip"
  }
}

output "glue_crawler_name" {
  value = "s3//${aws_s3_bucket.source-data-bucket.id}/"
}
