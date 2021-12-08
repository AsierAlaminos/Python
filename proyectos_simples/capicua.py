def conversor(numero):
    reves=numero[::-1]
    if numero==reves:
        print(f"{numero} es capicua")
    else:
        print(f"{numero} no es capicua")


pregunta="S"
while pregunta=="S" or pregunta=="s":
    numero=str(input("Dime un número::: "))
    conversor(numero)
    pregunta=str(input("¿Quieres continuar (S/N)? "))
