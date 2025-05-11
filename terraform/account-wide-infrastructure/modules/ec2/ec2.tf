# Create the Linux EC2 Web server
resource "aws_instance" "web" {
  ami             = data.aws_ami.windows-2019.id
  instance_type   = var.instance_type
  key_name        = aws_key_pair.ec2_key_pair.key_name
  subnet_id       = var.subnet_id
  security_groups = var.security_groups

  user_data = file("${path.module}/scripts/user_data.tpl")

  tags = {
    Name = "${var.name_prefix}-ec2"
  }

}

# Key pair for RDP access
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
