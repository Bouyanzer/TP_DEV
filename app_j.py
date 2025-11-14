from flask import Flask, request, jsonify

app = Flask(__name__)

etudiants = [
    {"id": 1, "nom": "Youcef", "age": 21},
    {"id": 2, "nom": "Guerif", "age": 109}
]


@app.route('/')
def accueil():
    return "Bienvenue"


@app.route('/etudiants', methods=['GET'])
def liste_etudiants():
    return jsonify(etudiants)


@app.route('/etudiants', methods=['POST'])
def ajouter_etudiant():
    nouveau = request.get_json()
    nouveau["id"] = len(etudiants) + 1
    etudiants.append(nouveau)
    return jsonify(nouveau), 201


@app.route('/etudiants/<int:identifiant>', methods=['GET'])
def obtenir_etudiant(identifiant):
    etudiant = next((e for e in etudiants if e["id"] == identifiant), None)
    if etudiant:
        return jsonify(etudiant)
    return jsonify({"erreur": "introuvable"}), 404


@app.route('/etudiants/<int:identifiant>', methods=['PUT'])
def modifier_etudiant(identifiant):
    etudiant = next((e for e in etudiants if e["id"] == identifiant), None)
    if not etudiant:
        return jsonify({"erreur": "introuvable"}), 404

    donnees = request.get_json()
    etudiant.update(donnees)
    return jsonify(etudiant)


@app.route('/etudiants/<int:identifiant>', methods=['DELETE'])
def supprimer_etudiant(identifiant):
    for i, e in enumerate(etudiants):
        if e["id"] == identifiant:
            del etudiants[i]
            return jsonify({"supprime": True})
    return jsonify({"erreur": "introuvable"}), 404


if __name__ == '__main__':
    app.run(debug=True)
