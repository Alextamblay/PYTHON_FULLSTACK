class mascota():
    def __init__(self, name, tipo, golosina, noise):
        self.name = name
        self.tipo = tipo
        self.golosina = golosina
        self.salud = 100
        self.energia = 100
        self.noise = noise

    def dormir():
        self.energy += 25
        return self
    
    def comer():
        self.energy += 5
        self.health += 10
        return self
    
    def jugar():
        self.health += 5
        self.energy -= 15
        return self

    def ruido():
        pass