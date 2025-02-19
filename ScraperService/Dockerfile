# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file to the working directory
COPY requirement.txt .

# Install any needed packages specified in requirement.txt
RUN pip install --no-cache-dir -r requirement.txt

# Copy the source code from the src folder into the container
COPY src/ .

# Set the default command to run your consumer script
CMD ["python", "consumer.py"]
