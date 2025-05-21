nombre = input("Hola, confío te encuentres bien, para iniciar escribe tu nombre y presiona enter:  ")
print ("Hola " + nombre + ". Para continuar ingresa dos números: ")

num_1 = int(input("ingresa el primer número: "))
num_2 = int(input("ingresa el segundo número: "))

suma = num_1 + num_2

print(str(num_1)+ "+" + str(num_2) + "=" + str(suma) )

resta = num_1-num_2

print(str(num_1) + "-" + str(num_2) + "=" + str(resta) )

multi= num_1 * num_2

print(str(num_1) + "*" + str(num_2) + "=" + str(multi) )



try:
    divi = num_1/num_2
    print(str(num_1) + "/" + str(num_2) + "=" + str(divi) )
except:
    print("Recuerda que la división por cero no está definida")

#Imprime solo la parte entera
try:
    divi = num_1//num_2
    print(str(num_1) + "/" + str(num_2) + "=" + str(divi) )
except:
    print("Recuerda que la división por cero no está definida")



try:
    modulo =num_1 % num_2
    print(str(num_1) + "%" + str(num_2) + "=" + str(modulo) )
except:
    print ("Recuerde que el modulo de un número y cero no está definido ")




