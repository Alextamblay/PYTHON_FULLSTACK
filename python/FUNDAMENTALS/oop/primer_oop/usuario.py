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
print(monty.name)



class Usuario: # declarando un atributo de clase
    nombre_banco = "Dojo Credit Union"
    bank_name = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

guido = Usuario()
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
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

'''guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
xiaomi = Usuario ("xiaomi Pacheco", "carlita@python.com")
benjita = Usuario ("benjita Celis", "benjita@python.com")
alecita = Usuario ("alecita Tamblay", "alecita@python.com")
catita = Usuario ("catita Rivas", "catita@python.com")
davicito = Usuario ("davicito Astudillo", "david@python.com")

guido.hacer_depósito(100.000)
monty.hacer_depósito(230.000)
xiaomi.hacer_depósito(350.000)
benjita.hacer_depósito(100.000)
alecita.hacer_depósito(780.000)
catita.hacer_depósito(17.000)
davicito.hacer_depósito(40.000)


print(F"Mi nombre es {guido.name} y mi email es {guido.email} el valor de mi cuenta es {guido.balance_cuenta} ")	# salida: Guido van Rossum y el correo
print(F"Mi nombre es {monty.name} y mi email es {monty.email} el valor de mi cuenta es {monty.balance_cuenta}")	# salida: Monty Python y el correo
print(F"Mi nombre es {xiaomi.name} y mi email es {xiaomi.email} el valor de mi cuenta es {xiaomi.balance_cuenta}") # salida xiaomi P y el correo
print(F"Mi nombre es {benjita.name} y mi email es {benjita.email} el valor de mi cuenta es {benjita.balance_cuenta}") # salida benjita celis y el correo
print(F"Mi nombre es {alecita.name} y mi email es {alecita.email} el valor de mi cuenta es {alecita.balance_cuenta}") # salida alecita t y el correo
print(F"Mi nombre es {catita.name} y mi email es {catita.email} el valor de mi cuenta es {catita.balance_cuenta}")  # salida catita R y el correo
print(F"Mi nombre es {davicito.name} y mi email es {davicito.email} el valor de mi cuenta es {davicito.balance_cuenta}")   # salida davicito A y el correo'''

class CuentaBancaria: # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, int_rate,balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

# método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls,name):
        cls.nombre_banco = name
# método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
# utilizamos cls para referirnos a la clase 
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum
