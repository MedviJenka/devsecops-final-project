output "ec2_instance" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.ec2_app.public_ip
}
