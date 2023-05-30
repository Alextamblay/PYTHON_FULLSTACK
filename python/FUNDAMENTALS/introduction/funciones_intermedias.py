'''x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Cambia el valor 10 en x a 15
x[1][0] = 15

# Cambia el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'

# En el directorio_deportes, cambia "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés'

# Cambia el valor 20 en z a 30
z[0]['y'] = 30

# Imprime los resultados después de los cambios
print(x)
print(estudiantes)
print(directorio_deportes)
print(z)'''

'''def iterateDictionary(some_list):
    for diccionario in some_list:
        output = ""
        for clave, valor in diccionario.items():
            output += f"{clave} - {valor}, "
        print(output[:-2])  # Elimina la coma y el espacio extra al final

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)'''

'''def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
print()
iterateDictionary2('last_name', estudiantes)'''

