#!/bin/bash


python3 --version
pip3 --version
docker --version
docker-compose --version

pip3 -m venv ./venv
source venv/bin/activate
docker-compose build
docker-compose up -d
