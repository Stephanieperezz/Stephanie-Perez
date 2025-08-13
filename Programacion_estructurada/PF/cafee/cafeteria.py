from conexionBD import *
from datetime import datetime

def realizarPedido( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa):
        try:
            cursor.execute("insert into pedidos ( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, fecha)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, datetime.now()))
            conexion.commit()
            return True
        except:
            print ("Error al realizar el pedido")
            return False

def modificarAlimento(id, producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa):
    try: 
        cursor.execute("update pedidos set producto=%s, tipo=%s, cantidad=%s, tamaño=%s, azucar=%s, sabor=%s, extra=%s, n_mesa=%s, fecha=%s where id=%s",(producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, datetime.now(), id))
        conexion.commit()
        return True
    except:
        print ("Error al modificar el pedido")
        return False
    
def mostrarPedido(n_mesa):
    try:
        cursor.execute("select * from pedidos where n_mesa=%s",(n_mesa,))
        #registros=cursor.fetchall()
        return cursor.fetchall()  
        #if len (registros)>0:
            #return registros
        #else:
            #return []
    except:
        return []
    
def mostrarTotal(n_mesa):
    try:
        cursor.execute("select total from total_mesa where n_mesa=%s", (n_mesa,))
        resultado= cursor.fetchone()
        if resultado:
            return float(resultado[0])
        else:
            return 0
    except:
        return 0

def mostrarCancelados():
    try:
        cursor.execute("select * from cancelados ")
        return cursor.fetchall()
    except:
        return []
    
def mostrarOrdenes():
    try:
        cursor.execute("select * from pedidos ")
        return cursor.fetchall()
    except:
        return []

def cancelarPedido(id):
    try: 
        cursor.execute("select * from pedidos where id = %s", (id,))
        pedido=cursor.fetchone()
        cursor.execute("insert into cancelados (producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, fecha) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], pedido[6], pedido[7], pedido[8], datetime.now()))
        cursor.execute("delete from pedidos where id=%s", (id,))
        conexion.commit()
        return True 
    except:
        print ("Error al cancelar el pedido")
        return False
    
def cancelarTodo(n_mesa):
    try:
        cursor.execute("select * from pedidos where n_mesa = %s", (n_mesa,))
        pedidos=cursor.fetchall()
        for pedido in pedidos:
            cursor.execute("insert into cancelados (producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, fecha) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], pedido[6], pedido[7], pedido[8], datetime.now()))
        cursor.execute("delete from pedidos where n_mesa = %s", (n_mesa,))
        conexion.commit()
        cursor.execute("delete from total_mesa where n_mesa=%s", (n_mesa,))
        conexion.commit()
        cursor.execute ("delete from usuarios where n_mesa=%s", (n_mesa,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al cancelar pedido: {e}")
        return False
    
def borrarRegistros():
    try:
        cursor.execute ("delete from cancelados")
        cursor.execute ("delete from pedidos")
        cursor.execute ("delete from total_mesa")
        cursor.execute ("delete from usuarios")
        conexion.commit()
        return True
    except:
        print ("Hubo un error y no se eliminaron los registros, intenta más tarde.")
        return False
    
def modificarBebidas(id, producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa):
    try: 
        cursor.execute("delete from pedidos where id=%s",(id,))
        conexion.commit()
        cursor.execute("insert into pedidos ( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, fecha)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( producto, tipo, cantidad, tamaño, azucar, sabor, extra, n_mesa, datetime.now()))
        conexion.commit()
        return True
    except:
        print ("Error al realizar el pedido")
        return False

def obtenerTotalMesa(n_mesa):
    cursor.execute("select total from total_mesa where n_mesa = %s", (n_mesa,))
    fila = cursor.fetchone()
    if fila:
        return fila[0] 
    else:
        return 0

def actualizarTotalMesa(n_mesa, total, pago):
    cursor.execute("select total from total_mesa where n_mesa = %s", (n_mesa,))
    fila = cursor.fetchone()
    if fila:
        cursor.execute("update total_mesa set total = %s where n_mesa = %s", (total, n_mesa))
    else:
        cursor.execute("insert into total_mesa (n_mesa, pago, total) values (%s, %s, %s)", (n_mesa, pago, total))
    conexion.commit()

def mostrarpers():
    try:
        cursor.execute("select * from total_mesa")
        return cursor.fetchall()
    except:
        return False

def eliminarOrden(n_mesa):
    try:
        cursor.execute ("delete from pedidos where n_mesa=%s", (n_mesa,))
        conexion.commit()
        cursor.execute ("delete from total_mesa where n_mesa=%s", (n_mesa,))
        conexion.commit()
        cursor.execute ("delete from usuarios where n_mesa=%s", (n_mesa,))
        conexion.commit()
        return True
    except:
        return False

def Nmesa():
    try:
        cursor.execute("select * from usuarios")
        return cursor.fetchall()
    except:
        return []

