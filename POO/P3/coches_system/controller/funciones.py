from tkinter import *
from tkinter import messagebox
from view import interfaz
from model import coches

class Controlador:
    @staticmethod
    def insertar_coche(marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=coches.Coches.insertar_autos(marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.respuesta_sql("Insertar",respuesta)
    
    @staticmethod
    def agregar_camioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        respuesta=coches.Coches.insertar_camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controlador.respuesta_sql("Insertar",respuesta)

    @staticmethod
    def insertar_camion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadcarga):
        respuesta=coches.Coches.insertar_camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadcarga)
        Controlador.respuesta_sql("Insertar",respuesta)

    @staticmethod
    def actualizar(id,marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=coches.Coches.actualizar_auto(id,marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.respuesta_sql("Actualizar",respuesta)
    
    @staticmethod
    def actualizar_camioneta(id,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        respuesta=coches.Coches.actualizar_camionetas(id,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controlador.respuesta_sql("Actualizar",respuesta)

    @staticmethod
    def actualizar_camion(id,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadcarga):
        respuesta=coches.Coches.actualizar_camiones(id,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadcarga)
        Controlador.respuesta_sql("Actualizar",respuesta)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Coches.borrar_auto(id)
        Controlador.respuesta_sql("Eliminar",respuesta)
 
    @staticmethod
    def eliminar_camionetas(id):
        respuesta=coches.Coches.borrar_camioneta(id)
        Controlador.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def eliminar_camion(id):
        respuesta=coches.Coches.borrar_camiones(id)
        Controlador.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def mostrar():
        registros=coches.Coches.consultar_autos()
        return registros
   
    @staticmethod
    def editar(id):
        registros=coches.Coches.consultar_autos_editar(id)
        return registros
    
    @staticmethod
    def mostrar_camionetas():
        registros=coches.Coches.consultar_camionetas()
        return registros
    
    @staticmethod
    def editar_camioneta(id):
        registros=coches.Coches.consultar_camionetas_editar(id)
        return registros
    
    @staticmethod
    def mostrar_camion():
        registros=coches.Coches.consultar_camiones()
        return registros
    
    @staticmethod
    def editar_camion(id):
        registros=coches.Coches.consultar_camiones_editar(id)
        return registros
    
    @staticmethod
    def respuesta_sql(titulo,respuesta): 
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="Acción realizada con éxito...")
        else:
            messagebox.showerror(icon="info",title=titulo,message="No fue posible realizar la acción, vuelva a intentar")


