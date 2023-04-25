perro = ('Bruce', 'cocker spaniel', 19, False)
print(perro[0])		# salida: Bruce
perro[1] = 'dachshund'	# ERROR: no se puede modificar ('tuple' el objeto no es compatible con la asignación)

lista_vacía = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# salida: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# salida: ['Francis', 'Oliver'

dic_vacío = {}
new_person = {'name': 'John', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
new_person['name'] = 'Jack'	# actualiza si la llave existe, agrega un par clave-valor si no
new_person['hobbies'] = ['escalada', 'programación']
print(new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'peso: 160.2, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}
w = new_person.pop('peso')	# remueve la llave indicada y devuelve el valor
print(w)		# salida: 160.2
print(new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}        

print(type(2.63))		# salida: <class 'float'>
print(type(new_person))		# salida: <class 'dict'>
