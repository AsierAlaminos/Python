import random

opciones=["piedra", "papel", "tijeras"]

def operador(jugador):
    eleccion=random.choice(opciones)
    if eleccion=="piedra":
        print("✊ Piedra")
    elif eleccion=="tijeras":
        print("✀ Tijeras")
    else:
        print("📄 Papel")
    jugador=jugador.lower()
    if jugador not in opciones:
        print("Elige Piedra Papel o Tijeras")
    else:
        if (eleccion=="piedra" and jugador=="piedra") or (eleccion=="papel" and jugador=="papel") or (eleccion=="tijeras" and jugador=="tijeras"):
            print("Empate")
        else:
            if (eleccion=="piedra" or jugador=="piedra") and (jugador=="papel" or eleccion=="papel"):
                print("Papel envuelve a Piedra")
            elif (eleccion=="tijeras" or jugador=="tijeras") and (jugador=="piedra" or eleccion=="piedra"):
                print("Piedra aplasta Tijeras")
            elif (eleccion=="papel" or jugador=="papel") and (jugador=="tijeras" or eleccion=="tijeras"):
                print("Tijeras cortan el Papel")


print("Bienvenido al juego de Piedra, Papel y Tijeras.")
operador(input(":::"))
