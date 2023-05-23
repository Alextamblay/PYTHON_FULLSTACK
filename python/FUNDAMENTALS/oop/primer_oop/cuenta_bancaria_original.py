class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance): 
    # tu código aquí (recuerda, los atributos de instancia van aquí)
    # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
        self.name = "name"
        self.amount = 0

    def hacer_depósito(self, amount):
    # tu código aquí
        self.amount += amount
        return self

    def hacer_retiro(self, amount):
    # tu código aquí
        self.amount -= amount
        return self

    def mostrar_info_cuenta(self):
    # tu código aquí
        print(f": {self.name},{self.amount}")
        return self

    def generar_interés(self):
    # tu código aquí
        pass

cuenta_1 = CuentaBancaria("cuenta1")
cuenta_2 = CuentaBancaria("cuenta2")

cuenta_1.hacer_depósito(100).hacer_depósito(200).hacer_depósito(50).hacer_retiro(45)

cuenta_2.hacer_depósito(1000).hacer_depósito(1000).hacer_retiro(500).hacer_retiro(300).hacer_retiro(10).hacer_retiro(8)