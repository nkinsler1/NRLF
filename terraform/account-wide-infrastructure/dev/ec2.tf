module "vpc" {
  source                        = "../modules/vpc"
  vpc_cidr_block                = var.vpc_cidr_block
  enable_dns_hostnames          = var.enable_dns_hostnames
  vpc_public_subnets_cidr_block = var.vpc_public_subnets_cidr_block
  aws_azs                       = var.aws_azs
  name_prefix                   = "nhsd-nrlf--dev"
}


module "web" {
  source        = "../modules/ec2"
  instance_type = var.instance_type
  instance_key  = var.instance_key
  name_prefix   = "nhsd-nrlf--dev"

  subnet_id       = module.vpc.subnet_id
  security_groups = module.vpc.security_group
}
