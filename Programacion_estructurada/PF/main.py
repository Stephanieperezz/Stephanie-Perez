import funciones
from cafee import cafeteria
from usuarios import usuario
import getpass
from datetime import datetime
from conexionBD import *
precios={
    "cafe americano": {"chico": 40, "grande": 45},
    "cappuccino": {"chico": 55, "grande": 60},
    "frappe": {"chico": 50, "grande": 75},
    "cafe de olla": {"chico": 50, "grande": 55},
    "latte": {"chico": 55, "grande": 60},
    "matcha": {"chico": 50, "grande": 70},
    "chilaquiles verdes": 85,
    "ensalada": 80,
    "sandwich de pollo": 70,
    "crepas": 75,
    "waffle": 80,
    "pay de manzana": 70
} 
##ESTE YA TIENE EXCEPCIONES
def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usuarios()

        if opcion=="1" or opcion=="CLIENTE NUEVO":
            funciones.borrarPantalla()
            print("\n \t ..:: ☕Registro al sistema ALMON COFFEE☕ ::..")
            while True:#3AGREGADO
                nombre=input("\t 👤¿Cuál es tu nombre?: ").upper().strip()
                if nombre.isalpha():
                    break
                else:
                    print("❌ Solo se permiten letras, intenta de nuevo.")
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            m_val=["tarjeta", "efectivo"]
            pago=input("\t Escriba el método de pago que desea efectivo/tarjeta: ").lower().strip()
            while pago not in m_val:
                print("\n\t\t ❌Escriba un método de pago válido")
                pago=input("\t Escriba el método de pago que desea efectivo/tarjeta: ").lower().strip()
            while True:
                try:##AGREGADO
                    n_mesa = int(input("\t ¿Cuál es el número de tu mesa?: ")) ##LO PUISE INT
                    lista_cafeteria=cafeteria.Nmesa()
                    ocupadas=[fila[2] for fila in lista_cafeteria]
                    if n_mesa in ocupadas:
                        print ("\n\t\t ❌Este número de mesa no está disponible, intenta con uno diferente.")
                        continue
                    break
                except ValueError:
                    print("\t\t Ingresa un número entero válido por favor")##FIN
            resultado=usuario.registrar(nombre, n_mesa, password, pago)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} correctamente")
            else:
                print(f"\n\t❌...No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="CLIENTE YA REGISTRADO": 
            funciones.borrarPantalla()
            print("\n \t ..::☕ALMON COFFEE☕ ::.. ")     
            nombre=input("\t 👤Ingresa tu nombre: ").upper().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip() 
            lista_usuarios=usuario.clienteRegistrado(nombre,password)
            if lista_usuarios:##CAMBIADO
                menu_pedidos(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2], lista_usuarios[4])
            else:
              print(f"\n\t❌Nombre y/o contraseña incorrectas por favor verifique ....")
              funciones.esperarTecla()    
        elif opcion=="3" or opcion=="PERSONAL AUTORIZADO": 
            funciones.borrarPantalla()
            print("\n \t ..::☕ALMON COFFEE☕ ::.. ")     
            nombre=input("\t 👤Ingresa tu nombre: ").upper().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip() 
            lista_usuarios=usuario.personal(nombre,password)
            if lista_usuarios:
                menu_personal(lista_usuarios[1])
            else:
              print(f"\n\t❌Nombre y/o contraseña incorrectas por favor verifique ....")
            funciones.esperarTecla() 
        elif opcion=="4" or opcion=="EXPORTAR TABLAS":  
            funciones.borrarPantalla()
            guardar=input("¿Deseas guardar las tablas en excel? si/no: ").lower().strip()
            while guardar not in ["si", "no"]:##AGREGADO
                funciones.borrarPantalla()
                print("\tPor favor selecciona una opción válida. ")
                guardar=input("¿Deseas guardar las tablas en excel? si/no: ").lower().strip()
            if guardar=="si":
                funciones.exportar_tablas(conexion)
            elif guardar=="no":
                print("\t\t No se exportaron las tablas.")
            funciones.esperarTecla()
        elif opcion=="5" or opcion=="SALIR":  
            print("✅Terminó la ejecución del sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("❌Opción no válida")
            opcion=True
            funciones.esperarTecla() 

def menu_personal(nombre):
    while True:
        funciones.borrarPantalla()
        print(f"\n\t\t 🧑‍💼 {nombre} bienvenida al sistema de personal de ALMON COFFEE 🧑‍💼")
        opcion=funciones.menu_personal()
        if opcion== '1' or opcion =="PEDIDOS CANCELADOS":
            funciones.borrarPantalla()
            lista_cafeteria=cafeteria.mostrarCancelados()
            if len (lista_cafeteria)>0:
                print(f"\n\t📝Pedidos cancelados")
                print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                print(f"_"*150)
                for fila in lista_cafeteria:
                    print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
            else:
                    print("⏳.::No hay pedidos cancelados::.⏳")
            funciones.esperarTecla()
        elif opcion =='2' or opcion =="PEDIDOS ACTIVOS":
            funciones.borrarPantalla()
            lista_cafeteria=cafeteria.mostrarOrdenes()
            if len (lista_cafeteria)>0:
                print(f"\n\t📝Pedidos activos")
                print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                print(f"_"*150)
                for fila in lista_cafeteria:
                    print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
            else:
                print("⏳.::No hay pedidos por el momento::.⏳")
            funciones.esperarTecla()
        elif opcion =='3' or opcion =="BORRAR REGISTROS":
            funciones.borrarPantalla()
            resp=input("¿Deseas solo eliminar una orden del día de hoy? si/no: ").lower().strip()
            while resp not in ["si", "no"]:##AGREGADO
                funciones.borrarPantalla()
                print ("\t\t Por favor selecciona una opción válida.")
                resp=input("¿Deseas solo eliminar una orden del día de hoy? si/no: ").lower().strip()
            if resp=="si":
                lista_cafeteria=cafeteria.Nmesa()
                if len (lista_cafeteria)>0:
                    print ("\n\n\t\t\t\t\t\t\t🧾.::ORDENES::.🧾")##TABULACIONES
                    print(f"\t\t\t\t\t{'|'}{'NOMBRE':<25}{'|'}{'NUMERO DE MESA':<25}{' |'}")
                    print(f"\t\t\t\t\t{'_' * 54}")
                    for fila in lista_cafeteria:
                        print(f"\t\t\t\t\t{'|'}{fila[1]:<25}{'|'}{fila[2]:<25}{' |'}")
                    while True:
                        try:##AGREGADO
                            n_mesa = int(input("\n\t Ingresa el número de mesa a borrar: ")) ##LO PUISE INT
                            lista_cafeteria=cafeteria.Nmesa()
                            ocupadas=[fila[2]for fila in lista_cafeteria]
                            if n_mesa not in ocupadas:
                                print("\t\t Este número de mesa no está activo.")
                                continue
                            break
                        except ValueError:
                            print("\t\t Ingresa un número entero válido por favor")##FIN
                respuesta=cafeteria.eliminarOrden(n_mesa)
                if respuesta:
                    print("✅.::SE HA ELIMINADO CORRECTAMENTE::.")
                else:
                    print("❌En este momento no fue posible eliminar los registros.")
            elif resp=="no": 
                res=input("¿Deseas eliminar todos los registros del día de hoy? si/no: ").lower().strip()
                while res not in ["si", "no"]:
                    print("\t\t Selecciona una opción válida por favor.")
                    res=input("¿Deseas eliminar todos los registros del día de hoy? si/no: ").lower().strip()
                if res=="si":
                    conf=input("¿Estas seguro de eliminar todos los registros? si/no: ").lower().strip()
                    while conf not in ["si", "no"]:
                        print("\t\t Selecciona una opción válida por favor.")
                        conf=input("¿Estas seguro de eliminar todos los registros? si/no: ").lower().strip()
                    if conf=="si":
                        respuesta=cafeteria.borrarRegistros()
                        if respuesta:
                            print("✅.::SE HA ELIMINADO CORRECTAMENTE::.")
                        else:
                            print("❌En este momento no fue posible eliminar los registros.")
                    elif conf=="no":
                        print ("❌No se ha borrado ningún registro. ")
                elif res=="no":
                    print("❌No se ha eliminado ningún registro.")
            funciones.esperarTecla()
        elif opcion== '4' or opcion=="MOSTRAR TOTAL":
            funciones.borrarPantalla()
            lista_cafeteria=cafeteria.mostrarpers()
            if len (lista_cafeteria)>0:
                print("\t 🧾TOTAL Y METODO DE PAGO SEGUN NUMERO DE MESA🧾")##TABULACIONES
                print(f"{'|'}{'# MESA':<15}{'|'}{'METODO DE PAGO':<25}{'|'}{'TOTAL':<25}{'|'}")
                print(f"_"*69)
                for fila in lista_cafeteria:
                    print (f"{'|'}{fila[0]:<15}{'|'}{fila[1]:<25}{'|'}{fila[2]:<25}{'|'}")
            else:
                print("⏳.::No hay pedidos por el momento::.⏳")
            funciones.esperarTecla()
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t ❌Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

def menu_pedidos(id, nombre, n_mesa, pago):
    total_general = cafeteria.obtenerTotalMesa(n_mesa)
    while True:
        total_general=total_general
        funciones.borrarPantalla()
        print(f"\n \t \t \t 👤 Bienvenido {nombre}, has iniciado sesión ...")
        opcion=funciones.menu_pedidos()
        if opcion == '1' or opcion=="REALIZAR PEDIDO":
            total_general = cafeteria.obtenerTotalMesa(n_mesa)
            otro="si"
            while otro=="si":
                precio=0
                funciones.borrarPantalla()
                tipo="alimento"
                tamaño="no aplica"
                azucar="no aplica"
                sabor="no aplica"
                extra="no aplica"
                val=["cafe americano", "cappuccino", "frappe", "cafe de olla", "latte", "matcha", "chilaquiles verdes", "ensalada", "sandwich de pollo", "crepas", "waffle", "pay de manzana"]
                print(f"\n \t .:: Realizar pedido ::. ")
                print("\n\t\t\tMENÚ DE BEBIDAS🧋")
                print("\tProducto\t\tCH\tGDE")
                print("\t1. Cafe americano\t$40\t$45")
                print("\t2. Cappuccino\t\t$55\t$60")
                print("\t3. Frappe\t\t$50\t$75")
                print("\t4. Cafe de olla\t\t$50\t$55")
                print("\t5. Latte\t\t$55\t$60")
                print("\t6. Matcha\t\t$50\t$70")
                print("\n\t\t\tMENÚ DE ALIMENTOS🥗")
                print("\t7. Chilaquiles verdes\t\t$85")
                print("\t8. Ensalada \t\t\t$80")
                print("\t9. Sandwich de pollo\t\t$70")
                print("\t10. Crepas\t\t\t$75")
                print("\t11. Waffle\t\t\t$80")
                print("\t12. Pay de manzana\t\t$70")
                producto=input("\tEscriba el nombre del producto que deseas ordenar: ").lower()
                while producto not in val:
                    print("❌Selecciona un producto válido por favor")
                    producto=input("\tEscriba el nombre del producto que deseas ordenar: ").lower()
                funciones.borrarPantalla()
                if producto in ["chilaquiles verdes", "ensalada", "sandwich de pollo", "crepas", "waffle", "pay de manzana"]:
                    cantidad=int(input("\tCantidad: "))
                    while cantidad <1:
                        print("\t❌ La cantidad tiene que ser mayor a 1. ")
                        cantidad=int(input("\tCantidad: "))
                    respuesta=cafeteria.realizarPedido( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa)
                    precio+=cantidad*precios[producto]
                if producto in ["cafe americano", "cappuccino", "frappe", "cafe de olla", "latte", "matcha"]:
                    tipo="bebida"
                    cuanto=int(input("\tCantidad: "))
                    while cuanto <1:
                        print("\n\t❌ La cantidad tiene que ser mayor a 1. ")
                        cuanto=int(input("\tCantidad: "))
                    funciones.borrarPantalla()
                    for i in range(1, cuanto+1):
                        print(f"BEBIDA #{i}")
                        cantidad="1"
                        tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                        while tamaño not in ["chico", "grande"]:
                            print("	❌Selecciona un tamaño válido por favor")
                            tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                        if producto == "frappe":
                            funciones.borrarPantalla()
                            azucar="no aplica"
                            sabor = input("\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor de tu frappé: ").lower().strip()
                            while sabor not in ["fresa", "nutella", "oreo"]:
                                print("❌Este sabor no está disponible")
                                sabor = input("\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor que deseas: ").lower().strip()
                            extra = input(f"¿Desea agregar {sabor} extra por $10 más? si/no: ").lower().strip()
                            while extra not in ["si", "no"]:
                                print("\t\t Selecciona una opción válida por favor.")
                                extra = input(f"¿Desea agregar {sabor} extra por $10 más? si/no: ").lower().strip()
                            if extra=="si":
                                precio+=10
                                funciones.borrarPantalla()
                        else: 
                            azucar = input("¿Cuántos sobres de azúcar deseas agregar?: ")
                        precio+=precios[producto][tamaño]
                        respuesta=cafeteria.realizarPedido( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa)
                if respuesta:
                    funciones.borrarPantalla()
                    print(f"\n\t✅ .::Se realizó tu orden con exito::.✅ ")
                else:
                    print(f"\n\t ❌.::No fue posible agregar tu orden en este momento::.")
                total_general+=precio
                cafeteria.actualizarTotalMesa(n_mesa, total_general, pago)
                print(f"\t\t🧾Tu total: {total_general}")
                otro=input("¿Deseas agregar otra orden? si/no: ").lower().strip()
                while otro not in ["si", "no"]:
                    print("\t\t Selecciona una opción válida por favor.")
                    otro=input("¿Deseas agregar otra orden? si/no: ").lower().strip()
            funciones.borrarPantalla()
        elif opcion == '2' or opcion=="MODIFICAR ORDEN":
            funciones.borrarPantalla()
            continuar=False
            while True:
                try: ##AGREGADO
                    n_mesa=int(input("Ingresa el numero de tu mesa: "))
                    lista_cafeteria=cafeteria.Nmesa()
                    ocupadas=[fila[2] for fila in lista_cafeteria]
                    if n_mesa in ocupadas:
                        funciones.borrarPantalla()
                        total_general = cafeteria.obtenerTotalMesa(n_mesa)
                        lista_cafeteria=cafeteria.mostrarPedido(n_mesa)
                        if len (lista_cafeteria)>0:
                            print(f"\n\t📝 Mostrar tus pedidos")
                            print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                            print(f"_"*150)
                            for fila in lista_cafeteria:
                                print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
                            continuar=True
                            break
                        else:
                            print("⏳.::No hay pedidos en este usuario::.⏳")
                            funciones.esperarTecla()
                            break
                    else:
                        print("\n\t\t⏳.::Este número de mesa no tiene ordenes registradas::.⏳")
                        funciones.esperarTecla()
                        break
                except ValueError:
                    print("\t\t Ingresa un número válido y entero de mesa por favor.")##FIN
            if continuar:
                resp=input("Deseas modificar un pedido de tu orden? si/no: "). lower().strip()
                while resp not in ["si", "no"]:
                    print("\t\t Por favor selecciona una opción válida")
                    resp=input("Deseas modificar un pedido de tu orden? si/no: "). lower().strip()
                if resp=="si":
                    print(f"\n \t ⚙️.:: {nombre}, vamos a modificar tu orden ::. \n")
                    id = input("\t \t ID del pedido a actualizar: ")
                    lista_cafeteria = cafeteria.mostrarPedido(n_mesa)
                    precio_viejo = 0
                    precio=0
                    for fila in lista_cafeteria:
                        if str(fila[0]) == id:
                            producto_viejo = fila[1]
                            cantidad_vieja = int(fila[3])
                            tamaño_viejo = fila[4]
                            if producto_viejo in precios:
                                if isinstance(precios[producto_viejo], dict):
                                    precio_viejo = precios[producto_viejo][tamaño_viejo] * cantidad_vieja
                                else:
                                    precio_viejo = precios[producto_viejo] * cantidad_vieja
                            break 
                    funciones.borrarPantalla()
                    tipo="alimento"
                    tamaño="no aplica"
                    azucar="no aplica"
                    sabor="no aplica"
                    extra="no aplica"
                    val=["cafe americano", "cappuccino", "frappe", "cafe de olla", "latte", "matcha", "chilaquiles verdes", "ensalada", "sandwich de pollo", "crepas", "waffle", "pay de manzana"]
                    print(f"\n \t .:: Realizar pedido ::. ")
                    print("\n\t\t\tMENÚ DE BEBIDAS🧋")
                    print("\tProducto\t\tCH\tGDE")
                    print("\t1. Cafe americano\t$40\t$45")
                    print("\t2. Cappuccino\t\t$55\t$60")
                    print("\t3. Frappe\t\t$50\t$75")
                    print("\t4. Cafe de olla\t\t$50\t$55")
                    print("\t5. Latte\t\t$55\t$60")
                    print("\t6. Matcha\t\t$50\t$70")
                    print("\n\t\t\tMENÚ DE ALIMENTOS🥗")
                    print("\t7. Chilaquiles verdes\t\t$85")
                    print("\t8. Ensalada \t\t\t$80")
                    print("\t9. Sandwich de pollo\t\t$70")
                    print("\t10. Crepas\t\t\t$75")
                    print("\t11. Waffle\t\t\t$80")
                    print("\t12. Pay de manzana\t\t$70")
                    producto=input("\tEscriba el nombre del nuevo producto que deseas ordenar: ").lower()
                    while producto not in val:
                        print("❌Selecciona un nuevo producto válido por favor")
                        producto=input("\tEscriba el nombre del nuevo producto que deseas ordenar: ").lower()
                    funciones.borrarPantalla()
                    if producto in ["chilaquiles verdes", "ensalada", "sandwich de pollo", "crepas", "waffle", "pay de manzana"]:
                        cantidad=int(input("\tCantidad: "))
                        while cantidad <1:
                            print("\t❌ La cantidad tiene que ser mayor a 1. ")
                            cantidad=int(input("\tCantidad: "))
                        respuesta=cafeteria.modificarAlimento(id, producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa)
                        precio+=cantidad*precios[producto]
                    if producto in ["cafe americano", "cappuccino", "frappe", "cafe de olla", "latte", "matcha"]:
                        tipo="bebida"
                        cuanto=int(input("\tCantidad: "))
                        while cuanto <1:
                            print("\n\t❌ La cantidad tiene que ser mayor a 1. ")
                            cuanto=int(input("\tCantidad: "))
                        funciones.borrarPantalla()
                        if cuanto>1:
                            for i in range(1, cuanto+1):
                                print(f"BEBIDA #{i}")
                                cantidad=1
                                tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                                while tamaño not in ["chico", "grande"]:
                                    print("❌Selecciona un tamaño válido por favor")
                                    tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                                if producto == "frappe":
                                    funciones.borrarPantalla()
                                    azucar="no aplica"
                                    sabor = input("\n\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor de tu frappé: ").lower().strip()
                                    while sabor not in ["fresa", "nutella", "oreo"]:
                                        print("❌Este sabor no está disponible")
                                        sabor = input("\n\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor que deseas: ").lower().strip()
                                    funciones.borrarPantalla()
                                    extra = input(f"¿Desea agregar {sabor} extra por $10 más? si/no: ").lower().strip()
                                    while extra not in ["si", "no"]:
                                        print("\t\t Selecciona una opción válida por favor.")
                                        extra = input(f"¿Desea agregar {sabor} extra por $10 más? si/no: ").lower().strip()
                                    funciones.borrarPantalla()
                                    if extra=="si":
                                        precio+=10
                                else: 
                                    azucar = input("¿Cuántos sobres de azúcar deseas agregar?: ")
                                    funciones.borrarPantalla()
                                precio+=precios[producto][tamaño]
                                respuesta=cafeteria.modificarBebidas(id, producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa)
                        elif cuanto==1:
                            cantidad=1
                            tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                            while tamaño not in ["chico", "grande"]:
                                print("	❌Selecciona un tamaño válido por favor")
                                tamaño = input("🥤Selecciona el tamaño de tu bebida chico/grande: ").lower().strip()
                            funciones.borrarPantalla()
                            if producto == "frappe":
                                azucar="no aplica"
                                sabor = input("\n\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor de tu frappé: ").lower().strip()
                                while sabor not in ["fresa", "nutella", "oreo"]:
                                    print("❌Este sabor no está disponible")
                                    sabor = input("\n\t\t SABORES: \n\t🍓fresa \n\t🍫nutella \n\t🍪oreo \n\tSelecciona el sabor que deseas: ").lower().strip()
                                funciones.borrarPantalla()
                                extra = input(f"¿Desea agregar {sabor} extra por $10 más? SI/NO: ").lower().strip()
                                while extra not in ["si", "no"]:
                                    print("\t\t Selecciona una opción válida por favor.")
                                    extra = input(f"¿Desea agregar {sabor} extra por $10 más? si/no: ").lower().strip()
                                funciones.borrarPantalla()
                                if extra=="si":
                                    precio+=10
                                    funciones.borrarPantalla()
                            else: 
                                azucar = input("¿Cuántos sobres de azúcar deseas agregar?: ")
                                funciones.borrarPantalla()
                            precio+=precios[producto][tamaño]
                            respuesta=cafeteria.modificarAlimento(id, producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa)
                    if respuesta:
                        funciones.borrarPantalla()
                        print(f"\n\t ✅.::Se actualizó tu orden con exito::.✅ ")
                    else:
                        print(f"\n\t❌ .::No fue posible actualizar tu orden en este momento::.")  
                    total_general = total_general - precio_viejo + precio
                    cafeteria.actualizarTotalMesa(n_mesa, total_general, pago)
                    print(f"\t\t🧾Tu total:: {total_general}") 
                funciones.esperarTecla()       
        elif opcion == '3' or opcion=="MOSTRAR PEDIDO":
            funciones.borrarPantalla()
            while True:##AGREGADO
                try:
                    n_mesa=int(input("Ingresa el numero de tu mesa: "))
                    lista_cafeteria=cafeteria.Nmesa()
                    ocupadas=[fila[2]for fila in lista_cafeteria]
                    if n_mesa in ocupadas:
                        lista_cafeteria=cafeteria.mostrarPedido(n_mesa)
                        if len (lista_cafeteria)>0:
                            print(f"\n\t📝Mostrar tus pedidos")
                            print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                            print(f"_"*150)
                            for fila in lista_cafeteria:
                                print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
                            total=cafeteria.mostrarTotal(n_mesa)
                            print(f"\n\t🧾Total general de la mesa {n_mesa}: ${total}")
                            funciones.esperarTecla()
                            break
                        else:
                            print("⏳.::No hay pedidos en este usuario::.⏳")
                            funciones.esperarTecla()
                            break
                    else:
                        print("\n\t\t❌.::Este numero de mesa no está activo::.")
                        funciones.esperarTecla()
                        break
                except ValueError:
                    print("\t\t Ingresa un número entero válido por favor")##FIN
        elif opcion == '4' or opcion=="CANCELAR PEDIDO":
            funciones.borrarPantalla()
            continuar=False
            while True:
                try:
                    n_mesa=int(input("Ingresa el numero de tu mesa: "))
                    funciones.borrarPantalla()
                    total_general = cafeteria.obtenerTotalMesa(n_mesa)
                    lista_cafeteria=cafeteria.Nmesa()
                    ocupadas=[fila[2] for fila in lista_cafeteria]
                    if n_mesa in ocupadas:
                        lista_cafeteria=cafeteria.mostrarPedido(n_mesa)
                        if len (lista_cafeteria)>0:
                            print(f"\n\t📝Mostrar tus pedidos")
                            print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                            print(f"_"*150)
                            for fila in lista_cafeteria:
                                print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
                            continuar=True
                            break
                        else:
                            print("⏳.::No hay pedidos en este usuario::.⏳")
                            funciones.esperarTecla()
                            break
                    else:
                        print("\n\t\t⏳.::Este número de mesa no tiene ordenes registradas::.⏳")
                        funciones.esperarTecla()
                        break           
                except ValueError:
                    print("\t\t Ingresa un número válido y entero de mesa por favor.")##FIN
            if continuar:        
                    print("\t\t ‼️  AL CANCELAR TODO TU PEDIDO SE ELIMINA TAMBIEN TU USUARIO.‼️ ")                        
                    print("\n\t ‼️  SI NO DESEAS CANCELAR TODO TU PEDIDO, ESCRIBE NO, ASI PODRAS CANCELAR SOLO CIERTOS PRODUCTOS.‼️")
                    resp=input("Deseas cancelar todo tu pedido? si/no: ").lower().strip()
                    while resp not in ["si", "no"]:
                        print("\t\t Selecciona una opción válida por favor.")
                        resp=input("Deseas cancelar todo tu pedido? si/no: ").lower().strip()
                    if resp=="si":
                        respp=input("¿Estas seguro de cancelar todo tu pedido? si/no: ").lower().strip()
                        while respp not in ["si", "no"]:
                            print("\t\t Selecciona una opción válida por favor.")
                            respp=input("¿Estás seguro de cancelar todo tu pedido? si/no: ").lower().strip()
                        if respp=="si":
                            respuesta=cafeteria.cancelarTodo(n_mesa)
                            if respuesta:
                                print(f"\n\t ✅.::Se borró la orden con exito::.✅ ")
                            else:
                                print(f"\n\t❌.::No fue posible borrar la orden en este momento, intentalo más tarde::.") 
                    elif resp=="no":
                        conf=input("Deseas solo cancelar ciertos productos de tu orden? si/no: "). lower().strip()
                        while conf not in ["si", "no"]:
                            print("\t\t Selecciona una opción válida por favor.")
                            conf=input("Deseas solo cancelar ciertos productos de tu orden? si/no: "). lower().strip()
                        funciones.borrarPantalla()
                        if conf=="si":
                            lista_cafeteria=cafeteria.mostrarPedido(n_mesa)
                            if len (lista_cafeteria)>0:
                                print(f"\n\t📝Mostrar tus pedidos")
                                print(f"{'|'}{'ID':<5}{'|'}{'producto':<25}{'|'}{'tipo':<15}{'|'}{'cantidad':<15}{'|'}{'tamaño':<15}{'|'}{'azucar':<15}{'|'}{'sabor':<15}{'|'}{'extra':<15}{'|'}{'numero de mesa':<15}{'|'}")
                                print(f"_"*150)
                                for fila in lista_cafeteria:
                                    print(f"{'|'}{fila[0]:<5}{'|'}{fila[1]:<25}{'|'}{fila[2]:<15}{'|'}{fila[3]:<15}{'|'}{fila[4]:<15}{'|'}{fila[5]:<15}{'|'}{fila[6]:<15}{'|'}{fila[7]:<15}{'|'}{fila[8]:<15}{'|'}")
                            id = input("\t \t ID de la orden a eliminar: ")
                            lista_cafeteria = cafeteria.mostrarPedido(n_mesa)
                            precio_viejo =0
                            precio=0
                            for fila in lista_cafeteria:
                                if str(fila[0]) == id:
                                    producto_viejo=fila[1]
                                    cantidad_vieja=int(fila[3])
                                    tamaño_viejo=fila[4]
                                    extra=fila[7]
                                    if producto_viejo in precios:
                                        if producto_viejo=="frappe":
                                            if isinstance(precios[producto_viejo], dict):
                                                precio_viejo=precios[producto_viejo][tamaño_viejo]* cantidad_vieja
                                                if extra=="si":
                                                    precio_viejo+=10*cantidad_vieja
                                        elif isinstance(precios[producto_viejo], dict):
                                            precio_viejo = precios[producto_viejo][tamaño_viejo] * cantidad_vieja
                                        else:
                                            precio_viejo = precios[producto_viejo] * cantidad_vieja
                                    break 
                            total_general = total_general - precio_viejo
                            cafeteria.actualizarTotalMesa(n_mesa, total_general, pago)
                            print(f"🧾Tu total:: {total_general}")
                            respuesta=cafeteria.cancelarPedido(id) 
                            if respuesta:
                                print(f"\n\t ✅.::Se borró la orden con exito::. ✅")
                            else:
                                print(f"\n\t❌.::No fue posible borrar la orden en este momento, intentalo más tarde::.") 
                    funciones.esperarTecla()  
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t ❌Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    




