#param(
#    [Parameter(Mandatory = $true)]
#    [string]$docker_username,
#    [Parameter(Mandatory = $true)]
#    [SecureString]$docker_password
#)


Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# Check versions
python --version
pip --version
docker --version
docker-compose --version

# Create a virtual environment
python -m venv ./venv

# Build and start Docker Compose
docker-compose build
docker scout quickview
docker-compose up -d

# Retrieve Jenkins initial admin password
# docker exec -it jenkins sh
# cat /var/jenkins_home/secrets/initialAdminPassword
