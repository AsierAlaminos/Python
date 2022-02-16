#PETICIÓN DE LA OPERACIÓN
operacion=str(input("Dime la operación\n::: "))

#SEPARADOR
def separador(string):
    global lista_separada
    string=string+"·"
    lista_separada=[]
    x=0
    for i in range(len(string)):
        if string[x] in "+-*/":
            lista_separada.append(str(string[:x]))
            lista_separada.append(str(string[x]))
            string=string[x+1:]
            x=0
        x+=1
        if string[x]=="·":
            lista_separada.append(str(string[:x]))
            break

#FILTRO
def filtro(string, lista):
    global numeritos, num_operacion
    #DECLARACIÓN DE LAS LISTAS PARA EL ALGORITMO
    numeritos=lista.copy()
    num_operacion=lista.copy()

    #ALGORITMO
    for i in lista:
        if i in "+-*/":
            numeritos.remove(i)

#ORGANIZADOR
def organizador(lista):
    global lista_organizada
    lista_organizada=[]
    for i in range(len(lista)):
        if lista[i]=="*" or lista[i]=="/":
            lista_organizada.append(i)
    for i in range(len(lista)):
        if lista[i]=="+" or lista[i]=="-":
            lista_organizada.append(i)

separador(operacion)
filtro(operacion, lista_separada)
organizador(lista_separada)


#OPERACIONES
if len(lista_separada)<=2:
    print("La operación está mal escrita\nEj: 2+5-5*9")
else:
    for i in range(len(numeritos)-1):
        for i in lista_organizada:
            if lista_separada[i]=="+":
                res=float(lista_separada[i-1])+float(lista_separada[i+1])
                lista_separada.insert(i,res)
                lista_separada.pop(i-1)
                lista_separada.pop(i+1)
                lista_separada.pop(i)
            elif lista_separada[i]=="-":
                res=float(lista_separada[i-1])-float(lista_separada[i+1])
                lista_separada.insert(i,res)
                lista_separada.pop(i-1)
                lista_separada.pop(i+1)
                lista_separada.pop(i)
            elif lista_separada[i]=="*":
                res=float(lista_separada[i-1])*float(lista_separada[i+1])
                lista_separada.insert(i,res)
                lista_separada.pop(i-1)
                lista_separada.pop(i+1)
                lista_separada.pop(i)
            elif lista_separada[i]=="/":
                if lista_separada[0]!="0" or lista_separada[1]!="0":
                    res=float(lista_separada[i-1])/float(lista_separada[i+1])
                    lista_separada.insert(i,res)
                    lista_separada.pop(i-1)
                    lista_separada.pop(i+1)
                    lista_separada.pop(i)
                else:
                    print("En la división no puede haber un 0")
            else:
                print("El operador debe estar entre estos: + - * /")
            organizador(lista_separada)
            break
                
                
    print(f"El resultado es -> {lista_separada[0]}")