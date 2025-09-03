# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (better caching for rebuilds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your whole project into the container
COPY . .

# Set environment variables (optional, but helps with encoding issues)
ENV PYTHONUNBUFFERED=1

# Default command: run playSong.py
ENTRYPOINT ["python", "consoleOutputer.py"]

CMD ["list"]