usu= input("Usuario: ")
contra= input("contraseña: ")

while usu != ("admin"):
     usu= input("Usuario incorrecto, inténtelo de nuevo: ")

while contra != ("0987"):
     contra= input("Contraseña equivocada, prueba otra vez ->")

if contra == ("0987"):
    print("¡Admitido!")