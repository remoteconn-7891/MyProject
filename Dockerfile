# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Make migrations


# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 MyProject.wsgi:application
