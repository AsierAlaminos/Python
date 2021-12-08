def histograma(lista):
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    for i in lista:
        print("+"*i)

lista=["2", "3", "5", "9"]
print(lista)
for i in range(len(lista)):
    lista[i]=int(lista[i])
print(lista)

histograma(lista)
