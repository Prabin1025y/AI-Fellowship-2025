# Use an official Python base image
FROM python:3.11-slim

# get netcat for wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
# create executable from wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Run wait for it and start the application
CMD ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

