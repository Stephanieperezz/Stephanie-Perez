import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_calificaciones"
      )
      return conexion
  except Error as e:
    print(f"Ocurrió un error: {e}")
    return None

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\tOprima ENTER para continuar...")  

def menuPrincipal():
  print("\n\t..:::Sistema de Gestión de Calificaciones:::...\n\t\t1️⃣ -Agregar Calificacion  \n\t\t2️⃣ -Mostrar Calificacion \n\t\t3️⃣ -Calcular Promedio \n\t\t4️⃣ -Buscar Alumno \n\t\t5️⃣ -SALIR ")
  opcion=input("\n\t\tElige una opción (1-5): ").upper()
  return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t Agregar calificaciones")
   nombre=input("\n\t\tNombre del Alumno: ").upper().strip()
   calificaciones=[]
   for i in range(1,4):
      continua=True
      while continua:
       try:
        cal=float(input(f" \t\t\t Calificación {i}: "))
        if cal>=0 and cal<11:
         calificaciones.append(cal)
         continua=False
        else:
          print("\n\t\t  Ingresa un valor válido ")
       except ValueError:
        print(" \n\t\t Ingresa un valor númerico ") 
   lista.append([nombre]+calificaciones)
   try:
     cursor=conexionbd.cursor()
     sql="INSERT INTO calificaciones (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
     val=(lista[0][0],calificaciones[0],calificaciones[1],calificaciones[2])
     cursor.execute(sql,val)
     conexionbd.commit() 
     print(" \n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")
   except Error as e:
     print(f"Ocurrió un error: {e}")

def mostrar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t  .:: Mostrar calificaciones ::. ")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t\t Mostrar las calificaciones")
            print(f"{'ID':<10}{'Nombre':<15}{'Cal 1':<15}{'Cal 2':<15}{'Cal 3':<15}")
            print(f"-"*100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*100)
            alu=len(registros)
            if alu>1:
              print(f"Son {alu} alumnos")
            elif alu==1:
              print(f"Es {alu} alumno")
        else:
            ("\n\t\tAún no tienes calificaciones agregadas")
        print("\n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")

def calcular_promedios(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t.:: Calcular promedio ::")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        print(f"{'Nombre':<15}{'Promedio':<15}")
        print(f"-"*70)
        if registros:
            promedio_grupal=0
            for fila in registros:
              nombre=fila[1]
              calificaciones=fila[2:]
              promedio=sum(calificaciones)/3
              print(f"{nombre:<15}{promedio:.2f}")
              promedio_grupal+=promedio
            print(f"-"*70)
            promedio_grupal=promedio_grupal/len(registros)
            print(f"\n\t\tEl promedio del grupo es: {promedio_grupal:.2f}")
        else:
            ("\n\t\tNo hay calificaciones en el sistema")

def buscar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t.::Buscar alumnos::.")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            nom=input("\n\t\t Ingrese el nombre del alumno a buscar: ").upper()
            for i in registros:
               if nom==i[1]:
                  print(f"-"*100)
                  print(f"{'ID':<10}{'Nombre':<15}{'Cal 1':<15}{'Cal 2':<15}{'Cal 3':<15}{'Promedio':<15}")
                  print(f"-"*100)
                  print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{sum(i[2:])/3:.2f}")
                  print(f"-"*100)
        else:
            print("No hay almuno con este nombre")
