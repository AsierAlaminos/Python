import random

palabras= ["mexico", "colombia", "canada", "venezuela", "uruguay", "argentina", "guatemala", "panama", "ecuador", "españa", "francia","alemania", "noruega", "portugal"]
palabra_random=random.choice(palabras)
vidas=5
letras_palabra=list(palabra_random)
letras_adivinadas=[]

print("Bienvenido al ahorcado \nTienes 5 vidas para adivinar la palabra secreta")
print("La palaba secreta es de paises")
print(f"la palabra tiene una longitud de {len(palabra_random)} digitos")
print("_"*len(palabra_random))
while True:
    while True:
        letra=input("Dime una letra::: ")
        if len(letra)!=1 or letra.isnumeric():
            print("ESCRIBE UNA SOLA LETRA")
        else:
            if letra.lower() in letras_adivinadas:
                print("Ya has intentado esa letra")
                vidas-=1
                print(f"Te quedan {vidas} vidas")
            else:
                letras_adivinadas.append(letra)
                if letra.lower() in letras_palabra:
                    print("Bien! Has adivinado una letra")
                    break
                else:
                    print("Esa letra no se encuentra en la palabra")
                    vidas-=1
                    print(f"Te quedan {vidas} vidas")
                    break
    if vidas==0:
        print(f"No te quedan mas vidas, la palabra secreta era {palabra_random}")
        break

    estatus_actual = ""

    letras_faltantes = 0
    for letra in letras_palabra:
        if letra in letras_adivinadas:
            estatus_actual = estatus_actual + letra
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1

    print(estatus_actual)


    if letras_faltantes == 0:
        print("Felicidades haz ganado")
        break
