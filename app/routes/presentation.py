from app import app
from flask import render_template

@app.route('/hello_world/')
def hello_world():
    return 'Hello World !'


@app.route('/')
def index():
    title = 'Présentation Flask'
    to_see = ['jinja2', 'variable', 'filtre', 'condition', 'boucles']
    return render_template('index.html', title=title, to_see=to_see)
