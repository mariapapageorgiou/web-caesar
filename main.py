from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <form method="post">
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
        Rotate by: 
        <input type="text" name="rot" value="0">
        <textarea rows="4" cols="50" name="text">{0}</textarea>
        <input type="submit" value="Submit">
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    user_sentence = str(request.form["text"])
    user_rotation = int(request.form["rot"])
    encrypted_message = rotate_string(user_sentence, user_rotation)
    return form.format(encrypted_message)
     

@app.route("/")
def index():
    return form.format("")

app.run()