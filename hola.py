from flask import Flask

"""
En la terminal ejecutar: flask --app hola run

En la terninal          : flask --app hola run --debug run

export FLASK_APP=hola

grep FLASK

"""



app = Flask('app-hola-flask')

@app.route('/')
def hola():
    return 'Hola, Flask!'

@app.route('/adios')
def adios():
    return 'Adios, Flask!'

@app.route('/nueva')
def cualquier_nombre():
    return 'Que pasa loco!'
