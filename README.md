# Setup Instructions
before you do the following things, I highly suggest you to use virtual python environment
## Step 0: Create a Python Virtual Environment

Before installing dependencies, it's recommended to create and activate a Python virtual environment. This helps manage project-specific packages and avoid conflicts with other projects.

### Using `venv` (Python 3.3+)

1. **Create the Virtual Environment**

    Open your terminal and navigate to your project directory. Then run:

    ```sh
    python3 -m venv env
    ```

    This command creates a virtual environment named `env` in your project directory.

2. **Activate the Virtual Environment**

    - **On Linux and macOS:**

        ```sh
        source env/bin/activate
        ```

    - **On Windows:**

        ```sh
        .\env\Scripts\activate
        ```

3. **Verify Activation**

    Once activated, your terminal prompt will change to indicate that you are now working inside the virtual environment. It typically looks like `(env)` preceding your command prompt.

4. **Deactivate the Virtual Environment**

    To deactivate the virtual environment and return to the global Python environment, simply run:

    ```sh
    deactivate
    ```

### Additional Tips

- **Installing Packages:**

    With the virtual environment activated, you can install packages using `pip` without affecting the global Python installation:

    ```sh
    pip install -r requirements.txt
    ```

- **Freezing Dependencies:**

    To generate a `requirements.txt` file with all installed packages, run:

    ```sh
    pip freeze > requirements.txt
    ```

- **Removing the Virtual Environment:**

    If you need to remove the virtual environment, deactivate it first and then delete the `env` directory:

    ```sh
    deactivate
    rm -rf env  # On Linux and macOS
    rmdir /s /q env  # On Windows
    ```

## Step 1: Install PyTorch

First, install PyTorch. You can find the appropriate installation command for your system and preferences on the [PyTorch website](https://pytorch.org/get-started/locally/).

For example, to install PyTorch with CUDA support, you can use the following command:

```sh
pip install torch torchvision torchaudio
```
## Step 1: Install PyTorch

First, install PyTorch. You can find the appropriate installation command for your system and preferences on the [PyTorch website](https://pytorch.org/get-started/locally/).

For example, to install PyTorch with CUDA support, you can use the following command:

```sh
pip install torch
```
If you prefer to install PyTorch without CUDA support, use:
```sh
pip install torch cpuonly
```

## Step 2: Install Requirements
After installing PyTorch, install the required dependencies listed in the **requirements.txt** file. Run the following command in your terminal:

```sh
pip install -r requirements.txt
```

# Building and Running the Docker Image

Follow these instructions to build and run your Docker image for the PyTorch project.

## Prerequisites

- **Docker** installed on your Linux machine. If not installed, follow the [Docker installation guide](https://docs.docker.com/engine/install/).

## Step 1: Navigate to Project Directory

Open your terminal and navigate to the root directory of your project where the `Dockerfile` is located.

## Step 2: Build the Docker Image
```sh
docker build -t emerging_topic_backend:latest .
```
## Step 3: Run the Docker Container
After building the image, run a container using the following command:

```sh
docker run --rm -it emerging_topic_backend:latest
```

- **--rm**: Automatically removes the container when it exits.
- **-it**: Runs the container in interactive mode with a terminal.
the output should be:
```
Fetching 15 files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 3088.74it/s]
(11, 768)
tensor([[ 1.0000,  0.6601,  0.5899, -0.0559, -0.0720,  0.2464,  0.1883,  0.0325,
          0.0723,  0.0285,  0.0371],
        [ 0.6601,  1.0000,  0.4219, -0.0216, -0.0341,  0.2232,  0.1767,  0.0480,
          0.0187,  0.0091,  0.0262],
        [ 0.5899,  0.4219,  1.0000, -0.0298, -0.0650,  0.1912,  0.1000, -0.0189,
         -0.0352,  0.0080, -0.0153],
        [-0.0559, -0.0216, -0.0298,  1.0000,  0.6710, -0.0135, -0.0626, -0.0273,
         -0.0621,  0.0623,  0.0202],
        [-0.0720, -0.0341, -0.0650,  0.6710,  1.0000, -0.0153, -0.0368, -0.0452,
         -0.0251,  0.0627,  0.0226],
        [ 0.2464,  0.2232,  0.1912, -0.0135, -0.0153,  1.0000,  0.7352,  0.0197,
          0.0381,  0.0825,  0.1189],
        [ 0.1883,  0.1767,  0.1000, -0.0626, -0.0368,  0.7352,  1.0000,  0.0059,
          0.0806,  0.0647,  0.1632],
        [ 0.0325,  0.0480, -0.0189, -0.0273, -0.0452,  0.0197,  0.0059,  1.0000,
          0.6435,  0.1828,  0.1590],
        [ 0.0723,  0.0187, -0.0352, -0.0621, -0.0251,  0.0381,  0.0806,  0.6435,
          1.0000,  0.1775,  0.1287],
        [ 0.0285,  0.0091,  0.0080,  0.0623,  0.0627,  0.0825,  0.0647,  0.1828,
          0.1775,  1.0000,  0.8002],
        [ 0.0371,  0.0262, -0.0153,  0.0202,  0.0226,  0.1189,  0.1632,  0.1590,
          0.1287,  0.8002,  1.0000]])
```

## Additional Commands
- List Docker Images:

```sh 
docker images
```
- List Running Containers:

```sh 
docker ps
```
- Stop a Running Container:

```sh 
docker stop <container_id>
```