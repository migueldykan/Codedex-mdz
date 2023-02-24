"""7.3 Pide al usuario un número entero (por ejemplo, 58) y nos dé todos los
múltiplos de 7 que hay entre el número 1 y ese número (incluido)"""

num=int(input("Dame un número entero: "))

for n in range(0,num+1):
    if n%7 == 0:
        print("Todos los números que son multiplos del 7 entre el 1 y ese número son:",n)
