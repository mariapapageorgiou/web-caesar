from flask import Flask, request, render_template
from caesar import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# TO DO fix the form with the render_template method

@app.route("/", methods=['POST'])
def encrypt():
    user_sentence = str(request.form["text"])
    user_rotation = int(request.form["rot"])
    encrypted_message = rotate_string(user_sentence, user_rotation)
    return render_template('form.html', encrypted_message=encrypted_message)
     

@app.route("/")
def index():
    return render_template('form.html') #form.format("")

@app.route("/encrypted-message")
def encryption():    
    encrypted_message = request.args.get('user_sentence', 'user_rotation')
    return render_template('form.html', encrypted_message=encrypted_message)

app.run()

#  username = request.args.get('username')
#     return render_template('welcome_form.html', username=username)