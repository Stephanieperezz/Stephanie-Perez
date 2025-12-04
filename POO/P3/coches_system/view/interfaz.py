from tkinter import *
from tkinter import messagebox
from controller import funciones

class Vistas:
    def __init__(self,ventana):
       ventana.title("Coches system")
       ventana.geometry("800x800")
       ventana.resizable(False,False)
       self.menu_principal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        Vistas.borrarPantalla(ventana)

        btn_auto=Button(ventana,text="1.- Autos", justify="center",command=lambda:Vistas.menu_acciones(ventana,"autos"))
        btn_auto.pack(pady=10)

        btn_camioneta=Button(ventana,text="2.- Camionetas", justify="center",command=lambda:Vistas.menu_acciones(ventana,"camionetas"))##MANDAR EL TIPO
        btn_camioneta.pack(pady=10)

        btn_camion=Button(ventana,text="3.- Camiones", justify="center",command=lambda:Vistas.menu_acciones(ventana,"camiones"))
        btn_camion.pack(pady=10)

        btn_salir=Button(ventana,text="4.- Salir", justify="center",command=ventana.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        if tipo=="autos":
            lbl_titulo=Label(ventana,text=f".::Haz entrado al menú de {tipo}::.")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",justify="center",command=lambda:Vistas.insertar_autos(ventana,tipo))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="2.- Consultar",justify="center",command=lambda:Vistas.consultar_autos(ventana,tipo))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="3.- Actualizar",justify="center",command=lambda:Vistas.cambiar_autos(ventana,tipo))
            btn_actualizar.pack(pady=10)
            btn_eliminar=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:Vistas.borrar_autos(ventana,tipo))
            btn_eliminar.pack(pady=10)
            btn_volver=Button(ventana,text="5.- Volver",justify="center",command=lambda:Vistas.menu_principal(ventana))
            btn_volver.pack(pady=10)
        elif tipo=="camionetas":
            lbl_titulo=Label(ventana,text=f".::Haz entrado al menú de {tipo}::.")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",justify="center",command=lambda:Vistas.insertar_camionetas(ventana,tipo))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="2.- Consultar",justify="center",command=lambda:Vistas.consultar_camionetas(ventana,tipo))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="3.- Actualizar",justify="center",command=lambda:Vistas.cambiar_camionetas(ventana,tipo))
            btn_actualizar.pack(pady=10)
            btn_eliminar=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:Vistas.borrar_camionetas(ventana,tipo))
            btn_eliminar.pack(pady=10)
            btn_volver=Button(ventana,text="5.- Volver",justify="center",command=lambda:Vistas.menu_principal(ventana))
            btn_volver.pack(pady=10)
        elif tipo=="camiones":
            lbl_titulo=Label(ventana,text=f".::Haz entrado al menú de {tipo}::.")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",justify="center",command=lambda:Vistas.insertar_camiones(ventana,tipo))
            btn_insertar.pack(pady=10)
            btn_consultar=Button(ventana,text="2.- Consultar",justify="center",command=lambda:Vistas.consultar_camiones(ventana,tipo))
            btn_consultar.pack(pady=10)
            btn_actualizar=Button(ventana,text="3.- Actualizar",justify="center",command=lambda:Vistas.cambiar_camiones(ventana,tipo))
            btn_actualizar.pack(pady=10)
            btn_eliminar=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:Vistas.borrar_camiones(ventana,tipo))
            btn_eliminar.pack(pady=10)
            btn_volver=Button(ventana,text="5.- Volver",justify="center",command=lambda:Vistas.menu_principal(ventana))
            btn_volver.pack(pady=10)

    @staticmethod
    def insertar_autos(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Bienvenido, vamos a insertar datos de {tipo}::.")
        lbl_titulo.pack(pady=10)


        lbl_marca=Label(ventana,text="Ingrese la marca:",justify="center")
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
        txt_marca.pack(pady=10)

        lbl_color=Label(ventana,text="Ingrese el color:",justify="center")
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
        txt_color.pack(pady=10)

        lbl_modelo=Label(ventana,text="Ingrese el modelo:",justify="center")
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
        txt_modelo.pack(pady=10)

        lbl_velocidad=Label(ventana,text="Ingrese la velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)
        velocidad=IntVar()
        txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
        txt_velocidad.pack(pady=10)

        lbl_caballaje=Label(ventana,text="Ingrese el caballaje:",justify="center")
        lbl_caballaje.pack(pady=10)
        caballaje=IntVar()
        txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
        txt_caballaje.pack(pady=10)

        lbl_plazas=Label(ventana,text="Ingrese las plazas:",justify="center")
        lbl_plazas.pack(pady=10)
        plazas=IntVar()
        txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
        txt_plazas.pack(pady=10)


        btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.insertar_coche(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get()))
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Mostrar autos::.")
        lbl_titulo.pack(pady=10)

        i=""
        registros=funciones.Controlador.mostrar()
        if len(registros)>0:
            for fila in registros:
                i=i+f"\n ID: {fila[0]}  Marca: {fila[1]}  Color: {fila[2]}  Modelo: {fila[3]} \n Velocidad: {fila[4]}  Caballaje: {fila[5]}  Plazas: {fila[6]}"
        else:
            messagebox.showwarning(icon="warning",message=".::No hay autos registrados::.")
        lbl_mostrar=Label(ventana,text=i,justify="center")
        lbl_mostrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def cambiar_autos(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a cambiar los datos de {tipo}::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID del auto a cambiar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar(id.get())

            if len(registros)>0:
                Vistas.borrarPantalla(ventana)
                lbl_marca=Label(ventana,text="Ingrese la nueva marca:",justify="center")
                lbl_marca.pack(pady=10)
                marca=StringVar()
                txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
                txt_marca.pack(pady=10)

                lbl_color=Label(ventana,text="Ingrese el nuevo color:",justify="center")
                lbl_color.pack(pady=10)
                color=StringVar()
                txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
                txt_color.pack(pady=10)

                lbl_modelo=Label(ventana,text="Ingrese el nuevo modelo:",justify="center")
                lbl_modelo.pack(pady=10)
                modelo=StringVar()
                txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
                txt_modelo.pack(pady=10)

                lbl_velocidad=Label(ventana,text="Ingrese la nueva velocidad:",justify="center")
                lbl_velocidad.pack(pady=10)
                velocidad=IntVar()
                txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
                txt_velocidad.pack(pady=10)

                lbl_caballaje=Label(ventana,text="Ingrese el nuevo caballaje:",justify="center")
                lbl_caballaje.pack(pady=10)
                caballaje=IntVar()
                txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
                txt_caballaje.pack(pady=10)

                lbl_plazas=Label(ventana,text="Ingrese las nuevas plazas:",justify="center")
                lbl_plazas.pack(pady=10)
                plazas=IntVar()
                txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
                txt_plazas.pack(pady=10)

                btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.actualizar(id.get(),marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get()))
                btn_guardar.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::. ")
        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def borrar_autos(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a eliminar un auto::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID del auto a eliminar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar(id.get())
            if len(registros)>0:
                lbl_confirm=Label(ventana,text="¿Seguro que deseas eliminar este registro?",justify="center")
                lbl_confirm.pack(pady=10)
                btn_confirm=Button(ventana,text="Confirmar",justify="center",command=lambda:funciones.Controlador.eliminar(id.get()))
                btn_confirm.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::.")

        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def insertar_camionetas(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Bienvenido, vamos a insertar datos de {tipo}::.")
        lbl_titulo.pack(pady=10)


        lbl_marca=Label(ventana,text="Ingrese la marca:",justify="center")
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
        txt_marca.pack(pady=10)

        lbl_color=Label(ventana,text="Ingrese el color:",justify="center")
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
        txt_color.pack(pady=10)

        lbl_modelo=Label(ventana,text="Ingrese el modelo:",justify="center")
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
        txt_modelo.pack(pady=10)

        lbl_velocidad=Label(ventana,text="Ingrese la velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)
        velocidad=IntVar()
        txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
        txt_velocidad.pack(pady=10)

        lbl_caballaje=Label(ventana,text="Ingrese el caballaje:",justify="center")
        lbl_caballaje.pack(pady=10)
        caballaje=IntVar()
        txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
        txt_caballaje.pack(pady=10)

        lbl_plazas=Label(ventana,text="Ingrese las plazas:",justify="center")
        lbl_plazas.pack(pady=10)
        plazas=IntVar()
        txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
        txt_plazas.pack(pady=10)

        lbl_traccion=Label(ventana,text="Ingrese la tracción:",justify="center")
        lbl_traccion.pack(pady=10)
        traccion=StringVar()
        txt_traccion=Entry(ventana,textvariable=traccion,justify="right",width=20)
        txt_traccion.pack(pady=10)

        lbl_cerrada=Label(ventana,text="Cerrada:",justify="center")
        lbl_cerrada.pack(pady=10)
        cerrada=StringVar()
        txt_cerrada=Entry(ventana,textvariable=cerrada,justify="right",width=20)
        txt_cerrada.pack(pady=10)


        btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.agregar_camioneta(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrada.get()))
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_camionetas(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Mostrar camionetas::.")
        lbl_titulo.pack(pady=10)

        i=""
        registros=funciones.Controlador.mostrar_camionetas()
        if len(registros)>0:
            for fila in registros:
                i=i+f"\n ID: {fila[0]}  Marca: {fila[1]}  Color: {fila[2]}  Modelo: {fila[3]} \n Velocidad: {fila[4]}  Caballaje: {fila[5]}  Plazas: {fila[6]}  Tracción: {fila[7]}  Cerrada: {fila[8]}"
        else:
            messagebox.showwarning(icon="warning",message=".::No hay camionetas registradas::.")
        lbl_mostrar=Label(ventana,text=i,justify="center")
        lbl_mostrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_camionetas(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a cambiar los datos de {tipo}::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID de la camioneta a cambiar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar_camioneta(id.get())

            if len(registros)>0:
                Vistas.borrarPantalla(ventana)
                lbl_marca=Label(ventana,text="Ingrese la nueva marca:",justify="center")
                lbl_marca.pack(pady=10)
                marca=StringVar()
                txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
                txt_marca.pack(pady=10)

                lbl_color=Label(ventana,text="Ingrese el nuevo color:",justify="center")
                lbl_color.pack(pady=10)
                color=StringVar()
                txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
                txt_color.pack(pady=10)

                lbl_modelo=Label(ventana,text="Ingrese el nuevo modelo:",justify="center")
                lbl_modelo.pack(pady=10)
                modelo=StringVar()
                txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
                txt_modelo.pack(pady=10)

                lbl_velocidad=Label(ventana,text="Ingrese la nueva velocidad:",justify="center")
                lbl_velocidad.pack(pady=10)
                velocidad=IntVar()
                txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
                txt_velocidad.pack(pady=10)

                lbl_caballaje=Label(ventana,text="Ingrese el nuevo caballaje:",justify="center")
                lbl_caballaje.pack(pady=10)
                caballaje=IntVar()
                txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
                txt_caballaje.pack(pady=10)

                lbl_plazas=Label(ventana,text="Ingrese las nuevas plazas:",justify="center")
                lbl_plazas.pack(pady=10)
                plazas=IntVar()
                txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
                txt_plazas.pack(pady=10)

                lbl_traccion=Label(ventana,text="Ingrese la nueva traccion:",justify="center")
                lbl_traccion.pack(pady=10)
                traccion=StringVar()
                txt_traccion=Entry(ventana,textvariable=traccion,justify="right",width=20)
                txt_traccion.pack(pady=10)

                lbl_cerrada=Label(ventana,text="Cerrada:",justify="center")
                lbl_cerrada.pack(pady=10)
                cerrada=StringVar()
                txt_cerrada=Entry(ventana,textvariable=cerrada,justify="right",width=20)
                txt_cerrada.pack(pady=10)

                btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.actualizar_camioneta(id.get(),marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),traccion.get(),cerrada.get()))
                btn_guardar.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::. ")
        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def borrar_camionetas(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a eliminar una camioneta::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID de la camioneta a eliminar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar_camioneta(id.get())
            if len(registros)>0:
                lbl_confirm=Label(ventana,text="¿Seguro que deseas eliminar este registro?",justify="center")
                lbl_confirm.pack(pady=10)
                btn_confirm=Button(ventana,text="Confirmar",justify="center",command=lambda:funciones.Controlador.eliminar_camionetas(id.get()))
                btn_confirm.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::.")

        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def insertar_camiones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Bienvenido, vamos a insertar datos de {tipo}::.")
        lbl_titulo.pack(pady=10)


        lbl_marca=Label(ventana,text="Ingrese la marca:",justify="center")
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
        txt_marca.pack(pady=10)

        lbl_color=Label(ventana,text="Ingrese el color:",justify="center")
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
        txt_color.pack(pady=10)

        lbl_modelo=Label(ventana,text="Ingrese el modelo:",justify="center")
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
        txt_modelo.pack(pady=10)

        lbl_velocidad=Label(ventana,text="Ingrese la velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)
        velocidad=IntVar()
        txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
        txt_velocidad.pack(pady=10)

        lbl_caballaje=Label(ventana,text="Ingrese el caballaje:",justify="center")
        lbl_caballaje.pack(pady=10)
        caballaje=IntVar()
        txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
        txt_caballaje.pack(pady=10)

        lbl_plazas=Label(ventana,text="Ingrese las plazas:",justify="center")
        lbl_plazas.pack(pady=10)
        plazas=IntVar()
        txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
        txt_plazas.pack(pady=10)

        lbl_eje=Label(ventana,text="Ingrese el eje:",justify="center")
        lbl_eje.pack(pady=10)
        eje=IntVar()
        txt_eje=Entry(ventana,textvariable=eje,justify="right",width=20)
        txt_eje.pack(pady=10)

        lbl_capacidadcarga=Label(ventana,text="Ingrese la capacidad de carga:",justify="center")
        lbl_capacidadcarga.pack(pady=10)
        capacidadcarga=IntVar()
        txt_capacidadcarga=Entry(ventana,textvariable=capacidadcarga,justify="right",width=20)
        txt_capacidadcarga.pack(pady=10)


        btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.insertar_camion(marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),eje.get(),capacidadcarga.get()))
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def consultar_camiones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Mostrar camionetas::.")
        lbl_titulo.pack(pady=10)

        i=""
        registros=funciones.Controlador.mostrar_camion()
        if len(registros)>0:
            for fila in registros:
                i=i+f"\n ID: {fila[0]}  Marca: {fila[1]}  Color: {fila[2]}  Modelo: {fila[3]} \n Velocidad: {fila[4]}  Caballaje: {fila[5]}  Plazas: {fila[6]}  Eje: {fila[7]}  Capacidad de carga: {fila[8]}"
        else:
            messagebox.showwarning(icon="warning",message=".::No hay camiones registrados::.")
        lbl_mostrar=Label(ventana,text=i,justify="center")
        lbl_mostrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def cambiar_camiones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a cambiar los datos de {tipo}::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID del camión a cambiar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar_camion(id.get())

            if len(registros)>0:
                Vistas.borrarPantalla(ventana)
                lbl_marca=Label(ventana,text="Ingrese la nueva marca:",justify="center")
                lbl_marca.pack(pady=10)
                marca=StringVar()
                txt_marca=Entry(ventana,textvariable=marca,justify="right",width=20)
                txt_marca.pack(pady=10)

                lbl_color=Label(ventana,text="Ingrese el nuevo color:",justify="center")
                lbl_color.pack(pady=10)
                color=StringVar()
                txt_color=Entry(ventana,textvariable=color,justify="right",width=20)
                txt_color.pack(pady=10)

                lbl_modelo=Label(ventana,text="Ingrese el nuevo modelo:",justify="center")
                lbl_modelo.pack(pady=10)
                modelo=StringVar()
                txt_modelo=Entry(ventana,textvariable=modelo,justify="right",width=20)
                txt_modelo.pack(pady=10)

                lbl_velocidad=Label(ventana,text="Ingrese la nueva velocidad:",justify="center")
                lbl_velocidad.pack(pady=10)
                velocidad=IntVar()
                txt_velocidad=Entry(ventana,textvariable=velocidad,justify="right",width=20)
                txt_velocidad.pack(pady=10)

                lbl_caballaje=Label(ventana,text="Ingrese el nuevo caballaje:",justify="center")
                lbl_caballaje.pack(pady=10)
                caballaje=IntVar()
                txt_caballaje=Entry(ventana,textvariable=caballaje,justify="right",width=20)
                txt_caballaje.pack(pady=10)

                lbl_plazas=Label(ventana,text="Ingrese las nuevas plazas:",justify="center")
                lbl_plazas.pack(pady=10)
                plazas=IntVar()
                txt_plazas=Entry(ventana,textvariable=plazas,justify="right",width=20)
                txt_plazas.pack(pady=10)

                lbl_eje=Label(ventana,text="Ingrese el nuevo eje:",justify="center")
                lbl_eje.pack(pady=10)
                eje=StringVar()
                txt_eje=Entry(ventana,textvariable=eje,justify="right",width=20)
                txt_eje.pack(pady=10)

                lbl_capacidadcarga=Label(ventana,text="Ingrese la nueva capacidad de carga:",justify="center")
                lbl_capacidadcarga.pack(pady=10)
                capacidadcarga=StringVar()
                txt_capacidadcarga=Entry(ventana,textvariable=capacidadcarga,justify="right",width=20)
                txt_capacidadcarga.pack(pady=10)

                btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:funciones.Controlador.actualizar_camion(id.get(),marca.get(),color.get(),modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),eje.get(),capacidadcarga.get()))
                btn_guardar.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::. ")
        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)
    @staticmethod
    def borrar_camiones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".::Vamos a eliminar un camión::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="Ingrese el ID del camión a eliminar:",justify="center")
        lbl_id.pack(pady=10)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=20)
        txt_id.pack(pady=10)

        def continuar():
            registros = funciones.Controlador.editar_camion(id.get())
            if len(registros)>0:
                lbl_confirm=Label(ventana,text="¿Seguro que deseas eliminar este registro?",justify="center")
                lbl_confirm.pack(pady=10)
                btn_confirm=Button(ventana,text="Confirmar",justify="center",command=lambda:funciones.Controlador.eliminar_camion(id.get()))
                btn_confirm.pack(pady=10)
                btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
                btn_volver.pack(pady=10)
            else:
                messagebox.showwarning(title="Registros",icon="warning",message=".::No hay registros con este ID::.")

        btn_continuar=Button(ventana,text="Continuar",justify="center",command=continuar)
        btn_continuar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:Vistas.menu_acciones(ventana,tipo))
        btn_volver.pack(pady=10)









