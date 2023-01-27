yuan=int(input("¿Cuánto te queda en Yuanes?"))
yen=int(input("¿Cuánto te queda en Yenes?"))
won=int(input("¿Cuánto te queda en Wones?"))

euryuan = yuan * 0.14
euryen = yen * 0.0072
eurwon= won * 0.00035

euro = euryuan + euryen + eurwon
print(euro)