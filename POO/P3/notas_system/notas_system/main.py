"""
    1.-Implementar el MVC
    2.- Paradigma POO
    3.- App de escritorio con interfaz grafica
"""
from view import vista1
from tkinter import *

class App:
    def __init__(self,ventana):
        view=vista1.View(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()