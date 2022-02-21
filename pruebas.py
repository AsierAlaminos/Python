"""
string="12+12-2+2+2-22+3"
lista1=string.split("+")
print(lista1)
lista2=[]
for i in lista1:
    if "-" in i:
        insert=i.split("-")
        lista2.append(insert)
    else:
        lista2.append(i)
lista1=[]
for i in lista2:
    for u in i:
        lista1.append(u)
print(lista2)
print(lista1)
operacion=str(input("Dime la operación\n::: "))
caracteres=operacion.split()
print(len(caracteres))
print(caracteres
)


def separador(lista,string):
    global stringv1
    stringv1=string+"·"
    x=0
    for i in range(len(stringv1)):
        if stringv1[0]=="(":
            break
        if stringv1[0] in "+-*/":
            lista.append(str(stringv1[x]))
            stringv1=stringv1[x+1:]
        if stringv1[x] in "+-*/":
            lista.append(str(stringv1[:x]))
            lista.append(str(stringv1[x]))
            stringv1=stringv1[x+1:]
            x=0
        x+=1
        if stringv1[x]=="·":
            lista.append(str(stringv1[:x]))
            break

def separadorv2(string):
    global lista1
    lista1=[]
    lista_pasajera=[]
    for u in range(len(string)):
        if len(string)==0:
            break
        if string[-1]=="·":
            string=string[:-1]
        if string[0]=="(":
            for i in range(len(string)):
                if string[i]=="(":
                    string=string[i:]
                    for j in range(len(string)):
                        if string[j]==")":                            
                            string_pasajera=string[i+1:j]
                            string=string[j+1:]
                            separador(lista_pasajera,string_pasajera)
                            if len(lista_pasajera)>=3:
                                lista1.append(lista_pasajera)
                                lista_pasajera=[]
                            break
                if len(string)<=0:
                    break
                            
                if string[0]!="(":
                    break
        else:
            separador(lista1,string)
            string=stringv1
    print(f"lista1 -> {lista1}")

def organizador(lista):
    global lista_organizada
    lista_organizada=[]
    for i in range(len(lista)):
        if lista[i]=="*" or lista[i]=="/":
            lista_organizada.append(i)
    for i in range(len(lista)):
        if lista[i]=="+" or lista[i]=="-":
            lista_organizada.append(i)
    print(f"lista_organizada -> {lista_organizada}")

separadorv2("(2+2*3)/3+(3+2*2)")
organizador(lista1)
2+2*3/3+3+2*2


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
    #DECLARACIÓN DE LA LISTA
    numeritos=lista.copy()

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
"""
string="(2+2*3)/3+(3+2**2)+9"
print(string)
print(string[1:3])
print(string[3:])