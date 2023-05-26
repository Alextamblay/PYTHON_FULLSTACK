class Mascota():
    def __init__(self, name, tipo, golosina):
        self.name = name
        self.tipo = tipo
        self.golosina = golosina
        self.salud = 100
        self.energia = 100

    def dormir(self):
        self.energia += 25
        return self
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self
    
    def jugar(self):
        self.salud += 5
        self.energia -= 15
        return self

    def ruido(self):
        print(self.ruido)

    def Mostrar_energia(self):
        print(f"La energia de Charlotte es: {self.energia}")
        return self
    def Mostrar_salud(self):
        print (f"La salud de Charlotte es: {self.salud}")
        return self