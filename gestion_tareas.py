class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE TAREAS =====")
    print("1. Añadir nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de una tarea")
    print("5. Actualizar descripción de una tarea")
    print("6. Eliminar tarea")
    print("7. Filtrar tareas por estado")
    print("8. Salir")
    return input("Seleccione una opción (1-8): ")

def agregar_tarea(lista_tareas):
    print("\n----- AÑADIR NUEVA TAREA -----")
    try:
        titulo = input("Ingrese el título de la tarea: ")
        # Verifica si ya existe una tarea con ese título
        if any(tarea.titulo.lower() == titulo.lower() for tarea in lista_tareas):
            print("¡Error! Ya existe una tarea con ese título.")
            return
        
        descripcion = input("Ingrese la descripción de la tarea: ")
        nueva_tarea = Tarea(titulo, descripcion)
        lista_tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' añadida correctamente.")
    except Exception as e:
        print(f"Error al añadir la tarea: {e}")

def mostrar_tareas(lista_tareas):
    print("\n----- LISTA DE TAREAS -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    for i, tarea in enumerate(lista_tareas, 1):
        print(f"{i}. Título: {tarea.titulo}")
        print(f"   Descripción: {tarea.descripcion}")
        print(f"   Estado: {tarea.estado}")
        print("   ------------------------")

def buscar_tarea(lista_tareas):
    print("\n----- BUSCAR TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a buscar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():  
                print(f"\nTítulo: {tarea.titulo}")
                print(f"Descripción: {tarea.descripcion}")
                print(f"Estado: {tarea.estado}")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al buscar la tarea: {e}")

def actualizar_estado(lista_tareas):
    print("\n----- ACTUALIZAR ESTADO DE TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Estado actual: {tarea.estado}")
                nuevo_estado = input("Ingrese el nuevo estado (pendiente/completada): ").lower()
                
                if nuevo_estado in ["pendiente", "completada"]:
                    tarea.estado = nuevo_estado
                    print(f"Estado de la tarea '{tarea.titulo}' actualizado a '{nuevo_estado}'.")
                else:
                    print("Estado no válido. Use 'pendiente' o 'completada'.")
                
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al actualizar el estado: {e}")

def actualizar_descripcion(lista_tareas):
    print("\n----- ACTUALIZAR DESCRIPCIÓN DE TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Descripción actual: {tarea.descripcion}")
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                tarea.descripcion = nueva_descripcion
                print(f"Descripción de la tarea '{tarea.titulo}' actualizada correctamente.")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al actualizar la descripción: {e}")

def eliminar_tarea(lista_tareas):
    print("\n----- ELIMINAR TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        encontrada = False
        
        for i, tarea in enumerate(lista_tareas):
            if tarea.titulo.lower() == titulo.lower():
                confirmacion = input(f"¿Está seguro de eliminar la tarea '{tarea.titulo}'? (s/n): ").lower()
                if confirmacion == 's':
                    del lista_tareas[i]
                    print(f"Tarea '{titulo}' eliminada correctamente.")
                else:
                    print("Operación cancelada.")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")

def filtrar_por_estado(lista_tareas):
    print("\n----- FILTRAR TAREAS POR ESTADO -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        estado = input("Ingrese el estado a filtrar (pendiente/completada): ").lower()
        
        if estado not in ["pendiente", "completada"]:
            print("Estado no válido. Use 'pendiente' o 'completada'.")
            return
        
        tareas_filtradas = [tarea for tarea in lista_tareas if tarea.estado.lower() == estado]
        
        if not tareas_filtradas:
            print(f"No hay tareas con estado '{estado}'.")
            return
        
        print(f"\nTareas con estado '{estado}':")
        for i, tarea in enumerate(tareas_filtradas, 1):
            print(f"{i}. Título: {tarea.titulo}")
            print(f"   Descripción: {tarea.descripcion}")
            print(f"   ------------------------")
    except Exception as e:
        print(f"Error al filtrar tareas: {e}")

def main():
    lista_tareas = []
    
    print("¡Bienvenido al Sistema de Gestión de Tareas!")
    
    while True:
        opcion = mostrar_menu()
        
        try:
            if opcion == "1":
                agregar_tarea(lista_tareas)
            elif opcion == "2":
                mostrar_tareas(lista_tareas)
            elif opcion == "3":
                buscar_tarea(lista_tareas)
            elif opcion == "4":
                actualizar_estado(lista_tareas)
            elif opcion == "5":
                actualizar_descripcion(lista_tareas)
            elif opcion == "6":
                eliminar_tarea(lista_tareas)
            elif opcion == "7":
                filtrar_por_estado(lista_tareas)
            elif opcion == "8":
                print("\n¡Gracias por usar el Sistema de Gestión de Tareas!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
        except Exception as e:
            print(f"Error inesperado: {e}")

class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE TAREAS =====")
    print("1. Añadir nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de una tarea")
    print("5. Actualizar descripción de una tarea")
    print("6. Eliminar tarea")
    print("7. Filtrar tareas por estado")
    print("8. Salir")
    return input("Seleccione una opción (1-8): ")

def agregar_tarea(lista_tareas):
    print("\n----- AÑADIR NUEVA TAREA -----")
    try:
        titulo = input("Ingrese el título de la tarea: ")
        # Verificar si ya existe una tarea con ese título
        if any(tarea.titulo.lower() == titulo.lower() for tarea in lista_tareas):
            print("¡Error! Ya existe una tarea con ese título.")
            return
        
        descripcion = input("Ingrese la descripción de la tarea: ")
        nueva_tarea = Tarea(titulo, descripcion)
        lista_tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' añadida correctamente.")
    except Exception as e:
        print(f"Error al añadir la tarea: {e}")

def mostrar_tareas(lista_tareas):
    print("\n----- LISTA DE TAREAS -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    for i, tarea in enumerate(lista_tareas, 1):
        print(f"{i}. Título: {tarea.titulo}")
        print(f"   Descripción: {tarea.descripcion}")
        print(f"   Estado: {tarea.estado}")
        print("   ------------------------")

def buscar_tarea(lista_tareas):
    print("\n----- BUSCAR TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a buscar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():  
                print(f"\nTítulo: {tarea.titulo}")
                print(f"Descripción: {tarea.descripcion}")
                print(f"Estado: {tarea.estado}")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al buscar la tarea: {e}")

def actualizar_estado(lista_tareas):
    print("\n----- ACTUALIZAR ESTADO DE TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Estado actual: {tarea.estado}")
                nuevo_estado = input("Ingrese el nuevo estado (pendiente/completada): ").lower()
                
                if nuevo_estado in ["pendiente", "completada"]:
                    tarea.estado = nuevo_estado
                    print(f"Estado de la tarea '{tarea.titulo}' actualizado a '{nuevo_estado}'.")
                else:
                    print("Estado no válido. Use 'pendiente' o 'completada'.")
                
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al actualizar el estado: {e}")

def actualizar_descripcion(lista_tareas):
    print("\n----- ACTUALIZAR DESCRIPCIÓN DE TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        encontrada = False
        
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Descripción actual: {tarea.descripcion}")
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                tarea.descripcion = nueva_descripcion
                print(f"Descripción de la tarea '{tarea.titulo}' actualizada correctamente.")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al actualizar la descripción: {e}")

def eliminar_tarea(lista_tareas):
    print("\n----- ELIMINAR TAREA -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        encontrada = False
        
        for i, tarea in enumerate(lista_tareas):
            if tarea.titulo.lower() == titulo.lower():
                confirmacion = input(f"¿Está seguro de eliminar la tarea '{tarea.titulo}'? (s/n): ").lower()
                if confirmacion == 's':
                    del lista_tareas[i]
                    print(f"Tarea '{titulo}' eliminada correctamente.")
                else:
                    print("Operación cancelada.")
                encontrada = True
                break
        
        if not encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")

def filtrar_por_estado(lista_tareas):
    print("\n----- FILTRAR TAREAS POR ESTADO -----")
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    
    try:
        estado = input("Ingrese el estado a filtrar (pendiente/completada): ").lower()
        
        if estado not in ["pendiente", "completada"]:
            print("Estado no válido. Use 'pendiente' o 'completada'.")
            return
        
        tareas_filtradas = [tarea for tarea in lista_tareas if tarea.estado.lower() == estado]
        
        if not tareas_filtradas:
            print(f"No hay tareas con estado '{estado}'.")
            return
        
        print(f"\nTareas con estado '{estado}':")
        for i, tarea in enumerate(tareas_filtradas, 1):
            print(f"{i}. Título: {tarea.titulo}")
            print(f"   Descripción: {tarea.descripcion}")
            print(f"   ------------------------")
    except Exception as e:
        print(f"Error al filtrar tareas: {e}")

def main():
    lista_tareas = []
    
    print("¡Bienvenido al Sistema de Gestión de Tareas!")
    
    while True:
        opcion = mostrar_menu()
        
        try:
            if opcion == "1":
                agregar_tarea(lista_tareas)
            elif opcion == "2":
                mostrar_tareas(lista_tareas)
            elif opcion == "3":
                buscar_tarea(lista_tareas)
            elif opcion == "4":
                actualizar_estado(lista_tareas)
            elif opcion == "5":
                actualizar_descripcion(lista_tareas)
            elif opcion == "6":
                eliminar_tarea(lista_tareas)
            elif opcion == "7":
                filtrar_por_estado(lista_tareas)
            elif opcion == "8":
                print("\n¡Gracias por usar el Sistema de Gestión de Tareas!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
        except Exception as e:
            print(f"Error inesperado: {e}")

main()