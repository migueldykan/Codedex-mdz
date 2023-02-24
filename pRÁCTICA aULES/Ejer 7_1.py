"""7.1 Crea un programa que pida al usuario que introduzca su nombre y un
número entero y escriba su nombre en pantalla tantas veces como indique ese
número entero."""

nom = input("Introduzca su nombre: ")
num = int(input("Introduzca un número entero: "))

for i in range(num):
    print(nom)


