from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en string 
  
  @app.route('/decrypt', methods=['GET'])
def decryptage():
    valeur = request.args.get('valeur')
    if not valeur:
        return "Erreur : aucune valeur à décrypter fournie", 400
    try:
        decrypted_bytes = f.decrypt(valeur.encode())  # Décryptage
        return f"Valeur décryptée : {decrypted_bytes.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}", 400
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
