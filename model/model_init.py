import json
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Obtenir le chemin absolu du répertoire actuel
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data_and_index():
    # Utiliser des chemins absolus pour les fichiers
    json_path = os.path.join(BASE_DIR, "model", "constitution.json")
    embeddings_path = os.path.join(BASE_DIR, "model", "constitution_embeddings_Multilingual.npy")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            articles_info = json.load(f)
        
        embeddings = np.load(embeddings_path)
        index = faiss.IndexFlatIP(embeddings.shape[1])
        faiss.normalize_L2(embeddings)
        index.add(embeddings)
        return articles_info, index
    except FileNotFoundError as e:
        print(f"Erreur: Fichier introuvable. Chemin complet: {e.filename}")
        print(f"Répertoire de base: {BASE_DIR}")
        print(f"Contenu du répertoire model:", os.listdir(os.path.join(BASE_DIR, "model")))
        raise

def generate_query_embedding(query, model_path):
    model = SentenceTransformer(model_path)
    return model.encode(query)

def faiss_search(index, query_embedding, k=3):
    query_embedding = query_embedding.reshape(1, -1)
    faiss.normalize_L2(query_embedding)
    distances, indices = index.search(query_embedding, k)
    return indices[0], distances[0]

def generate_answer_with_groq(question, context):
    prompt = f"""
You are a legal assistant specialized in constitutional law.
You are given excerpts from the Constitution below.

Context:
{context}

Question: {question}

Answer based only on the context above. If the information is missing, reply with "I can only answer questions related to the Moroccan Constitution and I couldn't find this information in the available articles."
"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )
    return response.choices[0].message.content

def answer_question_rag_with_groq(question, index, articles_info):
    model_path = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    query_embedding = generate_query_embedding(question, model_path)
    indices, _ = faiss_search(index, query_embedding, k=3)

    context = ""
    for idx in indices:
        article_id = articles_info[idx]["Article"]
        content = articles_info[idx]["Content"]
        context += f"Article {article_id}: {content}\n\n"

    return generate_answer_with_groq(question, context), indices