# dictionary = {
#     'nombre': 'Gerardo',
#     'edad': 21
# }

# dictionary.update({'apellido': 'Ceseñas'})
# dictionary.pop('edad')
# print(dictionary['nombre'])


# texto_completo = 'Administración de base de datos'
# search = 'Administracións'

# if search in texto_completo:
#     print('Sí existe')
# else:
#     print('No existe')

# lista_completa = ['Admon', 'Bases', 'Datos', 2, 'Unidad']
# search = 'Admin'

# if search in lista_completa:
#     print('Sí existe')
# else:
#     print('No existe')

# def Buscar(info_completa, search):
#     if search in info_completa:
#         print('Sí existe')
#     else:
#         print('No existe')

# Buscar(lista_completa, 'Admjon')

# Gerardo Ceseñas Rivera 8A DGS
lista_completa = ['Admon', 'Bases', 'Datos', 2, 'Unidad']
diccionarios = [{
    'nombre': 'Gerardo',
    'edad': '21'
},
    {
    'nombre': 'Ceseñas',
    'edad': '21'
}]

def Recorrer(lista_dicc):
    for elemento in lista_dicc:
        print(elemento)

Recorrer(diccionarios)


#Creaer una función para utilizar un for y que reaccione a una lista de diccionarios y otra de strings
