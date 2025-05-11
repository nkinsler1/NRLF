variable "name_prefix" {
  type        = string
  description = "The prefix to apply to all resources in the module."
}
variable "common_tags" {}
variable "instance_type" {}
variable "instance_key" {}
variable "security_groups" {}
variable "subnet_id" {}
