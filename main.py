from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def do_login():
    return f"Bienvenido {request.form['username']}. Tu contraseña es {request.form['password']}"

@app.route('/login', methods=['GET'])
def login_form():
    return f"""<html>
    <body>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Usuario" required>
            <input type="password" name="password" placeholder="Contraseña" required>
            <input type="submit" value="Ingresar">
        </form>
    </body>
    </html>"""

import cristian
@app.route('/cristian', methods=['GET'])
def do_cristian():
    return cristian.nombre()

app.run()
