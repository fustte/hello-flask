from flask import redirect, render_template, request, url_for

from .models import ListaMovimientos, Movimiento
from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    print('-----', lista)
    return render_template('inicio.html', movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    if request.method == 'GET':
        return render_template('nuevo.html')
    if request.method == 'POST':

        lista = ListaMovimientos()
        mov = Movimiento(request.form)
        if mov.has_errors:
            return f'ERROR: {mov.errores}'
        lista.agregar(mov)

        return redirect(url_for('home'))


@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'


@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return 'Borrar movimiento'
