#PETICIÓN DE LA OPERACIÓN
operacion=str(input("Dime la operación\n::: "))

caracteres=operacion.split()

#SEPARADOR
def separador(string):
    lista_separada=[]
    for i in range(len(string)):
        for j in string:
            if j in "+-*/":
                lista_separada.append(string[:i])
                string=string[i:]

#FILTRO
def filtro(string):
    global numeritos, num_operacion
    #DECLARACIÓN DE LAS LISTAS PARA EL ALGORITMO
    numeritos=caracteres.copy()
    num_operacion=caracteres.copy()

    #ALGORITMO
    for i in caracteres:
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

filtro(operacion)
organizador(caracteres)

#OPERACIONES
if len(caracteres)<=2:
    print("La operación está mal escrita\nEj: 2 + 2\n(Debe llevar espacios)")
else:
    for i in range(len(numeritos)-1):
        for i in lista_organizada:
            if caracteres[i]=="+":
                res=float(caracteres[i-1])+float(caracteres[i+1])
                caracteres.insert(i,res)
                caracteres.pop(i-1)
                caracteres.pop(i+1)
                caracteres.pop(i)
            elif caracteres[i]=="-":
                res=float(caracteres[i-1])-float(caracteres[i+1])
                caracteres.insert(i,res)
                caracteres.pop(i-1)
                caracteres.pop(i+1)
                caracteres.pop(i)
            elif caracteres[i]=="*":
                res=float(caracteres[i-1])*float(caracteres[i+1])
                caracteres.insert(i,res)
                caracteres.pop(i-1)
                caracteres.pop(i+1)
                caracteres.pop(i)
            elif caracteres[i]=="/":
                if caracteres[0]!="0" or caracteres[1]!="0":
                    res=float(caracteres[i-1])/float(caracteres[i+1])
                    caracteres.insert(i,res)
                    caracteres.pop(i-1)
                    caracteres.pop(i+1)
                    caracteres.pop(i)
                else:
                    print("En la división no puede haber un 0")
            else:
                print("El operador debe estar entre estos: + - * /")
            organizador(caracteres)
            break
                
                
    print(f"El resultado es -> {caracteres[0]}")