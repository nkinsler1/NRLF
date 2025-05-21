resource "aws_instance" "web" {
  #   associate_public_ip_address =
  iam_instance_profile = aws_iam_instance_profile.powerbi_profile.name
  ami                  = data.aws_ami.PowerBI_Gateway.id
  instance_type        = var.instance_type
  key_name             = aws_key_pair.ec2_key_pair.key_name
  subnet_id            = var.subnet_id
  security_groups      = var.security_groups

  user_data = file("${path.module}/scripts/user_data.tpl")

  tags = {
    Name = "${var.name_prefix}-ec2"
  }

}

resource "tls_private_key" "instance_key_pair" {
  algorithm = "RSA"
}

resource "aws_key_pair" "ec2_key_pair" {
  key_name   = "${var.name_prefix}_PowerBI-GateWay-Key"
  public_key = tls_private_key.instance_key_pair.public_key_openssh
}

resource "local_file" "ssh_key_priv" {
  filename = "${path.module}/keys/${aws_key_pair.ec2_key_pair.key_name}.pem"
  content  = tls_private_key.instance_key_pair.private_key_pem
}
