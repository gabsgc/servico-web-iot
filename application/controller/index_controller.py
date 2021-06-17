from application import app
from flask import jsonify, request

@app.route('/')
def index():
    return '<h1>Olá Mundo!</h1>'