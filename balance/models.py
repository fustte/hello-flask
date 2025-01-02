import csv
from datetime import date

from . import RUTA_FICHERO


class Movimiento:

    def __init__(self, dict_mov):
        self.errores = []

        fecha = dict_mov.get('fecha', '')
        concepto = dict_mov.get('concepto', 'Gastos varios')
        tipo = dict_mov.get('tipo', 'G')
        cantidad = dict_mov.get('cantidad', 0)

        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una fecha ISO 8601 válida'
            self.errores.append(mensaje)
        except TypeError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una cadena'
            self.errores.append(mensaje)
        except:
            self.fecha = None
            mensaje = f'Error desconocido con la fecha'
            self.errores.append(mensaje)

        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        try:
            self.leer_desde_archivo()
        except:
            self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(fila)
                self.movimientos.append(movimiento)

    def guardar(self):
        with open(RUTA_FICHERO, 'w') as fichero:
            # cabeceras = ['fecha', 'concepto', 'ingreso_gasto', 'cantidad']
            # writer = csv.writer(fichero)
            # writer.writerow(cabeceras)

            cabeceras = list(self.movimientos[0].__dict__.keys())
            cabeceras.remove('errores')

            writer = csv.DictWriter(fichero, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                mov_dict.pop('errores')
                writer.writerow(mov_dict)

    def agregar(self, movimiento):
        """
        Agrega un movimiento a la lista y actualiza el archivo CSV.
        """

        if not isinstance(movimiento, Movimiento):
            raise TypeError(
                'Solo puedes agregar datos usando la clase Movimiento')

        self.movimientos.append(movimiento)
        self.guardar()

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
