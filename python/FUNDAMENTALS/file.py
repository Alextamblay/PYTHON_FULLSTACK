num1 = 42 #variable declaracion
num2 = 2.3 #decimal
boolean = True #boolean
string = 'Hello World' #cadenas
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo de tipo lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana') #tupla
print(type(fruit)) #print de var tipo tupla
print(pizza_toppings[1]) #print de var tipo arreglo
pizza_toppings.append('Mushrooms') #nos permite agregar
print(person['name']) #selecciona el contenido de la var name 
person['name'] = 'George' #modifica
person['eye_color'] = 'blue' #agregar un valor al diccionario
print(fruit[2]) #vamos a imprimir l a2 posicion de la tupla

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #elimina un valor
pizza_toppings.pop(1) #elimina un valor de una posicion de un arreglo

print(person)#imprime person
person.pop('eye_color')# elimina un valor de arreglo
print(person) #vuelve a imprimir person

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#
print_hello_x_or_ten_times(4)#


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)