def calculo():
    numero=float(input("Dime un numero::: "))
    res=numero%2
    if res==0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

pregunta="S"
while pregunta=="S" or pregunta=="s":
    calculo()
    pregunta=str(input("¿Quieres continuar (S/N)? "))
