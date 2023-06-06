
from tienda import Tienda
from producto import Producto

def menu ():  
        print(" ________Menú Tienda________")
        print("|1.Registran Nuevo producto |")
        print("|2.Registrar Venta producto |")
        print("|3.Listar Productos         |")
        print("|4.Salir                    |")
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



        elif opcion == 2:
            tienda.vender_producto()

        elif opcion == 3:
            tienda.listar_productos()

        elif opcion == 4:
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()

