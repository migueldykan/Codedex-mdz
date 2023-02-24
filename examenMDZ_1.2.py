"""Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente. 
Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día. (Haz dos versiones:
 una sin utilizar listas y otra con listas)"""

num= int(input( "Dame un número del 1 al 7: "))

if num == 1:
    print("El días de la semana correspondiente a este número es el Lunes")

    if num == 2:
    print("El días de la semana correspondiente a este número es el Martes")

    if num == 3:
    print("El días de la semana correspondiente a este número es el Miércoles")

    if num == 4:
    print("El días de la semana correspondiente a este número es el Jueves")

    if num == 5:
    print("El días de la semana correspondiente a este número es el Viernes")

    if num == 6:
    print("El días de la semana correspondiente a este número es el Sábado")

    if num == 7:
    print("El días de la semana correspondiente a este número es el Domingo")

    else :
    print("Error, tiene que ser un número del 1 al 7")
    num=int(input("Pon un número del 1 al 7: "))
