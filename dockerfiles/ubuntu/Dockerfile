# Use an Ubuntu base image
FROM ubuntu:latest

# Set a maintainer label
LABEL maintainer="you@example.com"

# Update package repository and install basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    python3 \
    python3-pip \
    && apt-get clean \

# Set the working directory inside the container
WORKDIR /app

# Copy application files (if needed)
COPY . /app

# Set an entrypoint for debugging or runtime execution
ENTRYPOINT ["bash"]
