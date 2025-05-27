variable "assume_account" {
  sensitive = true
}

variable "assume_role" {}

variable "dev_api_domain_name" {
  description = "The internal DNS name of the API Gateway for the dev environment"
  default     = "dev.api.record-locator.dev.national.nhs.uk"
}

variable "devsandbox_api_domain_name" {
  description = "The internal DNS name of the API Gateway for the dev sandbox environment"
  default     = "dev-sandbox.api.record-locator.dev.national.nhs.uk"
}

variable "aws_azs" {
  type        = string
  description = "AWS Availability Zones"
  default     = "eu-west-2a"
}

variable "enable_dns_hostnames" {
  type        = bool
  description = "Enable DNS hostnames in VPC"
  default     = true
}

variable "vpc_cidr_block" {
  type        = string
  description = "Base CIDR Block for VPC"
  default     = "10.0.0.0/16"
}

variable "vpc_public_subnets_cidr_block" {
  type        = string
  description = "CIDR Block for Public Subnets in VPC"
  default     = "10.0.0.0/24"
}

variable "vpc_private_subnets_cidr_block" {
  type        = string
  description = "CIDR Block for Private Subnets in VPC"
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  type        = string
  description = "Type for EC2 Instance"
  default     = "t2.micro"
}

variable "use_custom_ami" {
  type        = bool
  description = "Use custom image"
  default     = false
}
