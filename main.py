from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def do_login():
    pass

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

app.run()
