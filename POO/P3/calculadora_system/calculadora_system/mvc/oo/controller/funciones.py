from tkinter import messagebox
from model import operaciones

#Controlador o Controller
class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        # messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}{signo}{numero2}={resultado}")
        resul=messagebox.askquestion(title=titulo,message=f"{numero1}{signo}{numero2}={resultado}\n\n¿Quieres guardar la operación en la BD?",icon="question")
        if resul=="yes":
          respuesta=operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
          Controladores.respuesta_sql("Agregar Registro",respuesta)

    @staticmethod
    def eliminar(id):
        registros=operaciones.Operaciones.consultar_borrar(id)
        if len(registros)>0:
            respuesta=operaciones.Operaciones.eliminar(id)
            Controladores.respuesta_sql("Borrar Registro",respuesta)
        else:
            messagebox.showinfo(icon="info",message="...No hay registros con este ID...")
           


    @staticmethod
    def cambiar(n1,n2,sig,resul,id):
        respuesta=operaciones.Operaciones.actualizar(n1,n2,sig,resul,id)
        Controladores.respuesta_sql("Cambiar Registro",respuesta)

    @staticmethod
    def consultar():
        registros=operaciones.Operaciones.consultar()
        return registros

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="...¡Acción realizada con éxito!...")
        else:
            messagebox.showinfo(icon="info",title=titulo,message="...No fue posible realizar la acción, vuelva a intentar ...")
           