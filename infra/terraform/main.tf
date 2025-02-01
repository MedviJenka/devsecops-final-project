// The script now initializes a Kubernetes cluster on the EC2 instance after pulling the Git repository.
// It installs Kubernetes components, sets up the kubeconfig, applies a Flannel CNI for networking, and deploys
// any Kubernetes manifests found in your repository under the k8s-manifests folder.


// TODO: understand implementation
provider "aws" {
  region = var.region
}

# Key Pair
resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = var.public_key
}

# Security Group
resource "aws_security_group" "instance_sg" {
  name        = var.security_group_name
  description = "Allow SSH and application access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "ec2_app" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.instance_sg.name]

  user_data = templatefile("${path.module}/user_data.sh", {
    git_repo_url   = var.git_repo_url
    k8s_manifest_path = var.k8s_manifest_path
  })

  tags = var.tags
}

output "ec2_instance_public_ip" {
  value = aws_instance.ec2_app.public_ip
}
