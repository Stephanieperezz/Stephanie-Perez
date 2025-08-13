import pandas as pd
import conexionBD

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usuarios():
   print("\n \t.:: Sistema de gestión de cafetería ::.. \n\t\t1.-  Cliente nuevo  \n\t\t2.-  Cliente ya registrado \n\t\t3.-  Personal autorizado \n\t\t4.-  Exportar tablas \n\t\t5.-  Salir ")
   opcion=input("\t\t Elige una opción (1-5): ").upper().strip() 
   return opcion

def menu_pedidos():
   print("\n \t .::  Opciones ::. \n\t1.-  Realizar pedido \n\t2.-  Modificar orden \n\t3.-  Mostrar pedido \n\t4.-  Cancelar pedido \n\t5.-  Salir """)
   opcion = input("\t\t Elige una opción (1-5): ").upper().strip()
   return opcion   

def menu_personal():
   print("\n \t .::  Opciones ::. \n\t1.-  Pedidos cancelados \n\t2.-  Pedidos activos \n\t3.-  Borrar registros \n\t4.-  Mostrar total \n\t5.-  Salir""")
   opcion = input("\t\t Elige una opción (1-5): ").upper().strip()
   return opcion  

def exportar_tablas(conexion):
   tablas=["cancelados", "pedidos", "total_mesa", "usuarios", "personal"]
   excel=pd.ExcelWriter("bd_cafeteria.xlsx")
   conexiondb=conexionBD.conexion
   for i in tablas:
      cursor=conexiondb.cursor()
      cursor.execute(f"select * from {i}")
      columnas=[col[0]for col in cursor.description]
      datos=pd.DataFrame(cursor.fetchall(), columns=columnas)
      datos.to_excel(excel, sheet_name=i, index=False)
      cursor.close()
   excel.close()
   print("\n\t\t ✅ Las tablas se exportaron correctamente.")