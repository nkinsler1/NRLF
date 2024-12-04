# S3 Bucket for Raw Data
resource "aws_s3_bucket" "source-data-bucket" {
  bucket = "source-data-bucket"
}

# S3 Bucket for Processed Data
resource "aws_s3_bucket" "target-data-bucket" {
  bucket = "target-data-bucket"
}


# S3 Bucket for Code
resource "aws_s3_bucket" "code-bucket" {
  bucket = "code-bucket"
}

resource "aws_s3_bucket_object""code-data-object" {
  bucket = aws_s3_bucket.code-bucket.bucket
  key    = "main.py"
  source = "${path.module}/src/main.py"
  etag   = "${filemd5("${path.module}/src/main.py")}"
}