variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
}

variable "public_key" {
  description = "Public key for SSH"
  type        = string
}

variable "security_group_name" {
  description = "Name of the security group"
  type        = string
  default     = "ec2-instance-sg"
}

variable "allowed_ssh_ip" {
  description = "IP address allowed for SSH access (CIDR format)"
  type        = string
  default     = "0.0.0.0/0" # Replace this with a more secure value
}

variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-09a9858973b288bdd" # Amazon Linux 2 AMI
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.large"
}

variable "git_repo_url" {
  description = "Git repository URL to clone"
  type        = string
  default     = "https://github.com/MedviJenka/devsecops-final-project.git"
}

variable "k8s_manifest_path" {
  description = "Path to Kubernetes manifests in the repository"
  type        = string
  default     = "k8s-manifests"
}

variable "tags" {
  description = "Tags to assign to the resources"
  type        = map(string)
  default     = {
    Name = "EC2-Git-K8s"
  }
}
