variable "database" {
  description = "What the db will be called"
  default     = "nrl_reporting"
}

variable "name_prefix" {
  type        = string
  description = "The prefix to apply to all resources in the module."
}

variable "target_bucket_name" {
  type = string
}
