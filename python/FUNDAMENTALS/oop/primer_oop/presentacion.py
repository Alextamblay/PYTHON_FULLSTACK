class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):
    	self.balance_cuenta += amount

