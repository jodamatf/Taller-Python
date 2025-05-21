import time


def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    try:
         return a/b
    except:
        return print("Recuerde que la división por cero no está definida")

def modulo (c,d):
    try:
        return c%d
    except:
        return print("Recuerde que 'a' modulo cero no está definido. Elija un valor diferente de cero")

def menu_cal():
    print("Calculadora básica")
    print("1. Suma")
    print("2. resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Modulo de un número (a)")
    print("6. Salir\n")


def select():

    # menu_cal() call removed to avoid redundancy

    opcion=""
    
    while opcion!="6":
        menu_cal()
        opcion= input("Digite la opción de su preferencia: \n")
       
        
        if opcion == "1":
            print("Seleccionaste la suma. Cargando...")
            time.sleep(1)
            a = float(input("Ingrese el valor de (a): "))
            b = float(input("Ingrese el valor de (b): "))
            print(suma(a, b))
        elif opcion == "2":
            print("Seleccionaste la resta. Cargando...")
            time.sleep(1)
            a = float(input("Ingrese el valor de (a): "))
            b = float(input("Ingrese el valor de (b): "))
            print(resta(a, b))
        elif opcion == "3":
            print("Seleccionaste la multiplicación. Cargando...")
            time.sleep(1)
            a = float(input("Ingrese el valor de (a): "))
            b = float(input("Ingrese el valor de (b): "))
            print(multi(a, b))
        elif opcion == "4":
            print("Seleccionaste la división. Cargando...")
            time.sleep(1)
            a = float(input("Ingrese el valor de (a): "))
            b = float(input("Ingrese el valor de (b): "))
            print(div(a, b))
        elif opcion == "5":
            print("Seleccionaste el modulo. Cargando...")
            time.sleep(1)
            a = float(input("Ingrese el valor de (a): "))
            b = float(input("Ingrese el valor de (b): "))
            print(f"a % b es: {modulo(a, b)}")
        elif opcion == "6":
            print("Saliendo del programa...")
            time.sleep(2)
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")


select()