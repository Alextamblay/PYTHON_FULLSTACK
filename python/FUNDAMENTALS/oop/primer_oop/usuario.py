'''class usuario:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

usuario()
guido = usuario()
monty = usuario()
#accediendo a los atributos de la instancia
print(guido.name)
print(monty.name)'''

'''class Usuario: # declarando un atributo de clase
    nombre_banco = "Dojo Credit Union"
    bank_name = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0'''

'''guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.nombre_banco) # salida: Dojo Credit Union 
print(monty.bank_name) # salida: Primer Dojo Nacional'''

class Usuario: # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional" # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
carlita = Usuario ("carlita T", "carlita@python.com")
benjita = Usuario ("benjita celis", "benjita@python.com")
alecita = Usuario ("alecita t", "alecita@python.com")
catita = Usuario ("catita R", "catita@python.com")
david = Usuario ("david A", "david@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(carlita.name) # salida carlita T
print(benjita.name) # salida benjita celis
print(alecita.name) # salida alecita t
print(catita.name)  # salida catita R
print(david.name)   # salida david A
