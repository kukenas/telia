FROM python:3.7-slim

MAINTAINER Aurimas Kukenas "kukenas.aurimas@gmail.com"

RUN mkdir -p /app/

# Environment variables:
ENV FILE_TO_RUN="/main.py"

# Copy the entire project, except what is defined in '.dockerignore'
COPY . /app

WORKDIR /app

# In case any external libraries are used
RUN pip install -r /app/requirements.txt

# Make the script executable
RUN chmod +x /app/bin/run_pytests.sh

# Run pytests
RUN ./bin/run_pytests.sh