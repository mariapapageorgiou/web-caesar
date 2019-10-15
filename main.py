from flask import Flask, request, render_template
from caesar import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def encrypt():
    user_sentence = str(request.form["text"])
    user_rotation = int(request.form["rot"])
    encrypted_message = rotate_string(user_sentence, user_rotation)
    return render_template('form.html', encrypted_message=encrypted_message)

@app.route("/")
def index():
    return render_template('form.html') 

@app.route("/encrypted-message")
def encryption():    
    encrypted_message = request.args.get('user_sentence', 'user_rotation')
    return render_template('form.html', encrypted_message=encrypted_message)

app.run()