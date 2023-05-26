def valores_list255():
    list=[]
    for x in range (1,256):
        list.append(x)
    return list

variable = valores_list255()
print(variable)

def sumanumeros(lista):
    suma = sum(lista)
    return suma

variable2 = sumanumeros(([15,5,15,10]))
print (f"el total de la suma es = {variable2}")


def promedio_dojo (lista):
    promedio = sum(lista)/len(lista)
    return promedio

variable3 = promedio_dojo(({3,5,6}))
print (f"el promedio de las notas es = {variable3}")
