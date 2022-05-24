from re import S
import pymongo
import pandas as pd
from bson.objectid import ObjectId

from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con['sistema_escolares']

datos_alumno = {
    'nombre': 'Gerardo',
    'apellido': 'Ceseñas',
    'carrera': 'Desarrollo y Gestión de Software'
}

datos_materia = [
    {
        'nombre': 'Administración de Base de Datos'
    },
    {
        'nombre': 'Desarrollo Web Profesional'
    }
]

datos_calificaciones = [
    {
        'alumno_id': ObjectId('6226755dae9bf321f4659650'),
        'materia_id': ObjectId('622675a0348c08fb3cae7ccc'),
        'calificacion': 100
    },
    {
        'alumno_id': ObjectId('6226755dae9bf321f4659650'),
        'materia_id': ObjectId('622675a0348c08fb3cae7ccd'),
        'calificacion': 100
    }
]

datos_kardex = [
    {
        'alumno_id': ObjectId('6226755dae9bf321f4659650'),
        'promedio': 100
    }
]


def FunctionInsert(coleccion, datos):
    collection = db[coleccion]
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)

def functionUpdateCalificacion(calificacion_anterior, calificacion, alumno_id):
    collection = db['calificaciones']
    kardex = db['kardex']

    alumno_id = {
        'alumno_id': alumno_id
    }

    calif_anterior = {
        'calificacion': calificacion_anterior
    }

    calif_nueva = {
        '$set': {
            'calificacion': calificacion
        }
    }

    collection.update_one(calif_anterior, calif_nueva)
    resultados = list(kardex.find(alumno_id, {"_id": 1, "promedio": 1}))

    califs = list(collection.find())
    suma = 0
    if califs:
        for elemento in califs:
            suma += elemento["calificacion"]
            print(suma)

        promedio_nuevo = {
              '$set': {
                  'promedio': suma / 2
              }
        }
        promedio = list(kardex.find(alumno_id, {"_id": 1, "promedio": 1}))
        if (promedio):
            for elemento in promedio: 
                prom = elemento["promedio"]
            kardex.update_one({'promedio': prom}, promedio_nuevo)

def ExportData(collection, filename, format):
    data = list(collection.find())
    df = pd.DataFrame(data)
    if (format == 'csv'):
        df.to_csv(filename + '.csv', index = False)
        print('El archivo ha sido exportado en formato CSV')
    elif (format == 'xlsx'):
        df.to_excel(filename + '.xlsx', index = False)
        print('El archivo ha sido exportado en formato XLSX')
    else:
        print('Formato incorrecto, intenta de nuevo')

ExportData(db['kardex'], 'kardex', 'csv')

# functionUpdateCalificacion(80, 100, ObjectId('6226755dae9bf321f4659650'))
