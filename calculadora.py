#PETICIÓN DE LA OPERACIÓN
operacion=str(input("Dime la operación\n::: "))

caracteres=operacion.split()

#FILTRO
def filtro(string):
    global numeritos, save
    #DECLARACIÓN DE LAS LISTAS PARA EL ALGORITMO
    numeritos=caracteres.copy()
    save=caracteres.copy()

    #ALGORITMO
    for i in caracteres:
        if i in "+-*/":
            numeritos.remove(i)

filtro(operacion)

#OPERACIONES
if len(caracteres)<=2:
    print("La operación está mal escrita\nEj: 2 + 2\n(Debe llevar espacios)")
else:
    for i in numeritos:
        if i!=save[-1]:
            if caracteres[1]=="+":
                res=int(caracteres[0])+int(caracteres[2])
                #print(f"La solución es-> {operacion}")
            elif caracteres[1]=="-":
                res=int(caracteres[0])-int(caracteres[2])
                #print(f"La solución es-> {operacion}")
            elif caracteres[1]=="*":
                res=int(caracteres[0])*int(caracteres[2])
                #print(f"La solución es-> {operacion}")
            elif caracteres[1]=="/":
                if caracteres[0]!="0" or caracteres[1]!="0":
                    res=int(caracteres[0])/int(caracteres[2])
                    #print(f"La solución es-> {operacion}")
                else:
                    print("En la división no puede haber un 0")
            else:
                print("El operador debe estar entre estos: + - * /")
            
            for i in range(3):
                caracteres.pop(0)
            caracteres.insert(0, res)
    print(f"El resultado es -> {caracteres[0]}")