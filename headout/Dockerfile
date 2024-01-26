# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE headout.settings

# Create and set the working directory
WORKDIR /app
COPY requirements.txt .

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Allocate maximum of 1500 MB RAM and 2000m/2 Core CPU
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "headout.wsgi:application"]

