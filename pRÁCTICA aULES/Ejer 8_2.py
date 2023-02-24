"""8.2 Pide al usuario 10 números y luego muestra los que son pares"""

num=[]
for n in range(0,10):
    num.append(int(input("Dame un número: ")))
print("")
print("Los números pares son:")
for n in num:
    if (n%2 == 0):
        print(n)