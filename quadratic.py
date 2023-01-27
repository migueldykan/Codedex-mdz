a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

root1 = (( - b + (((b ** 2) - 4 * a * c) ** (0.5))) / (2*a))
root2 = (( - b - (((b ** 2) - 4 * a * c) ** (0.5))) / (2*a))

print (root1)
print (root2)