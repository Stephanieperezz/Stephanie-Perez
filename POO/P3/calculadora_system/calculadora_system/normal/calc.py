"""
  Crear una calculadora:
  1.- Dos campos de Texto
  2.- 4 botones para las Operaciones
  3.- Mostrar el Resultado en una alerta
"""
from tkinter import messagebox
from tkinter import *

def operaciones(titulo,numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="x":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}+{numero2}={resultado}")

# def mensaje(titulo,numero1,numero2,resultado):
#     messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}+{numero2}={resultado}")

# #Controlador o Controller
# def suma(numero1,numero2):
#     sumar=numero1+numero2
#     mensaje("Sumar",numero1,numero2,sumar)

# def resta(numero1,numero2):
#     restar=numero1-numero2
#     mensaje("Restar",numero1,numero2,restar)

# def multiplicacion(numero1,numero2):
#     multi=numero1*numero2
#     mensaje("Multiplicación",numero1,numero2,multi)

# def division(numero1,numero2):
#     dividir=numero1/numero2
#     mensaje("Dividir",numero1,numero2,dividir)




#Interfaz o View
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
                command=lambda: operaciones("Suma",n1.get(),n2.get(),"+"))
btn_suma.pack()

btn_resta=Button(ventana,text="-",command=lambda: operaciones("Resta",n1.get(),n2.get(),"-"))
btn_resta.pack()

btn_multiplicacion=Button(ventana,text="x",command=lambda: operaciones("Multiplicación",n1.get(),n2.get(),"x"))
btn_multiplicacion.pack()

btn_division=Button(ventana,text="/",command=lambda: operaciones("División",n1.get(),n2.get(),"/"))
btn_division.pack()

btn_salir=Button(ventana,text="Salir",command=ventana.quit)
btn_salir.pack()



ventana.mainloop()