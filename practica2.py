from crud import *
import datetime

buscar = { 'nombre': 'Amoxicilina' }
print(FunctionSelect('productos', buscar, 'all'))

def SaveLogs(table, action):
    current_time = datetime.datetime.now()
    data_log = {
        'action': action,
        'date': current_time,
        'tabla': table
    }
    FunctionInsert('log', data_log)

datos_producto = {
        'lote': '30a0552',
        'nombre': 'Betacetimetadol',
        'desc': 'Reduce la dependencia de la heroína cuando se administra correctamente',
        'precio': 1780,
        'departamento': 'Opioide',
        'receta': True,
        'stock': 20,
        'descuento': 0,
    }

# Gerardo Ceseñas Rivera 8A DGS
# La función "FunctionInsert" tiene encapsulada la función "SaveLogs", por lo que registra cuando y
# qué acción se hizo.
FunctionInsert('productos', datos_producto)
# SaveLogs('productos', 'insert')
# FunctionSelect('productos', {}, 'all')