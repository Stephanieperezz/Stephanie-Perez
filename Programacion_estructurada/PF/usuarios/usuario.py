from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, n_mesa, contrasena, pago):
    try:
        fecha=datetime.datetime.now()
        contrasena=hash_password(contrasena)
        cursor.execute("insert into usuarios (nombre, n_mesa, password, pago, fecha) values (%s,%s,%s,%s,%s)",(nombre, n_mesa, contrasena, pago, fecha))
        conexion.commit()
        return True
    except:
        return False
    
def clienteRegistrado(nombre,contrasena):
    try:
       contrasena=hash_password(contrasena)
       cursor.execute("select * from usuarios where nombre=%s and password=%s",(nombre,contrasena)) 
       return cursor.fetchone()
    except:
        return []     

def personal(nombre, contrasena):
    try:
        contrasena=hash_password(contrasena)
        cursor.execute("select * from personal where nombre=%s and password=%s", (nombre, contrasena))
        return cursor.fetchone()
    except:
        return[]
    