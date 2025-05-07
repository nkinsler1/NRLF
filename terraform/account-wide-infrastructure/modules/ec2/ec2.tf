module "autoscaling" {
  source  = "registry.terraform.io/terraform-aws-modules/autoscaling/aws"
  version = "6.5.2"

  name = "PowerBI-On-Premise-Gateway"

  min_size         = 0
  max_size         = 1
  desired_capacity = 1

  # Autoscaling Schedule
  schedules = {
    morning_start = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 1
      recurrence       = "50 5 * * 0-6"
      time_zone        = "Europe/Paris"
    }

    morning_stop = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 0
      recurrence       = "30 6 * * 0-6"
      time_zone        = "Europe/Paris"
    }

    noon_start = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 1
      recurrence       = "50 11 * * 0-6"
      time_zone        = "Europe/Paris"
    }

    noon_stop = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 0
      recurrence       = "30 12 * * 0-6"
      time_zone        = "Europe/Paris"
    }

    evening_start = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 1
      recurrence       = "50 17 * * 0-6"
      time_zone        = "Europe/Paris"
    }

    evening_stop = {
      min_size         = -1
      max_size         = -1
      desired_capacity = 0
      recurrence       = "30 18 * * 0-6"
      time_zone        = "Europe/Paris"
    }
  }

  wait_for_capacity_timeout = 0
  health_check_type         = "EC2"
  health_check_grace_period = 300
  enable_monitoring         = false

  #image_id                = data.aws_ami.windows.id  // Phase 2 : we let the Auto Scaling Group use the AMI we've juste created.
  image_id                = data.aws_ami.final.id
  launch_template_version = "$Latest"
  instance_type           = "m5a.large"

  instance_market_options = {
    market_type = "spot"
  }

  # Refresh instances when redeploying
  instance_refresh = {
    strategy = "Rolling"
    triggers = ["tag"]
  }

  # Assign a role to the instance
  create_iam_instance_profile = true
  iam_role_name               = "powerbi-gateway-role"
  iam_role_description        = "Allow the Power BI Gateway to be managed by"
  iam_role_policies = {
    AmazonSSMManagedInstanceCore = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
  }
  key_name = aws_key_pair.ec2_key_pair.key_name

  vpc_zone_identifier = data.aws_subnets.subnets.ids

  security_groups = [module.security-group-outbound.security_group_id]

  user_data              = filebase64("./userdata.txt")
  update_default_version = true
}

############################
# Add rule to db managed group
############################
# module "upgrade_db_sg" {
#   source  = "registry.terraform.io/terraform-aws-modules/security-group/aws"
#   version = "4.13.1"

#   create_sg         = false
#   security_group_id = data.aws_security_group.db_sg.id
#   ingress_with_source_security_group_id = [
#     {
#       description              = "Allow incoming connections from Power BI Gateway"
#       rule                     = "postgresql-tcp"
#       source_security_group_id = module.security-group-outbound.security_group_id
#     },
#   ]
# }

############################
# Key pair for RDP access
############################
resource "tls_private_key" "instance_key_pair" {
  algorithm = "RSA"
}

resource "aws_key_pair" "ec2_key_pair" {
  key_name   = "PowerBI-GateWay-Key"
  public_key = tls_private_key.instance_key_pair.public_key_openssh
}

# Saving Key Pair for ssh login for Client if needed
resource "local_file" "ssh_key" {
  filename = "${aws_key_pair.ec2_key_pair.key_name}.pem"
  content  = tls_private_key.instance_key_pair.private_key_pem
}
