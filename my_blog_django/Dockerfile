# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

# Set the working directory inside the container
WORKDIR /my_blog_django

# Install system dependencies and Node.js
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g gulp-cli  # Install Gulp globally

# Copy the project files into the container
COPY . /my_blog_django

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN cd frontend && npm install

# Set the Python path
ENV PYTHONPATH=/my_blog_django

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /my_blog_django/entrypoint.sh
RUN chmod +x /my_blog_django/entrypoint.sh

# Define the entrypoint for the container
ENTRYPOINT ["/my_blog_django/entrypoint.sh"]
