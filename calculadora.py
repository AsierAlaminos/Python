from math import sqrt

#PETICIÓN DE LA OPERACIÓN
operacion=str(input("Dime la operación\t(Para ayuda escribe 'help')\n::: "))

#SEPARADOR
def separador_complementario(lista,string):
    global stringv1
    stringv1=string+"·"
    x=0
    for i in range(len(stringv1)):
        if stringv1[0]=="(":
            break
        if stringv1[0] in "+-*/":
            lista.append(str(stringv1[x]))
            stringv1=stringv1[x+1:]
        if stringv1[x] in "+-*/$":
            if stringv1[x:x+2]=="**":
                lista.append(str(stringv1[:x]))
                lista.append(str(stringv1[x:x+2]))
                stringv1=stringv1[x+2:]
            else:
                lista.append(str(stringv1[:x]))
                lista.append(str(stringv1[x]))
                stringv1=stringv1[x+1:]
            x=0
        x+=1
        if stringv1[x]=="·":
            lista.append(str(stringv1[:x]))
            break

def separador(string):
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
                            separador_complementario(lista_pasajera,string_pasajera)
                            if len(lista_pasajera)>=3:
                                lista1.append(lista_pasajera)
                                lista_pasajera=[]
                            if len(string)==0:
                                break
                            elif string[0]=="(":
                                break
                            else:
                                break
                if len(string)<=0:
                    break
                            
                if string[0]!="(":
                    break
        else:
            separador_complementario(lista1,string)
            string=stringv1

#ORGANIZADOR
def organizador(lista):
    global lista_organizada
    lista_organizada=[]
    for i in range(len(lista)):
        if lista[i]=="$":
            lista_organizada.append(i)
    for i in range(len(lista)):
        if lista[i]=="**":
            lista_organizada.append(i)
    for i in range(len(lista)):
        if lista[i]=="*" or lista[i]=="/":
            lista_organizada.append(i)
    for i in range(len(lista)):
        if lista[i]=="+" or lista[i]=="-":
            lista_organizada.append(i)

#OPERACIONES
def operaciones(lista,caracter):
    if (lista[caracter])=="+":
        res=float(lista[caracter-1])+float(lista[caracter+1])
        lista.insert(caracter,res)
        lista.pop(caracter-1)
        lista.pop(caracter+1)
        lista.pop(caracter)
    elif lista[caracter]=="-":
        res=float(lista[caracter-1])-float(lista[caracter+1])
        lista.insert(caracter,res)
        lista.pop(caracter-1)
        lista.pop(caracter+1)
        lista.pop(caracter)
    elif lista[caracter]=="*":
        res=float(lista[caracter-1])*float(lista[caracter+1])
        lista.insert(caracter,res)
        lista.pop(caracter-1)
        lista.pop(caracter+1)
        lista.pop(caracter)
    elif lista[caracter]=="/":
        if lista[0]!="0" or lista[1]!="0":
            res=float(lista[caracter-1])/float(lista[caracter+1])
            lista.insert(caracter,res)
            lista.pop(caracter-1)
            lista.pop(caracter+1)
            lista.pop(caracter)
        else:
            print("En la división no puede haber un 0")
    elif lista[caracter]=="**":
        res=float(lista[caracter-1])**float(lista[caracter+1])
        lista.insert(caracter,res)
        lista.pop(caracter-1)
        lista.pop(caracter+1)
        lista.pop(caracter)
    elif lista[caracter]=="$":
        res=sqrt(float(lista[caracter+1]))
        lista.insert(caracter,res)
        lista.pop(caracter+1)
        lista.pop(caracter)
    else:
        print("El operador debe estar entre estos: + - * /")
    organizador(lista)

separador(operacion)
print(f"lista1 -> {lista1}")

#BUCLES
if operacion=="help":
    print("suma=+'\nresta='-'\nmultiplicación='*'\ndivisión='/'\nexponentes='**'\nraiz cuadrada='$'")
elif len(lista1)<=2:
    print("La operación está mal escrita\nEj: 2+5-5*9")
else:
    organizador(lista1)
    print(f"lista_organizada -> {lista_organizada}")
    for i in range(len(lista1)):
        if len(lista1[i])>=3:
            organizador(lista1[i])
            print(f"lista_organizada{lista_organizada}")
            for u in lista_organizada:
                operaciones(lista1[i],u)
            lista1[i]=str(lista1[i][0])
    for j in range(len(lista1)):
        if len(lista1)<=1:
            break
        else:
            x=0
            x+=1
            operaciones(lista1,x)
                
                
    print(f"El resultado es -> {lista1[0]}")