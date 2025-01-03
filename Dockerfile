# Use the official Python image from the Docker Hub
FROM python:3.11

# Install SDL2 and other necessary libraries
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run your FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
