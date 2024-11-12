from sentence_transformers import SentenceTransformer
from download_model import downloader


if __name__ == '__main__':

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