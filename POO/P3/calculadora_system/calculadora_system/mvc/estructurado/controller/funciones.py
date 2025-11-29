from tkinter import messagebox

#Controlador o Controller
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