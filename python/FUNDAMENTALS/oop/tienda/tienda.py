class Tienda:
    def __init__(self, name, ):
        self.name = name
        self.lista = []
    def agregar_producto(self, nuevo_producto):
        self.lista.append(nuevo_producto)
        return self

    def vender_producto(self, id): 
        for x in self.lista:
            if x.name == id:
                x.remove
            else:
                print ("Producto no existe" )
        return self

    def listar_productos(self): 
        for x in self.lista:
            x.Print_info()
        return self

    def inflación(self, porcentaje_aumento):
        pass

    def hacer_liquidación(self, category, porcentaje_descuento):
        pass
    

