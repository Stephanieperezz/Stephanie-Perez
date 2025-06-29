
peliculas={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
   input("Presiona una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("Crear películas ")
    peliculas.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    peliculas.update({"clasificacion":input("Ingrese la clasificacion: ").upper().strip()})
    peliculas.update({"genero":input ("Ingresa el género: ").upper().strip()})
    peliculas.update({"categoría": input("Ingrese la categoría: ").upper().strip()})
    print ("LA OPERACION SE REALIZÓ CON ÉXITO")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar películas ")
    if len(peliculas)>0:
        for i in peliculas:
            print(f"{i}:{peliculas[i]}")
    else:
        print("NO HAY PELICULAS EN EL SISTEMA")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("Agregar una característica de película ")
    atributo=input("Ingresa el nombre de la nueva característica que deseas agregar: ").upper().strip()
    valor_atributo=input("Ingresa el valor de la nueva característica que deseas agregar: ").upper().strip()
    peliculas.update({atributo:valor_atributo})
    print("TODO SE REALIZÓ CON ÉXITO")


def borrarPeliculas():
    borrarPantalla()
    print("Borrar películas ")
    if len(peliculas)>0:
        resp=input("¿Deseas borrar o quitar la película? SI/NO: ").upper().strip()
        if resp=="SI":
            peliculas.clear()
    else:
        print("NO HAY PELICULAS EN EL SISTEMA")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("Modificar característica de películas ")
    if len (peliculas)>0:
        for i in peliculas:
            print(f"{i}:{peliculas[i]}")
            resp=input(f"¿Desea modificar el valor de {i}? SI/NO: ").upper().strip()
            if resp=="SI":
                nuevo_valor = input("Ingresa actualización: ").upper().strip()
                peliculas.update({i: nuevo_valor})
                print("OPERACION REALIZADA CON ÉXITO")
    else:
        print("NO HAY PELICULAS EN EL SISTEMA")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("Borrar característica de películas ")
    for i in peliculas:
        print("\n\t\t valores actuales:")
        print(f"\n\t\t {i}:{peliculas[i]}")
    resp=input("Desea borrar alguna característica? SI/NO").upper() .strip()
    if resp=="SI":
        cat=input("Ingrese la característica que deseas borrar o quitar ").upper().strip()
        espereTecla()
        if cat in peliculas:
            del peliculas[cat]
            print("LA OPERACION SE REALIZO CON EXITO")
        else: 
            print("Esta característica no existe")

