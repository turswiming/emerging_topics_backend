# Use the official PyTorch image from Docker Hub
FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Download the model file from Hugging Face
RUN python download_model.py

# Specify the command to run the application
CMD ["python", "entry.py"]