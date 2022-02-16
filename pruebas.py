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
"""

def separador(string):
    string=string+"·"
    lista_separada=[]
    x=0
    for i in range(len(string)):
        print("num x ->{}".format(x))
        print("string ->{}".format(string[x]))
        if string[x] in "+-*/":
            lista_separada.append(str(string[:x]))
            lista_separada.append(str(string[x]))
            string=string[x+1:]
            print(string)
            x=0
        x+=1
        if string[x]=="·":
            lista_separada.append(str(string[:x]))
            break

def separadorv2(string):
    def separadorv2(string):
    lista1=[]
    for u in range(len(string)):
        if string[0]=="(":
            for i in range(len(string)):
                if string[i]=="(":
                    for j in range(len(string)):
                        if string[j]==")":
                            lista1.append(string[i+1:j])
                            string=string[j+1:]
                            if string[0]=="(":
                                break
                            else:
                                break
                if string[0]!="(":
                    break
        else:
            cadena=string+"·"
            lista_separada=[]
            x=0
            for i in range(len(cadena)):
                print("num x ->{}".format(x))
                print("string ->{}".format(cadena[x]))
                if string[x] in "+-*/":
                    lista1.append(str(cadena[:x]))
                    lista1.append(str(cadena[x]))
                    cadena=cadena[x+1:]
                    print(cadena)
                    x=0
                x+=1
                if cadena[x]=="·":
                    lista1.append(str(cadena[:x]))
                    break
                
    print(lista1)
separadorv2("(2+2*3)/3+(3+2*2)")


separadorv2("(2+2*3)/3+(3+2*2)")