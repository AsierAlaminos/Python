from math import sqrt

class Calculadora():
    
    def __init__(self,operacion,lista):
        self.operacion=operacion
        self.lista=lista

    def separador_sec(lista,operacion):
        global operacion_red
        operacion_red=operacion+"·"
        x=0
        for i in range(len(operacion_red)):
            if operacion_red[0]=="(":
                break
            elif operacion_red[0] in "+-*/^$":
                lista.append(operacion_red[0])
                operacion_red=operacion_red[1:]
            elif operacion_red[x] in "+-*/^$":
                lista.append(operacion_red[:x])
                lista.append(operacion_red[x])
                operacion_red=operacion_red[x+1:]
                x=0
            x+=1
            if operacion_red[x]=="·":
                lista.append(operacion_red[:x])
                break
    
    def separador_prin(self,operacion):
        global lista_final
        lista_final=[]
        lista_parentesis=[]
        for i in range(len(operacion)):
            if len(operacion)==0:
                break
            elif operacion[-1]=="·":
                operacion=operacion[:-1]
            elif operacion[i]=="(":
                for j in range(len(operacion)):
                    if operacion[j]==")":
                        operacion_parentesis=operacion[i:j+1]
                        operacion=operacion[j+1:]
                        Calculadora.separador_sec(lista_parentesis,operacion_parentesis)
                        lista_final.insert(i,lista_parentesis)
                        lista_parentesis=[]
            elif len(operacion)==0:
                break
            else:
                Calculadora.separador_sec(lista_final,operacion)
                operacion=operacion_red

    def organizador(lista):
        global lista_organizada
        lista_organizada=[]
        for i in range(len(lista)):
            if lista[i] == "$" or lista[i] == "**":
                lista_organizada.append(i)
            elif lista[i] == "*" or lista[i] == "/":
                lista_organizada.append(i)
            elif lista[i] == "+" or lista[i] == "-":
                lista_organizada.append(i)
    
    def operaciones(self,lista,posicion):
        if (lista[posicion])=="+":
            res=float(lista[posicion-1])+float(lista[posicion+1])
            lista.insert(posicion,res)
            lista.pop(posicion-1)
            lista.pop(posicion+1)
            lista.pop(posicion)
        elif lista[posicion]=="-":
            res=float(lista[posicion-1])-float(lista[posicion+1])
            lista.insert(posicion,res)
            lista.pop(posicion-1)
            lista.pop(posicion+1)
            lista.pop(posicion)
        elif lista[posicion]=="*":
            res=float(lista[posicion-1])*float(lista[posicion+1])
            lista.insert(posicion,res)
            lista.pop(posicion-1)
            lista.pop(posicion+1)
            lista.pop(posicion)
        elif lista[posicion]=="/":
            if lista[0]!="0" or lista[1]!="0":
                res=float(lista[posicion-1])/float(lista[posicion+1])
                lista.insert(posicion,res)
                lista.pop(posicion-1)
                lista.pop(posicion+1)
                lista.pop(posicion)
            else:
                print("En la división no puede haber un 0")
        elif lista[posicion]=="**":
            res=float(lista[posicion-1])**float(lista[posicion+1])
            lista.insert(posicion,res)
            lista.pop(posicion-1)
            lista.pop(posicion+1)
            lista.pop(posicion)
        elif lista[posicion]=="$":
            res=sqrt(float(lista[posicion+1]))
            lista.insert(posicion,res)
            lista.pop(posicion+1)
            lista.pop(posicion-1)
        
    def starter(self):
        Calculadora.separador_prin(self.operacion)
        if self.operacion=="help":
            print("suma=+'\nresta='-'\nmultiplicación='*'\ndivisión='/'\nexponentes='**'\nraiz cuadrada='$'")
        elif len()