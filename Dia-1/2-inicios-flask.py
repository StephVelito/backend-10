from flask import Flask 

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'

app.run(debug=True)
