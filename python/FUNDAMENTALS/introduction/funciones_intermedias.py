1.-"Actualizar valores en diccionarios y listas"

x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

estudiantes = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Messi', 'Ronaldo', 'Rooney']}
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)

2.-"Iterar a través de una lista de diccionarios"

def iterateDictionary(some_list):
    for diccionario in some_list:
        for clave, valor in diccionario.items():
            print(clave + " - " + valor)
        print()


estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(estudiantes)


3.-"Obtener valores de una lista de diccionarios"

def iterateDictionary2(key_name, some_list):
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
iterateDictionary2('last_name', estudiantes)

4.-"Iterar a través de un diccionarios con valores de lista"

def printInfo(some_dict):
    for clave, valores in some_dict.items():
        print(len(valores), clave.upper())
        for valor in valores:
            print(valor)
        print()

dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)




