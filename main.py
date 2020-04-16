from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def do_login():
    return f"Bienvenido {request.form['username']}. Tu contraseña es {request.form['password']}"

app.run()