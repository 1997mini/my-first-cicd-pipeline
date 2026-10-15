# Use an official, lightweight Python runtime as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy our python script into the container
COPY app.py .

# Run the script when the container starts up
CMD ["python", "app.py"]
