import mysql.connector
from mysql.connector import Error
import os

#3EN PYTHON SI SOLO ES UN VAL HAY QUE PONERLE UNA COMA (NOMBRE, )
##EN SQL SE PONE LA INSTRUCCION 
##FETALL ES CUANDO REGRESA MAS DE DOS VALORES
##FETCHONE ES CUANDO REGRESA SOLO UN VALOR (CLAVE PRIMARIA)
peliculas={}

def borrarPantalla():
    os.system("cls")

def espereTecla():
   input("Presiona una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    ##CURSOR ES PARA PODER TRABAJAR CON LA TABLA
    ##EL CURSOR SE USA PARA EJECUTAR Y TRAER LOS REGISTROS DE LA CONSULTA PARA METERLOS A UNA LISTA
    if conexionBD!=None:
        print("Crear películas ")
        peliculas.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
        peliculas.update({"categoria": input("Ingrese la categoría: ").upper().strip()})
        peliculas.update({"clasificacion":input("Ingrese la clasificacion: ").upper().strip()})
        peliculas.update({"genero":input ("Ingresa el género: ").upper().strip()})
        peliculas.update({"idioma": input("Ingrese el idioma: ").upper().strip()})
        ###SQL A BASE DE DATOS
        cursor=conexionBD.cursor()
        ##CADA %s VA A TOMAR EL VALOR DE CADA UNA DE LAS VARIABLES
        sql="insert into peliculas ( nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
        ##CREAR UNA TUPLA CON LOS VALORES QUE SE SOLICITARON ANTES 
        val=(peliculas["nombre"], peliculas["categoria"], peliculas["clasificacion"], peliculas["genero"], peliculas["idioma"])
        cursor.execute(sql,val)
        conexionBD.commit()##COMIT HACE QUE SI NO FALLA LA INSTRUCCION ANTERIOR, SE PUEDA CONECTAR Y YA SE QUEDEN LOS VALORES
        ##COMMIN SOLO SE USA EN INSERT, DELETE AND UPDATE 
        print ("\n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")

def mostrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(".::Mostrar películas::.")
            print(f"{'ID':<10}{'Nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
            print ("_"*130)
            for elemento in registros:
                print(f"{elemento[0]:<10}{elemento[1]:<15}{elemento[2]:<15}{elemento[3]:<15}{elemento[4]:<15}{elemento[5]:<15}")
                print ("_"*130)
        else:
            print("NO HAY PELICULAS EN EL SISTEMA")

def buscarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingresa el nombre de la película que deseas buscar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre, )
        cursor.execute(sql, val)
        registros=cursor.fetchall()
        if registros:
            print(".::Buscar películas::.")
            print(f"{'ID':<10}{'Nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
            print ("_"*130)
            for elemento in registros:
                print(f"{elemento[0]:<10}{elemento[1]:<15}{elemento[2]:<15}{elemento[3]:<15}{elemento[4]:<15}{elemento[5]:<15}")
                print ("_"*130)
        else:
            print("No hay películas con este nombre en el sistema...")

def conectar():
    ##Esto se va a usar en todos los metodos, solo va a cambiar el nombre de la base de datos.
    """SE PUEDEN PRESENTAR 4 DISTINTOS ERRORES, 1) CONTRASEÑA NO COINCIDA O SIN CONTRASEÑA, 
    2) BASE DE DATOS DIFERENTE O INEXISTENTE, 3) SERVIDOR APAGADO, 4) USUARIO DISTINTO."""
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que presenta es: {e}")
        return None

def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingresa el nombre de la película que deseas borrar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre, )
        cursor.execute(sql, val)
        registros=cursor.fetchall()
        if registros:
            print(".::Borrar película::.")
            print(f"{'ID':<10}{'Nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
            print ("_"*130)
            for elemento in registros:
                print(f"{elemento[0]:<10}{elemento[1]:<15}{elemento[2]:<15}{elemento[3]:<15}{elemento[4]:<15}{elemento[5]:<15}")
                print ("_"*130)
            resp=input(f"¿Deseas borrar esta película ({nombre})?").upper().strip()
            if resp=="SI":
                sql="delete from peliculas where nombre=%s"
                val=(nombre, )
                cursor.execute(sql, val)
                conexionBD.commit()
                print("La película se ha borrado correctamente...")
        else:
            print("No hay películas con este nombre en el sistema...")

def modificarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql=("select * from peliculas")
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(".::Mostrar películas::.")
            print(f"{'ID':<10}{'Nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
            print ("_"*130)
            for elemento in registros:
                print(f"{elemento[0]:<10}{elemento[1]:<15}{elemento[2]:<15}{elemento[3]:<15}{elemento[4]:<15}{elemento[5]:<15}")
                print ("_"*130)
            nombre=input("Ingresa el nombre de la película que deseas modificar: ").upper().strip()
            cursor=conexionBD.cursor()
            sql=("select * from peliculas where nombre=%s")
            val=(nombre, )
            cursor.execute(sql, val)
            registros=cursor.fetchall()
            borrarPantalla()
            if registros:
                print(".::Borrar película::.")
                print(f"{'ID':<10}{'Nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
                print ("_"*130)
                for elemento in registros:
                    print(f"{elemento[0]:<10}{elemento[1]:<15}{elemento[2]:<15}{elemento[3]:<15}{elemento[4]:<15}{elemento[5]:<15}")
                    print ("_"*130)
                resp=input("Seguro que deseas modificar esta película? si/no").upper().strip()
                if resp=="SI":
                    peliculas["nombre"]=input("Ingresa el nuevo nombre: ").upper().strip()
                    peliculas["categoria"]=input("Ingrese la categoría: ").upper().strip()
                    peliculas["clasificacion"]=input("Ingrese la clasificacion: ").upper().strip()
                    peliculas["genero"]=input ("Ingresa el género: ").upper().strip()
                    peliculas["idioma"]= input("Ingrese el idioma: ").upper().strip()
                    sql="update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre = %s"
                    val=(peliculas["nombre"], peliculas["categoria"], peliculas["clasificacion"], peliculas["genero"], peliculas["idioma"], nombre)
                    cursor=conexionBD.cursor()
                    cursor.execute(sql,val)
                    conexionBD.commit()
                    print ("\n\t\t.::LA OPERACION SE REALIZÓ CON ÉXITO::.")