"""8.3 Pide al usuario un número del 1 al 12 y escribe el número del mes
correspondiente (1 = enero, 2= febrero,..) usando un array"""

meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

num=int(input("Introduce un número del 1 al 12: "))

while num<1  or num> 12:
    print("syntax error")
    num=int(input("Vuelva a introducirme un número: "))
    
if num >=1 or num<= 12:
    print("El mes correspondiente es", meses[num-1])
