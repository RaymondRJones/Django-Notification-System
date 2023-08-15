# Use the official Python image from the dockerhub
FROM python:3.11

# Set the environment variable to make sure Python outputs everything that's printed
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["gunicorn", "yourprojectname.wsgi:application", "--bind", "0.0.0.0:8000"]

