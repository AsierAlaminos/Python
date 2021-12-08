def contador(texto):
    split=texto.split()
    print(f"Han sido {len(split)}")

pregunta="S"
while pregunta=="S" or pregunta=="s":
    texto=str(input("¿En que estas pensando?"))
    contador(texto)
    pregunta=str(input("¿Quieres continuar (S/N)? "))
