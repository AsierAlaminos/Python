from tkinter import *

root= Tk()
num1=""
num2=""
num=""
vacio=StringVar()
vacio.set("")
mosnum=Label(root)
resultado=Entry(root)
resultado.config(state=DISABLED, justify=CENTER)
def uno():
    global num
    num="1"
    añadir(num)
def dos():
    global num
    num="2"
    añadir(num)
def tres():
    global num
    num="3"
    añadir(num)
def cuatro():
    global num
    num="4"
    añadir(num)
def cinco():
    global num
    num="5"
    añadir(num)
def seis():
    global num
    num="6"
    añadir(num)
def siete():
    global num
    num="7"
    añadir(num)
def ocho():
    global num
    num="8"
    añadir(num)
def nueve():
    global num
    num="9"
    añadir(num)

def num1(numeros):
    global num1
    num1+=numeros

def añadir(operacion):
    global num1
    global num2
    if operacion=="":
        num1+=num
        num1=str(num1)
        numero=StringVar()
        numero.set(num1)
        mosnum.config(textvariable=numero)
    else:
        num2+=num
        num2=str(num2)
        number=StringVar()
        number.set(num2)
        resultado.config(textvariable=vacio)
        resultado.config(textvariable=number)



def sumar(operador1, operador2):
    global ans
    añadir("2")
    ans=float(operador1)+float(operador2)
    res=StringVar()
    res.set(ans)
    resultado.config(texvariable=res)

def resta(operador1, operador2):
    global ans
    añadir("2")
    ans=float(operador1)-float(operador2)
    res=StringVar()
    res.set(ans)
    resultado.config(texvariable=res)

def multiplicacion(operador1, operador2):
    global ans
    añadir("2")
    ans=float(operador1)*float(operador2)
    res=StringVar()
    res.set(ans)
    resultado.config(texvariable=res)

def division(operador1, operador2):
    global ans
    añadir("2")
    ans=float(operador1)/float(operador2)
    res=StringVar()
    res.set(ans)
    resultado.config(texvariable=res)

    

Button(root, text="1", command=uno).pack()

Button(root, text="2", command=dos).pack()

Button(root, text="3", command=tres).pack()

Button(root, text="4", command=cuatro).pack()

Button(root, text="5", command=cinco).pack()

Button(root, text="6", command=seis).pack()

Button(root, text="7", command=siete).pack()

Button(root, text="8", command=ocho).pack()

Button(root, text="9", command=nueve).pack()

Button(root, text="+", command=sumar).pack()

Button(root, text="-", command=resta).pack()

Button(root, text="*", command=multiplicacion).pack()

Button(root, text="/", command=division).pack()


resultado.pack()


root.mainloop()