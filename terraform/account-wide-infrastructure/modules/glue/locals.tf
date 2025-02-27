locals {
  s3 = {
    transition_storage = {
      infrequent_access = {
        storage_class = "STANDARD_IA"
        days          = 150
      }
      glacier = {
        storage_class = "GLACIER"
        days          = 200
      }
    }

    expiration = {
      days = 1095
    }
  }
}
