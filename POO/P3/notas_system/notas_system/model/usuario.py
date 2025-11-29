
from conexionBD import *
import hashlib
import datetime



class Usuario:
    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena = self.hash_password(password)

    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre,apellidos,email,contrasena):
        try:
            contrasena_hasheada = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,NOW())",
                (nombre,apellidos,email,contrasena_hasheada)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None         
        

