from sentence_transformers import SentenceTransformer
from download_model import downloader
import uvicorn
from fastapi_service import app

def is_docker():
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            return 'docker' in f.read()
    except FileNotFoundError:
        return False

if is_docker():
    print("Running inside Docker")
else:
    print("Not running inside Docker")

if True:

    # Download all files from the specified repository
    downloader().download_models()

    model = SentenceTransformer("model_files")
    corpus = [
    "A man is eating food.",
    "A man is eating a piece of bread.",
    "A man is eating pasta.",
    "The girl is carrying a baby.",
    "The baby is carried by the woman",
    "A man is riding a horse.",
    "A man is riding a white horse on an enclosed ground.",
    "A monkey is playing drums.",
    "Someone in a gorilla costume is playing a set of drums.",
    "A cheetah is running behind its prey.",
    "A cheetah chases prey on across a field.",
    ]
    embeddings = model.encode(corpus)
    print(embeddings.shape)
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)

    #following code handing the api
    #this line  will execute the fastapi_service.py first
    port = 8800
    if is_docker():
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        uvicorn.run(app, host="127.0.0.1", port=port)
