def multiplicador(lista):
    multiplicacion=1
    for i in lista:
        i=int(i)
        multiplicacion*=i
    print(f'multiplicacion: {multiplicacion}')

def sumar(lista):
    suma=0
    for i in lista:
        i=int(i)
        suma+=i
    print(f'suma: {suma}')


lista=(input("::: ").split())
multiplicador(lista)
sumar(lista)
