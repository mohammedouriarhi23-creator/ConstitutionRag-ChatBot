from flask import Flask, render_template, request, jsonify
from model.model_init import load_data_and_index, answer_question_rag_with_groq
import os
import traceback

app = Flask(__name__)

articles_info, index = load_data_and_index()
    
@app.route("/", methods=["GET"])
def index_route():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    if request.method == "POST":
        if articles_info is None or index is None:
            return jsonify({
                "error": "Les données n'ont pas été chargées correctement. Veuillez vérifier les fichiers de modèle."
            }), 500
            
        data = request.get_json()
        question = data.get("question", "")
        
        if not question:
            return jsonify({"error": "Question vide"}), 400
        
        try:    
            response, sources = answer_question_rag_with_groq(
                question, index, articles_info
            )
            
            return jsonify({
                "question": question,
                "response": response,
                "sources": "Constitution du Royaume du Maroc"
            })
        except Exception as e:
            print(f"Erreur lors du traitement de la question: {e}")
            print(traceback.format_exc())
            return jsonify({
                "error": "Une erreur est survenue lors du traitement de votre question."
            }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000',debug=True)
    