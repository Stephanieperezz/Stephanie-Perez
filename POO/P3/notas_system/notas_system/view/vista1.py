from tkinter import *
from tkinter import messagebox
from controller import controlador1
class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Gestion de Notas")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".: Menu Principal :.",justify="center")
        lbl_titulo.pack(pady=10)

        btn_registro=Button(ventana,text="1.- Registro",command=lambda:View.registro(ventana),justify="center")
        btn_registro.pack(pady=15)

        btn_login=Button(ventana,text="2.- Login",command=lambda:View.login(ventana),justify="center")
        btn_login.pack(pady=15)

        btn_salir=Button(ventana,text="3.- Salir",command=ventana.quit,justify="center")
        btn_salir.pack(pady=15)

    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_inicio=Label(ventana,text="Registro en el Sistema",justify="center")
        lbl_inicio.pack(pady=10)

        lbl_nombre=Label(ventana,text="¿Cual es tu nombre?",justify="center")
        lbl_nombre.pack(pady=10)

        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=15)

        lbl_apellidos=Label(ventana,text="¿Cuales son tus apellidos?",justify="center")
        lbl_apellidos.pack(pady=10)

        txt_apellidos=Entry(ventana)
        txt_apellidos.pack(pady=15)

        lbl_email=Label(ventana,text="Ingresa tu email: ",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana)
        txt_email.pack(pady=15)

        lbl_contrasena=Label(ventana,text="Ingresa tu contraseña: ",justify="center")
        lbl_contrasena.pack(pady=10)

        txt_contrasena=Entry(ventana,justify="center",show="*")
        txt_contrasena.pack(pady=15)

        btn_registrar=Button(ventana,text="Registrar",command=lambda:{
            controlador1.Controlador.registro(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_contrasena.get()),View.login(ventana)})
        btn_registrar.pack(pady=15)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def login(ventana):
        View.borrarPantalla(ventana)
        lbl_inicio=Label(ventana,text=".: Inicio en el Sistema :.",justify="center")
        lbl_inicio.pack(pady=10)
        
        lbl_email=Label(ventana,text="Ingresa tu email: ",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana)
        txt_email.pack(pady=15)
        txt_email.focus()

        lbl_contrasena=Label(ventana,text="Ingresa tu contraseña: ",justify="center")
        lbl_contrasena.pack(pady=10)

        txt_contrasena=Entry(ventana,justify="center",show="*")
        txt_contrasena.pack(pady=15)

        btn_entrar=Button(ventana,text="Entrar",command=lambda:
            controlador1.Controlador.iniciar_sesion(ventana,txt_email.get(),txt_contrasena.get()))
        btn_entrar.pack(pady=15)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        View.borrarPantalla(ventana)

        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        lbl_titulo=Label(ventana,text=f".::Bienvenido, {nombre} {apellidos} has iniciado sesion::.")
        lbl_titulo.pack(pady=10)

        btn_crear=Button(ventana,text="1.- Crear",command=lambda:View.crear(ventana))
        btn_crear.pack(pady=15)

        btn_mostrar=Button(ventana,text="2.- Mostrar",command=lambda:View.mostrar(ventana))
        btn_mostrar.pack(pady=15)

        btn_cambiar=Button(ventana,text="3.- Cambiar",command=lambda:View.cambiar_notas(ventana))
        btn_cambiar.pack(pady=15)

        btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:View.eliminar_notas(ventana))
        btn_eliminar.pack(pady=15)

        btn_regresar=Button(ventana,text="5.- Regresar",command=lambda:View.login(ventana))
        btn_regresar.pack(pady=15)

    @staticmethod
    def crear(ventana):
        View.borrarPantalla(ventana)
        lbl_crear=Label(ventana,text=".:: Crear Nota ::.", justify="center")
        lbl_crear.pack(pady=10)

        lbl_titulo=Label(ventana,text="Titulo: ",justify="center")
        lbl_titulo.pack(pady=10)

        txt_titulo=Entry(ventana)
        txt_titulo.pack(pady=15)
        txt_titulo.focus()

        lbl_descripcion=Label(ventana,text="Descripcion: ",justify="center")
        lbl_descripcion.pack(pady=10)

        txt_descripcion=Entry(ventana,justify="center")
        txt_descripcion.pack(pady=15)

        btn_guardar=Button(ventana,text="Guardar",command=lambda:controlador1.Controlador.crear_nota(id_user,
            txt_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=15)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def mostrar(ventana):
        View.borrarPantalla(ventana)
        lbl_mostrar=Label(ventana,text=f"{nom_user} {ape_user} tus notas son: ", justify="center")
        lbl_mostrar.pack(pady=10)

        filas=""
        registros=controlador1.Controlador.mostrar_nota(id_user)
        if len(registros)>0:
            num_nota=1
            for fila in registros:
                filas=filas+f"Nota: {num_nota} \n ID: {fila[0]}.- Titulo: {fila[2]}  Fecha de Creacion: {fila[4]} \n Descripcion: {fila[3]}"
                num_nota+=1
        else:
            messagebox.showwarning(icon="warning",message="No existen notas para este usuario...")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def cambiar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::{nom_user} {ape_user}, vamos a modificar una nota ::.",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_id=Label(ventana, text="ID de la Nota a Cambiar: ",justify="center")
        lbl_id.pack(pady=10)
        
        txt_id=Entry(ventana)
        txt_id.pack(pady=10)
        txt_id.focus()
        
        lbl_nuevo_titulo=Label(ventana,text="Nuevo Titulo: ",justify="center")
        lbl_nuevo_titulo.pack(pady=10)
        
        txt_nuevo_titulo=Entry(ventana)
        txt_nuevo_titulo.pack(pady=10)
        
        lbl_descripcion=Label(ventana,text="Nueva descripción: ",justify="center")
        lbl_descripcion.pack(pady=10)
        
        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=10)
        
        btn_guardar=Button(ventana,text="Guardar", command= lambda: controlador1.Controlador.cambiar_nota(txt_id.get(),txt_nuevo_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user) )
        btn_volver.pack(pady=10)
    
    @staticmethod
    def eliminar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::{nom_user} {ape_user}, vamos a eliminar una nota ::.",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_id=Label(ventana, text="ID de la Nota a eliminar: ",justify="center")
        lbl_id.pack(pady=10)
        
        txt_id=Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=10)
        
        btn_eliminar=Button(ventana,text="Eliminar", command= lambda: controlador1.Controlador.eliminar_nota(txt_id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_user,ape_user) )
        btn_volver.pack(pady=10)

