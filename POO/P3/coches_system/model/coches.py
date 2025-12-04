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
    def consultar_autos():
      try:
         cursor.execute(
            "select * from autos"
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
      
      
       
