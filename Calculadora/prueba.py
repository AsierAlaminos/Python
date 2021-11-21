from tkinter import *
import os


"""
Configuración de la raíz
"""
root=Tk()
root.title("CALCULADORA")
#root.iconbitmap('masmenos.ico')
root.resizable(True, True)
root.config(bg="blue", cursor="x_cursor")
root.geometry("350x450")

"""
Configuración del primer Frame
"""
frame1=Frame(root)
frame1.pack()
frame1.config(bg="lightblue")
frame1.config(width=350, height=400, cursor="x_cursor")
frame1.config(relief="ridge")
frame1.config(bd=8)
frame1.pack(fill="both", expand=1)

"""
Configuración del Entry
"""
entry=Entry(frame1)
entry.pack()
entry.config(bg="red", font=("Verdana", 10))
#entry.grid(row=0, column=1)

"""
Configuración del Label
"""
label=Label(frame1, text="!Hola Mundo¡")
label.pack()
label.config(fg= "red", bg="green", font=("Verdana", 10))
texto=StringVar()
texto.set("Un nuevo texto")
label.config(textvariable=texto)
#label.grid(row=1, column=1)

"""
Configuración del texto largo
"""
textolar=Text(frame1)







root.mainloop()