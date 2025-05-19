locals {
  s3 = {
    transition_storage = {
      infrequent_access = {
        storage_class = "STANDARD_IA"
        days          = 2
      }
      glacier = {
        storage_class = "GLACIER"
        days          = 7
      }
    }

    expiration = {
      days = 1095
    }
  }
}
