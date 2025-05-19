resource "aws_ecr_repository" "repository" {
  name                 = "${local.project}-ci-build"
  image_tag_mutability = "MUTABLE"
}

data "aws_iam_policy_document" "codebuild_access_policy" {
  statement {
    sid    = "CodeBuildEcrAccess"
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["codebuild.amazonaws.com"]
    }

    actions = [
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
      "ecr:BatchCheckLayerAvailability",
    ]

    condition {
      test     = "StringEquals"
      variable = "aws:SourceAccount"
      values   = ["${data.aws_caller_identity.current.account_id}"]
    }
  }
}

resource "aws_ecr_repository_policy" "codebuild_access_policy" {
  repository = aws_ecr_repository.repository.name
  policy     = data.aws_iam_policy_document.codebuild_access_policy.json
}
