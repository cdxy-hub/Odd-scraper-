FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY ./app /app/app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
