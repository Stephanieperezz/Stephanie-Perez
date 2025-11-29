from tkinter import *
from controller import funciones

#Interfaz o View
def interfaz():
    ventana=Tk()
    ventana.title("Calculadora Básica")
    ventana.geometry("600x400")
    ventana.resizable(False,False)

    n1=IntVar()
    n2=IntVar()
    txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
    txt_numero1.pack(side="top",anchor="center")

    txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
    txt_numero2.pack(side="top",anchor="center")

    btn_suma=Button(ventana,text="+",
                    command=lambda: funciones.operaciones("Suma",n1.get(),n2.get(),"+"))
    btn_suma.pack()

    btn_resta=Button(ventana,text="-",command=lambda: funciones.operaciones("Resta",n1.get(),n2.get(),"-"))
    btn_resta.pack()

    btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
    btn_multiplicacion.pack()

    btn_division=Button(ventana,text="/",command=lambda: funciones.operaciones("División",n1.get(),n2.get(),"/"))
    btn_division.pack()

    btn_salir=Button(ventana,text="Salir",command=ventana.quit)
    btn_salir.pack()



    ventana.mainloop()