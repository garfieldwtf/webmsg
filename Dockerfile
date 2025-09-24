# Use python:alpine3.21 as the base image
FROM python:alpine3.21

# Set environment variable for the custom message
ENV MESSAGE="Hello, Docker World!"

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/app.py

# Expose port 8080
EXPOSE 8080

# Run the app
CMD ["python3", "app.py"]

