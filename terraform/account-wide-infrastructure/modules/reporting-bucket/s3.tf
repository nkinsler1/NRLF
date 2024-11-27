resource "aws_s3_bucket" "reporting" {
  bucket        = "${var.name_prefix}-reporting"
  force_destroy = var.enable_bucket_force_destroy
}

resource "aws_s3_bucket_policy" "reporting_bucket_policy" {
  bucket = aws_s3_bucket.reporting.id

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "reporting_bucket_policy"
    Statement = [
      {
        Sid       = "HTTPSOnly"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource = [
          aws_s3_bucket.reporting.arn,
          "${aws_s3_bucket.reporting.arn}/*",
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      },
    ]
  })
}

resource "aws_s3_bucket_public_access_block" "reporting-public-access-block" {
  bucket = aws_s3_bucket.reporting.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "reporting" {
  bucket = aws_s3_bucket.reporting.bucket

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "reporting" {
  bucket = aws_s3_bucket.reporting.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_object" "reporting_certificate" {
  bucket = aws_s3_bucket.reporting.bucket
  key    = "certificates.pem"
  source = var.server_certificate_file
  etag   = filemd5(var.server_certificate_file)
}
