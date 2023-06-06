
from tienda import Tienda
from producto import Producto

def menu ():  
        print("---Tienda---")
        print("1.")
        print("2.")
        print("3.")
        print("4.Listar Registros")
        print("5.")
        
def main():

    while True:


        opcion = int(input("Seleccione una opción: "))
        print(type(opcion))
        if opcion == 1:
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.agregar_usuario(nombre)
            print("Usuario agregado exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_entrada(nombre)
            print("Registro de entrada realizado.")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_salida(nombre)
            print("Registro de salida realizado.")
        elif opcion == 4:
            sistema_asistencia.listar_registros()
        elif opcion == 5:
            break
        

if __name__ == "__main__":
    main()

#producto1 = Producto("confort",3000, "higiene")
#producto1.Print_info()