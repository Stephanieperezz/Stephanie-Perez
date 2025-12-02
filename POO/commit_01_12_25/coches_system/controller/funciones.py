from tkinter import *
from tkinter import messagebox
from view import interfaz
from model import coches

class Controlador:
    @staticmethod
    def insertar_coche(marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=coches.Coches.insertar_autos(marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.respuesta_sql("Insertar",respuesta)

    def mostrar():
        registros=coches.Coches.consultar_autos()
        return registros
    
    def editar(id):
        registros=coches.Coches.consultar_autos_editar(id)
        return registros

    def actualizar(id,marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=coches.Coches.actualizar_auto(id,marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.respuesta_sql("Actualizar",respuesta)

    def eliminar(id):
        respuesta=coches.Coches.borrar_auto(id)
        Controlador.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def respuesta_sql(titulo,respuesta): 
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="Acción realizada con éxito...")
        else:
            messagebox.showerror(icon="info",title=titulo,message="No fue posible realizar la acción, vuelva a intentar")

