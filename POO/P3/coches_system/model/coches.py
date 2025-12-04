from conexionBD import *
class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,eje,capacidadcarga):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        self.traccion = traccion
        self.cerrada = cerrada
        self.eje = eje
        self.capacidadcarga = capacidadcarga

    @staticmethod
    def insertar_autos(txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas):
      try:
         cursor.execute(
            "insert into autos values(null,%s,%s,%s,%s,%s,%s)",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas)
         )
         conexion.commit()
         return True
      except:
          return False
      
    @staticmethod
    def insertar_camionetas(txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_traccion,txt_cerrada):
      try:
         cursor.execute(
            "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_traccion,txt_cerrada)
         )
         conexion.commit()
         return True
      except:
          return False
      
    @staticmethod
    def insertar_camiones(txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_eje,txt_capacidadcarga):
      try:
         cursor.execute(
            "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_eje,txt_capacidadcarga)
         )
         conexion.commit()
         return True
      except:
          return False
      
    @staticmethod
    def actualizar_auto(txt_id,txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas):
       try:
         cursor.execute(
            "update autos set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_id)
         )
         conexion.commit()
         return True
       except: 
         return False
       
    @staticmethod
    def actualizar_camionetas(txt_id,txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_traccion,txt_cerrada):
       try:
         cursor.execute(
            "update camionetas set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s,cerrada=%s where id=%s",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_traccion,txt_cerrada,txt_id)
         )
         conexion.commit()
         return True
       except: 
         return False
       
    @staticmethod
    def actualizar_camiones(txt_id,txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_eje,txt_capacidadcarga):
       try:
         cursor.execute(
            "update camiones set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadcarga=%s where id=%s",
            (txt_marca,txt_color,txt_modelo,txt_velocidad,txt_caballaje,txt_plazas,txt_eje,txt_capacidadcarga,txt_id)
         )
         conexion.commit()
         return True
       except: 
         return False
       
    @staticmethod
    def borrar_auto(txt_id):
        try:
          cursor.execute(
            "delete from autos where id=%s",
            (txt_id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
    @staticmethod
    def borrar_camioneta(txt_id):
        try:
          cursor.execute(
            "delete from camionetas where id=%s",
            (txt_id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
    @staticmethod
    def borrar_camiones(txt_id):
        try:
          cursor.execute(
            "delete from camiones where id=%s",
            (txt_id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
    @staticmethod
    def consultar_autos():
      try:
         cursor.execute(
            "select * from autos"
         )
         return cursor.fetchall()
      except:    
         return []
      
    @staticmethod
    def consultar_camionetas():
      try:
         cursor.execute(
            "select * from camionetas"
         )
         return cursor.fetchall()
      except:    
         return []
      
    @staticmethod
    def consultar_camiones():
      try:
         cursor.execute(
            "select * from camiones"
         )
         return cursor.fetchall()
      except:    
         return []
      
    @staticmethod
    def consultar_autos_editar(txt_id):
      try:
         cursor.execute(
            "select * from autos where id=%s",(txt_id,)
         )
         return cursor.fetchall()
      except:    
         return []
      
    @staticmethod
    def consultar_camionetas_editar(txt_id):
      try:
         cursor.execute(
            "select * from camionetas where id=%s",(txt_id,)
         )
         return cursor.fetchall()
      except:    
         return []
      
    @staticmethod
    def consultar_camiones_editar(txt_id):
      try:
         cursor.execute(
            "select * from camiones where id=%s",(txt_id,)
         )
         return cursor.fetchall()
      except:    
         return []
      
       

