resource "aws_iam_policy" "ods-table-read" {
  name        = "${var.name_prefix}-ods-table-read"
  description = "Read the ods-table"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ]
        Effect = "Allow"
        Resource = [
          aws_kms_key.ods-table-key.arn
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "dynamodb:Query",
          "dynamodb:Scan",
          "dynamodb:GetItem",
        ],
        Resource = [
          "${aws_dynamodb_table.ods.arn}*"
        ]
      }
    ]
  })
}

resource "aws_iam_policy" "ods-table-write" {
  name        = "${var.name_prefix}-ods-table-write"
  description = "Write to the ods-table"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:Encrypt",
          "kms:GenerateDataKey"
        ]
        Effect = "Allow"
        Resource = [
          aws_kms_key.ods-table-key.arn
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem",
        ],
        Resource = [
          "${aws_dynamodb_table.ods.arn}*"
        ]
      }
    ]
  })
}

resource "aws_iam_policy" "ods-kms-read-write" {
  name        = "${var.name_prefix}-ods-kms-read-write"
  description = "Encrypt and decrypt with the ods table kms key"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "kms:Decrypt",
          "kms:DescribeKey",
          "kms:Encrypt",
          "kms:GenerateDataKey"
        ]
        Effect = "Allow"
        Resource = [
          aws_kms_key.ods-table-key.arn
        ]
      }
    ]
  })
}
