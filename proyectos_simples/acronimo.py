def acronimo(texto):
    split=texto.split()
    print(split[2])
    for i in len(split):
        inicial=split[i]
        acronimo=()
        acronimo.append(inicial)
    print(acronimo)

acronimo("Hola Muy Buenas Tardes")
