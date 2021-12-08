def comparador(lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
                print(i)
    return False
lista1=str(input("Dime una lista: ").split())
lista2=str(input("Dime otra lista: ").split())
comparador(lista1, lista2)
