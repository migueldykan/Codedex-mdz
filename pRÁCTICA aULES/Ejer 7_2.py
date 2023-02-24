"""7.2 Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de
multiplicar de ese número( Ejemplo: “5 x 1 = 5” hasta “5 x 10 = 50”)"""

num=int(input("Dame un número"))
for i in range (11):
    print(num,"x",i,"=",(num*i))