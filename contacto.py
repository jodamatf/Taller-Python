class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestión de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    contactos = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo del programa.")
            break
        elif opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            contacto = Contacto(nombre, telefono)
            contactos.append(contacto)
            print("Contacto agregado")

        elif opcion == "2":
            if not contactos:
                print("No hay contactos")
            else:
                for c in contactos:
                    print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            encontrado = False
            for c in contactos:
                if c.nombre == nombre:
                    print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado")
        elif opcion == "4":
            nombre = input("Ingrese el nombre a eliminar: ")
            encontrado = False
            for c in contactos:
                if c.nombre == nombre:
                    contactos.remove(c)
                    print("Contacto eliminado")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado")
        else:
            print("Opción no válida. Inténtalo de nuevo")


main()