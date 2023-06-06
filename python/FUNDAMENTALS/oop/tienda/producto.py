class Producto():
    def __init__(self, name, precio, categoria):
        self.name = name
        self.precio = precio
        self.categoria = categoria 

    def actualizar_precio(self, cambio_porcentaje, está_elevado): 
        if está_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def Print_info(self):
        print(f"El nombre del producto es {self.name} La categoria es {self.categoria} El precio del producto es {self.precio}")


