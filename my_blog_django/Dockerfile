FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /my_blog_django

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /my_blog_django

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/my_blog_django

COPY entrypoint.sh /my_blog_django/entrypoint.sh

RUN chmod +x /my_blog_django/entrypoint.sh

ENTRYPOINT ["/my_blog_django/entrypoint.sh"]