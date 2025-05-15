module "vpc" {
  source                        = "../modules/vpc"
  vpc_cidr_block                = var.vpc_cidr_block
  enable_dns_hostnames          = var.enable_dns_hostnames
  vpc_public_subnets_cidr_block = var.vpc_public_subnets_cidr_block
  aws_azs                       = var.aws_azs
  name_prefix                   = "nhsd-nrlf--dev"
}


module "ec2" {
  source             = "../modules/ec2"
  instance_type      = var.instance_type
  name_prefix        = "nhsd-nrlf--dev"
  target_bucket_arn  = module.dev-glue.target_bucket_arn
  glue_kms_key_arn   = module.dev-glue.aws_kms_key_arn
  athena_kms_key_arn = module.dev-athena.kms_key_arn
  athena_bucket_arn  = module.dev-athena.bucket_arn


  subnet_id       = module.vpc.subnet_id
  security_groups = module.vpc.security_group
}
