from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def do_login():
    pass

app.run()