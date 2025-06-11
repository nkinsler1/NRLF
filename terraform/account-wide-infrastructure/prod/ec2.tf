module "vpc" {
  source                         = "../modules/vpc"
  vpc_cidr_block                 = var.vpc_cidr_block
  enable_dns_hostnames           = var.enable_dns_hostnames
  vpc_public_subnets_cidr_block  = var.vpc_public_subnets_cidr_block
  vpc_private_subnets_cidr_block = var.vpc_private_subnets_cidr_block
  aws_azs                        = var.aws_azs
  name_prefix                    = "nhsd-nrlf--prod"
}

module "powerbi_gw_instance_v2" {
  source             = "../modules/ec2"
  use_custom_ami     = true
  instance_type      = var.instance_type
  name_prefix        = "nhsd-nrlf--test-powerbi-gw-v2"
  target_bucket_arn  = module.prod-glue.target_bucket_arn
  glue_kms_key_arn   = module.prod-glue.aws_kms_key_arn
  athena_kms_key_arn = module.prod-athena.kms_key_arn
  athena_bucket_arn  = module.prod-athena.bucket_arn

  subnet_id       = module.vpc.private_subnet_id
  security_groups = [module.vpc.powerbi_gw_security_group_id]
}
