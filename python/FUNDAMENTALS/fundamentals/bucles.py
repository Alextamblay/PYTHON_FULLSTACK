'''for x in range(0, 10, 2):
    print(x)'''

'''for x in 'Hello':
    #print(x)'''

'''mi_lista = ["abc", 123, "xyz"]
#for i in range(0, len(mi_lista)):
    #print(i, mi_lista[i])'''
#salida: 0 abc, 1 123, 2 xyz
    
#O 
    
'''for v in mi_lista:
    print(v)
salida: abc, 123, xyz'''

'''perro = ('martillo','bomba','chiporro','ganado')
for data in perro:
    print(data)''''''

#mi_dicc = { "nombre": "Noelle", "lenguaje": "Python" }
#for k in mi_dicc:
    #print(k)'''
# salida: nombre, lenguaje

'''mi_dicc = { "name": "Noelle", "languaje": "Python" }
for k in mi_dicc:
    print(mi_dicc[k])'''

# salida: Noelle, Python

'''capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}'''
# otra forma de iterar a través de las claves
'''for key in capitales.keys():
    print(key)'''
# salida: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# para iterar a través de los valores
'''for val in capitales.values():
    print(val)'''
# salida: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# para iterar a través de las claves y valores
'''for key, val in capitales.items():
    print(key, " = ", val)'''
# salida: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

'''count = 0
while count <= 5:
    print("looping - ", count)
    count += 1'''

'''y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Sentencia else final")'''

'''for val in "cadena":
    if val == "e":
        continue
    print(val)'''
# salida: c, a, d, n, a
# nota: no hay e en el resultado, pero el bucle continuó hasta después de la e

'''y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# solo se ejecuta en una salida limpia del bucle while (es decir, no un break)
    print("sentencia else final")'''
# salida: 3, 2, 1

def di_hola(nombre):
    print("Hola, " + nombre)
    #return "hole "+ nombre

val = di_hola('Michael')
print(val)


def di_hola(nombre):
    return "Hola " + nombre
saludo = di_hola("Michael") # el valor devuelto por la función di_hola se asigna a la variable 'saludo'
print(saludo) # esto dará como resultado 'Hola Michael'







