class Producto:
    def __init__(self, nombre,cantidad, precio):
        #Constructor de la clase producto

        self.nombre=nombre
        self.cantidad=cantidad
        self.precio=precio

def mostrar_menu():
    #Función para mostrar el menú de opciones
    print("Sistema de Inventario")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Salir")

inventario=[]

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "0":
        # Salir del programa
        print("Saliendo del programa.")
        break

    if opcion == "1":
        # Agregar un nuevo producto
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            precio = float(input("Ingresa el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado.")
        except ValueError:
            # Manejar errores de entrada no válida
            print("Error: Entrada no válida.")

    elif opcion == "2":
        # Mostrar todos los productos
        for p in inventario:
            print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    elif opcion == "3":
        # Buscar un producto por nombre
        nombre = input("Ingresa el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")                
    elif opcion == "4":
        # Actualizar la cantidad de un producto
        nombre = input("Ingresa el nombre del producto a actualizar: ")
        try:
            nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad = nueva_cantidad
                    print("Cantidad actualizada.")
                    break
        except ValueError:
            # Manejar errores de entrada no válida
            print("Error: Entrada no válida.")

    elif opcion == "5":
        # Eliminar un producto por nombre
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado.")
                break

    else:
        # Manejar opción no válida
        print("Opción no válida. Inténtalo de nuevo.")

