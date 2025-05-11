# Create the Linux EC2 Web server
resource "aws_instance" "web" {
  ami             = data.aws_ami.windows-2019.id
  instance_type   = var.instance_type
  key_name        = var.instance_key
  subnet_id       = var.subnet_id
  security_groups = var.security_groups

  user_data = file("${path.module}/scripts/user_data.tpl")

  tags = {
    Name = "${var.name_prefix}-ec2"
  }

}
