# S3 Bucket for Raw Data
resource "aws_s3_bucket" "source-data-bucket" {
  bucket = "source-data-bucket"
}

resource "aws_s3_bucket_policy" "source-data-bucket" {
  bucket = "source-data-bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "source-data-bucket-policy"
    Statement = [
      {
        Sid    = "HTTPSOnly"
        Effect = "Deny"
        Principal = {
          "AWS" : "*"
        }
        Action = "s3:*"
        Resource = [
          aws_s3_bucket.source-data-bucket.arn,
          "${aws_s3_bucket.source-data-bucket.arn}/*",
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

resource "aws_s3_bucket_public_access_block" "source-data-bucket-public-access-block" {
  bucket = aws_s3_bucket.source-data-bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}


# S3 Bucket for Processed Data
resource "aws_s3_bucket" "target-data-bucket" {
  bucket = "target-data-bucket"
}

resource "aws_s3_bucket_policy" "target-data-bucket" {
  bucket = "target-data-bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "target-data-bucket-policy"
    Statement = [
      {
        Sid    = "HTTPSOnly"
        Effect = "Deny"
        Principal = {
          "AWS" : "*"
        }
        Action = "s3:*"
        Resource = [
          aws_s3_bucket.target-data-bucket.arn,
          "${aws_s3_bucket.target-data-bucket.arn}/*",
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

resource "aws_s3_bucket_public_access_block" "target-data-bucket-public-access-block" {
  bucket = aws_s3_bucket.target-data-bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# S3 Bucket for Code
resource "aws_s3_bucket" "code-bucket" {
  bucket = "code-bucket"
}

resource "aws_s3_bucket_policy" "code-bucket" {
  bucket = "code-bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "code-bucket-policy"
    Statement = [
      {
        Sid    = "HTTPSOnly"
        Effect = "Deny"
        Principal = {
          "AWS" : "*"
        }
        Action = "s3:*"
        Resource = [
          aws_s3_bucket.code-bucket.arn,
          "${aws_s3_bucket.code-bucket.arn}/*",
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

resource "aws_s3_bucket_public_access_block" "code-bucket-public-access-block" {
  bucket = aws_s3_bucket.code-bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_object" "code-data-object" {
  bucket = aws_s3_bucket.code-bucket.bucket
  key    = "main.py"
  source = "${path.module}/src/main.py"
  etag   = filemd5("${path.module}/src/main.py")
}

data "archive_file" "python" {
  type        = "zip"
  output_path = "${path.module}/files/src.zip"

  source_dir = "${path.module}/src"
}

resource "aws_s3_bucket_object" "code-data-object" {
  bucket = aws_s3_bucket.code-bucket.bucket
  key    = "main.py"
  source = data.archive_file.python
}
