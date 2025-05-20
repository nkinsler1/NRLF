output "subnet_id" {
  value = aws_subnet.public_subnet.id
}

output "private_subnet_id" {
  value = aws_subnet.private_subnet.id
}

output "security_group" {
  value = [aws_security_group.sg.id]
}

output "powerbi_gw_security_group_id" {
  value = aws_security_group.powerbi_gw_sg.id
}
