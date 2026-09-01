# Assistant Constitution Marocaine

Un assistant digital intelligent pour répondre aux questions sur la Constitution du Royaume du Maroc en utilisant des techniques de RAG (Retrieval Augmented Generation) et l'API Groq.

![Constitution Marocaine](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Morocco.svg/200px-Flag_of_Morocco.svg.png)

## 📝 Description

Ce projet est un assistant conversationnel qui permet aux utilisateurs de poser des questions sur la Constitution du Maroc. L'application utilise une architecture RAG (Retrieval Augmented Generation) pour :

1. Rechercher les articles pertinents de la Constitution
2. Générer des réponses précises basées sur ces articles via l'API Groq (LLaMA 3 70B)

## 🚀 Fonctionnalités

- Interface utilisateur intuitive et responsive
- Recherche sémantique d'articles pertinents grâce à FAISS
- Génération de réponses précises basées sur les articles retrouvés
- Indication des sources utilisées pour chaque réponse
- Design aux couleurs du Maroc

## 🛠 Technologies utilisées

- *Backend*: Python, Flask
- *Frontend*: HTML, CSS, JavaScript
- *Recherche sémantique*: FAISS, Sentence-Transformers
- *Génération de texte*: API Groq (LLaMA 3 70B)
- *Traitement de documents*: PDFMiner

## 📋 Prérequis

- Python 3.8+
- Une clé API Groq valide

## ⚙ Installation

1. Clonez ce dépôt :
bash
git clone https://github.com/medsaa0/constitutionRAG.git
cd constitutionRAG


2. Créez un environnement virtuel et activez-le :
bash
python -m venv venv 
source venv/bin/activate  # Sur Windows : venv\Scripts\activate


3. Installez les dépendances :
bash
pip install -r requirements.txt


4. Configurez votre clé API Groq dans model/model_init.py :
python
client = Groq(api_key="votre-clé-api-groq")


5. Lancez l'application :
bash
python app.py 


6. Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:5000

## 📂 Structure du projet


assistant-constitution-maroc/
├── app.py                    # Point d'entrée de l'application Flask
├── model/
│   ├── model_init.py         # Initialisation du modèle et fonctions RAG
│   ├── constitution.json     # Données structurées de la Constitution
│   └── constitution_embeddings_Multilingual.npy  # Embeddings pré-calculés
├── static/
│   └── style.css             # Styles CSS de l'application
├── templates/
│   └── index.html            # Template pour l'interface utilisateur
└── requirements.txt          # Dépendances du projet


## 📖 Utilisation

1. Ouvrez l'application dans votre navigateur
2. Posez une question sur la Constitution marocaine dans le champ de texte
3. Recevez une réponse générée à partir des articles pertinents de la Constitution

## 🧪 Exemple de questions

- "Quels sont les pouvoirs du Roi selon la Constitution marocaine ?"
- "Comment est organisé le pouvoir judiciaire au Maroc ?"
- "Quels sont les droits fondamentaux garantis par la Constitution ?"
- "Comment peut-on modifier la Constitution ?"

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## ✉ Contact

Pour toute question ou suggestion, veuillez ouvrir une issue sur GitHub.

---

Développé avec ❤ pour le Royaume du Maroc
