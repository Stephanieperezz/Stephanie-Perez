
peliculas={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
   input("Presiona una tecla para continuar...")


def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar películas ")
    if len(peliculas)>0:
        for i in peliculas:
            print(f"{i}:{peliculas[i]}")
    else:
        print("NO HAY PELICULAS EN EL SISTEMA")

def borrarPeliculas():
    borrarPantalla()
    print("Borrar películas ")
    if len(peliculas)>0:
        resp=input("¿Deseas borrar o quitar la película? SI/NO: ").upper().strip()
        if resp=="SI":
            peliculas.clear()
    else:
        print("NO HAY PELICULAS EN EL SISTEMA")
        
def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t AGREGAR PELÍCULA")
    nombre = input("\n\t\t Ingresa el nombre de la película: ").strip()
    if nombre:
        peliculas.append(nombre)
        print(f"\n\t\t Película '{nombre}' agregada exitosamente.")
    else:
        print("\n\t\t No ingresaste un nombre válido.")

def modificarPeliculas():
    borrarPantalla()
    print("\n\t\t MODIFICAR PELÍCULA")
    if peliculas:
        for i, p in enumerate(peliculas, start=1):
            print(f"\t\t {i}. {p}")
        try:
            pos = int(input("\n\t\t Ingresa el número de la película a modificar: "))
            if 1 <= pos <= len(peliculas):
                nueva = input("\n\t\t Ingresa el nuevo nombre: ").strip()
                if nueva:
                    peliculas[pos - 1] = nueva
                    print("\n\t\t Película modificada correctamente.")
                else:
                    print("\n\t\t No ingresaste un nombre válido.")
            else:
                print("\n\t\t Número fuera de rango.")
        except:
            print("\n\t\t Entrada inválida.")
    else:
        print("\n\t\t No hay películas registradas.")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t\t BUSCAR PELÍCULA")
    nombre = input("\n\t\t Ingresa el nombre o parte del nombre a buscar: ").lower().strip()
    encontrados = [p for p in peliculas if nombre in p.lower()]
    if encontrados:
        print("\n\t\t Resultados encontrados:")
        for i, p in enumerate(encontrados, start=1):
            print(f"\t\t {i}. {p}")
    else:
        print("\n\t\t No se encontró ninguna coincidencia.")

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t\t LIMPIAR TODAS LAS PELÍCULAS")
    if peliculas:
        confirm = input("\n\t\t ¿Estás seguro/a? Esto eliminará todas las películas. (si/no): ").lower()
        if confirm == "si":
            peliculas.clear()
            print("\n\t\t Lista de películas vaciada.")
        else:
            print("\n\t\t Operación cancelada.")
    else:
        print("\n\t\t No hay películas que eliminar.")