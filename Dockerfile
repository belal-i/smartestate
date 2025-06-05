FROM python:3.12-slim-bullseye

LABEL version="0.3.0"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml /app/
RUN mkdir /app/smartestate/ && \
    pip install --upgrade pip && pip install .

# Copy code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
