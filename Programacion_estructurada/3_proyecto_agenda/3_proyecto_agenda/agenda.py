import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_agenda"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t Oprima cualquier tecla para continuar ...")  

def main_principal():
    print("\n\t..:::Sistema de Gestión de Agenda de Contactos :::...\n\t\t1️⃣- Agregar contacto  \n\t\t2️⃣- Mostrar Todos los contactos \n\t\t3️⃣- Buscar contacto por nombre \n\t\t4️⃣- Modificar contacto \n\t\t5️⃣- Eliminar contacto \n\t\t6️⃣- SALIR ")
    opcion=input("\n\t\t\t  Elige una opción (1-6): ").upper().strip()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t\t .::  Agregar Contactos ")
      nombre=input("Nombre del contacto: ").upper().strip()
      if nombre in agenda:
          print(f"\n\t\t  El contacto {nombre} ya existe ")
      else:
        tel=input(" Telefono: ").strip()
        email=input(" E-mail: ").lower().strip()
        agenda[nombre]=[tel,email]
        try:
            cursor=conexionBD.cursor()
            sql="insert into agenda (nombre,telefono,email) values (%s,%s,%s)"
            val=(nombre,tel,email)
            cursor.execute(sql,val)
            conexionBD.commit()
            input("\n\t\tLA OPERACION SE REALIZÓ CON EXITO \n\t Presiona ENTER para continuar...")
        except Error as e:
            print(f"\n\t\t Ocurió un erro: {e}")

def mostrar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print(" .::Mostrar Contacto::.")
      cursor=conexionBD.cursor()
      sql="select * from agenda"
      cursor.execute(sql)
      registros=cursor.fetchall()
      if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*100)
                con_age=len(registros)
            print(f"\n\t\t ...Hay {con_age} contactos en tu agenda..")
      else:
          print("\n\t\t No hay contactos en la agenda")
    input("\n\t\tLA OPERACION SE REALIZÓ CON EXITO \n\t Presiona ENTER para continuar...")

def buscar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!= None:
        print("\n\t\t .:: Buscar Contacto ::.")
        cursor=conexionBD.cursor()
        nombre = input("\n\t\tIngresa el nombre del contacto a buscar: ").upper().strip()
        sql="select * from agenda where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*100)
        else:
            print(f"\n\t\tEste contacto no se encuentra en la agenda")
        input("\n\t\tPresiona ENTER para continuar...")

def modificar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t .:: Modificar Contacto ::.")
        cursor=conexionBD.cursor()
        nombre=input("\n\t\t Dame el nombre del contacto que deseas modificar: ").upper().strip()
        sql="select* from agenda where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\t\t Contacto: {nombre} ")
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*100)
            resp=input("\n\t\t Desea modificar el contacto? SI/NO: ").upper().strip()
            if resp=="SI":
                nuevo_nom = input("\n\t\t Nuevo nombre: ").upper().strip()
                nuevo_num= input("\n\t\t Nuevo telefono: ").strip()
                nuevo_corr= input("\n\t\t Nuevo email: ").lower().strip()
                sql="update agenda set nombre=%s, telefono=%s, email=%s where nombre=%s"
                val=(nuevo_nom,nuevo_num,nuevo_corr,nombre)
                cursor.execute(sql,val)
                conexionBD.commit()
                print ("\n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")
        else:
            print("Este contacto no se encuentra en la agenda")
        input("\n\t\tPresiona ENTER para continuar...")

def eliminar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t .::Borrar contacto::.")
        cursor=conexionBD.cursor()
        nombre=input("\n\t\t Ingrese el nombre del contacto a borrar: ").upper().strip()
        sql="select * from agenda where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\t\t Contacto: {nombre} ")
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*100)
            resp=input(f"\n\t\t ¿Deseas borrar a {nombre} de tus contactos? SI/NO: ").upper().strip()
            if resp=="SI":
                sql="delete from agenda where nombre = %s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexionBD.commit()
                print ("\n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")
        else:
            print(f"\n\t\t El contacto no esta en la lista...")
        input("\n\t\tPresiona ENTER para continuar...")

