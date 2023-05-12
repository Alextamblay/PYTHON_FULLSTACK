class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f" Esta es el saldo de la cuenta User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


benjita = User("benjita")
catita = User("catita")
lucianito = User("lucianito")

benjita.make_deposit(100)
benjita.make_deposit(200)
benjita.make_deposit(50)
benjita.make_withdrawl(45)
benjita.display_user_balance()

catita.make_deposit(1000)
catita.make_deposit(1000)
catita.make_withdrawl(500)
catita.make_withdrawl(300)
catita.display_user_balance()

lucianito.make_deposit(1500)
lucianito.make_withdrawl(1000)
lucianito.make_withdrawl(5000)
lucianito.make_withdrawl(3000)
lucianito.display_user_balance()


catita.transfer_money(400, benjita)