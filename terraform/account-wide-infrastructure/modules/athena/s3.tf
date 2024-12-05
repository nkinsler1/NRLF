resource "aws_s3_bucket" "athena" {
  bucket = "athena"
}


resource "aws_s3_bucket_server_side_encryption_configuration" "athena" {
  bucket = aws_s3_bucket.athena.bucket
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.athena.arn
    }
  }

}