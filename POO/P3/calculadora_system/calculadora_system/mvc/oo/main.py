"""
  Crear una calculadora:
  1.- Dos campos de Texto
  2.- 4 botones para las Operaciones
  3.- Mostrar el Resultado en una alerta
  4.- Programacion OO
  5.- Implementar el MVC
"""

from view import interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()




