# Use the official PyTorch image from Docker Hub
FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Print a message before downloading the model
RUN echo "Starting model download, it may take time and looks stuck, please be patient" && \
    python download_model.py && \
    echo "Model downloaded successfully."

EXPOSE 8800

# Specify the command to run the application
CMD ["python", "entry.py"]
