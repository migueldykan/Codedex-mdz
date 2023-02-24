"""Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente. 
Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día. (Haz dos versiones:
 una sin utilizar listas y otra con listas)"""

dias= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

num=int(input("Introduce un número del 1 al 7: "))

#Ahora utilizamos el while para que mientras nos dé un número fuera del rango del 1 al 7 
#le dé error y tenga que volver a poner otro número ahora sí dentro del rango.

while num <1 or num >7:
    print("Error, este número no puede ser dado. ")
    num=int(input("Vuelva a introducirme un número del 1 al 7: "))

if num >=1 or num<= 7:
    print("El día de la semana correspondiente a este número es", dias[num-1])
