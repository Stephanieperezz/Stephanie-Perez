from tkinter import messagebox
from model import usuario,nota
from view import vista1

class Controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correcamente con el email: {email}",title="Usuarios")
        else:
            messagebox.showerror(icon="error",message="Ocurrio un error, vuelva a intentarlo",title="Usuarios")

    @staticmethod
    def iniciar_sesion(ventana,email,password):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(
                icon="info",
                message=f"{registro[1]} {registro[2]}, iniciaste sesión correctamente",
                title="Usuarios"
            )
            vista1.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
             messagebox.showerror(icon="error",message="Email y/o contraseña incorrectos, vuelva a intentarlo",title="Usuarios")

    #@staticmethod
    #def crear_nota(usuario_id,titulo):
        #respuesta=nota.Nota(usuario_id,titulo)###AQUI ANTES IBA TUTULO
        #if respuesta:
            #messagebox.showinfo(icon="info",message=Controlador.respuesta_sql(respuesta),title="Notas")
        #else:
           #messagebox.showerror(icon="error",message="Ocurrio un error, vuelva a intentarlo",title="Notas")

    @staticmethod 
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear nota",respuesta)

    @staticmethod
    def mostrar_nota(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    
    @staticmethod
    def eliminar_nota(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Eliminar nota",respuesta)

    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        respuesta=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql("Cambiar nota",respuesta)
    
    @staticmethod
    def respuesta_sql(titulo,respuesta): 
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="Acción realizada con éxito...")
        else:
            messagebox.showerror(icon="info",title=titulo,message="No fue posible realizar la acción, vuelva a intentar")
