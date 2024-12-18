# Set the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /polinomic

# Install system dependencies, including Cython, build-essential, and other required libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    pkg-config \
    libcairo2-dev \
    cmake \
    cython3 \
    build-essential \
    libgirepository1.0-dev \
    gir1.2-gtk-3.0 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt from the root folder to the app folder
COPY requirements.txt /polinomic/

# Upgrade pip, setuptools, and wheel to avoid build issues
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the project files
COPY . /polinomic/

# Expose port 8000 to be accessed by the host
EXPOSE 8000

# Run the Django app (Gunicorn can be used for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
