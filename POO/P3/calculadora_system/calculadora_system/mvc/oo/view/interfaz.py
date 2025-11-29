from tkinter import *
from controller import funciones
from model import operaciones
from tkinter import messagebox

#Interfaz o View
class Vistas:
    def __init__(self,ventana):
       ventana.title("Calculadora Básica")
       ventana.geometry("800x600")
       ventana.resizable(False,False)
       self.interfaz(ventana)
    
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
 
    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.focus()
        txt_numero1.pack(side="top",anchor="center")

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="+",
                        command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()

        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("División",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()
 
    def menuPrincipal(self,ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        operacionesMenu.add_command(label="Consultar",command=lambda: self.consultar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda: self.cambiar(ventana))
        operacionesMenu.add_command(label="Borrar",command=lambda: self.eliminar(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)

    def eliminar(self,ventana): 
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=f".:: Borrar una Operación ::.")
        lbl_titulo.pack(pady=10)
        lbl_id=Label(ventana,text="ID de la Operación: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id= Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_eliminar=Button(ventana, text="Eliminar", command=lambda: funciones.Controladores.eliminar(id.get()))
        btn_eliminar.pack(pady=5)
        btn_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana) )
        btn_volver.pack(pady=5)

    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de la Operaciones ::. ")
        lbl_titulo.pack(pady=10)
        
        registros=funciones.Controladores.consultar()
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+f"\nOperacion: {num_operaciones} ID:{fila[0]} Fecha de Creación: {fila[1]}\n Operacion: {fila[2]}{fila[4]}{fila[3]}={fila[5]} "
                num_operaciones+=1
        else:
            messagebox.showinfo(icon="info",message=".. No existen operaciones en el Sistema ... agrega operaciones ...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana) )
        btn_volver.pack(pady=5)

    def cambiar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        
        lbl_titulo=Label(ventana, text=f".:: Cambiar una Operación ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la Operación: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id= Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        Label(ventana, text="Nuevo Número 1: ").pack(pady=5)
        n1=IntVar()
        numero1 = Entry(ventana,textvariable=n1,justify="right",width=5)
        numero1.pack(pady=5)

        Label(ventana, text="Nuevo Número 2: ").pack(pady=5)
        n2=IntVar()
        numero2=Entry(ventana,textvariable=n2,justify="right",width=5)
        numero2.pack(pady=5)

        Label(ventana, text="Nuevo Signo: ").pack(pady=5)
        sig=StringVar()
        signo=Entry(ventana,justify='center',textvariable=sig,width=5)
        signo.pack(pady=5)

        Label(ventana, text="Nuevo Resultado: ").pack(pady=5)
        resul=DoubleVar()
        resultado=Entry(ventana,textvariable=resul,justify="right",width=5)
        resultado.pack(pady=5)

        Button(ventana, text="Guardar", command=lambda: funciones.Controladores.cambiar(n1.get(),n2.get(),sig.get(),resul.get(),id.get()) ).pack(pady=5)
        Button(ventana, text="Volver", command=lambda: self.interfaz(ventana)).pack(pady=5)
    