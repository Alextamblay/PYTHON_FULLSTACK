
from tienda import Tienda
from producto import Producto

def menu ():  
        print(" ________Menú Tienda________")
        print("|1.Registran Nuevo producto |")
        print("|2.Registrar Venta producto |")
        print("|3.Listar Productos         |")
        print("|4.Modificar producto       |")
        print("|5.Salir                    |")
        print("|___________________________|")
def main():
    tienda = Tienda("tiendita kitty")

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            nombre = (input("ingrese el nombre del producto "))
            precio = (input("ingrese el precio del producto "))
            categoria = (input("ingrese la categoria "))
            nuevo_producto = Producto(nombre, precio, categoria)
            tienda.agregar_producto(nuevo_producto)

            print("------------------------")
            print("-----Producto Listo-----")
            print("------------------------")

        if opcion == 2:
            tienda.vender_producto()

        if opcion == 3:
            tienda.listar_productos()

        if opcion == 4:
            nombre = (input("ingrese el nombre del producto "))
            precio = (input("ingrese el precio del producto "))
            categoria = (input("ingrese la categoria "))
            producto_modificar = Producto(nombre, precio, categoria)
            tienda.actualizar_lista(producto_modificar)

            print("------------------------")
            print("-  Producto modificado -")
            print("------------------------")

        elif opcion == 5:
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()

