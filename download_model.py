#this file used when download the models from the huggingface hub
#this file runs when docker is build or test the model on your local machine

from huggingface_hub import snapshot_download

class downloader:
    def __init__(self):
        pass
    
    def download_models(self):
        # Download all files from the specified
        snapshot_download(
                repo_id="sentence-transformers/all-mpnet-base-v2", 
                local_dir="model_files",
                ignore_patterns=["*.gitignore","*.onnx","*.bin"])
        
if __name__ == '__main__':
    downloader().download_models()