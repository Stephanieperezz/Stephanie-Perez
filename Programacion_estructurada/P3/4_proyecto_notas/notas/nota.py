from conexionBD import *
from datetime import datetime
fecha_actual = datetime.now()

def crear(usuario_id, titulo, descripcion):
        try:
            cursor.execute("insert into notas (usuario_id, titulo, descripcion, fecha)values(%s,%s,%s,%s)", (usuario_id,titulo, descripcion, fecha_actual))
            conexion.commit()
            return True
        except:
              return False

def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        #registros=cursor.fetchall()
        return cursor.fetchall()  
        #if len (registros)>0:
            #return registros
        #else:
            #return []
    except:
        return []
    
def cambiar(id, titulo, descripcion):
    try: 
        cursor.execute("update notas set titulo=%s, descripcion=%s, fecha=now() where id=%s",(titulo, descripcion, id))
        conexion.commit()
        return True
    except:
        return False
    
def borrar(id):
    try: 
        cursor.execute("delete from notas where id=%s", (id,))
        conexion.commit()
        return True
    except:
        return False
    
def buscar(id):
    try:
        cursor.execute("select * from notas where id=%s", (id,))
        return cursor.fetchall()
    except:
        return False