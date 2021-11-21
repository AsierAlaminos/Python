print("Hola, bienvenido a la calculadora.")
import os
operaciones=["S", "R", "M", "D", "E", "P", "s", "r", "m", "d", "e", "p", "Prueba"]
i=1
def suma(x, y):

    print("Resultado:", (x + y))

while True:
    #print(i)
    i=i+1
    print("S/s-Suma")
    print("R/r-Resta")
    print("M/m-Multiplicación")
    print("D/d-Division")
    print("E/e-Elevar a...")
    print("P/p-Porcentajes")
    operacion=input("¿Que quieres calcular:" )
    if operacion=="Prueba":
        print("1.-SUMA")
        x = int(input("Dime un numero:"))
        y = int(input("Dime otro:"))
        print(suma(x, y))
    if operacion in operaciones:
        print("")
    else:
        print("Fallo en la sintaxis")
#Suma
    if operacion=="S" or operacion=="s":
        print("1.-SUMA")
        suma1=int(input("Dime un numero:" ))
        suma2=int(input("Dime otro:" ))
        print("Resultado:", (suma1 + suma2))
#resta
    if operacion=="R" or operacion=="r":
        print("2.-RESTA")
        resta1=int(input("Dime un numero:" ))
        resta2=int(input("Dime otro:"))
        print("Resultado:", (resta1-resta2))
#multiplicación
    if operacion=="M" or operacion=="m":
        print("3.-MULTIPLICACION")
        multi1=int(input("Dime un numero:" ))
        multi2=int(input("Dime otro:" ))
        print("Resultado: ", (multi1*multi2))
#Division
    if operacion=="D" or operacion=="d":
        print("4.-DIVISION")
        division1=int(input("Dime un numero:" ))
        division2=int(input("Dime otro:" ))
        print("Resultado: ", (division1/division2))
#Elevar
    if operacion=="E" or operacion=="e":
        print("ELEVAR A...")
        elevado=int(input("Dime un numero:" ))
        elevador=int(input("¿A que numero lo quieres elevar?:"))
        print("Resultado: ", (elevado**elevador))
#Procentajesincrementar
    if operacion=="P" or operacion=="p":
        print("PORCENTAJES")
        total=int(input("Dime el porcentaje que quieres sacar:" ))
        parcial=int(input("De que numero:" ))
        print("Resultado: ", total*parcial/100 )
    Si=input("¿Quieres continuar? (S/N)" )
    if Si=="S" or Si=="s":
        save=input("¿Quieres guardar la operacion?: (S/N)" )
        if save=="S" or save=="s":
            continue
        if save=="N" or save=="n":
            os.system("cls")
            continue
    else:
        break