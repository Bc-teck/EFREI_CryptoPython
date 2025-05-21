from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<key>/<valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Utilisation de la clé fournie par l'utilisateur
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Chiffrement
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en string
    except Exception as e:
        return f"Erreur lors du cryptage : {str(e)}", 400

@app.route('/decrypt/<key>/<token>')
def decryptage(key, token):
    try:
        f = Fernet(key.encode())  # Utilisation de la clé fournie par l'utilisateur
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Déchiffrement
        return f"Valeur décryptée : {valeur.decode()}"  # Retourne le texte d'origine
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
