import peliculas
opcion=True
"""NOTAS.- 
1-Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre, categoría, clasificación, género, idioma) de pelícukas"""

while opcion:
    peliculas.borrarPantalla()
    print (
    "\n\t\t 1. Crear películas " 
    "\n\t\t 2. Borrar películas " 
    "\n\t\t 3. Mostrar películas " 
    "\n\t\t 4. Buscar películas " 
    "\n\t\t 5. Modificar películas"
    "\n\t\t 6. Salir" )
    opcion=input("\n\t\t Elige el número de la opción que deseas realizar: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
        case"2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case"3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case"4":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case"5":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "6":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\t\tTerminaste la ejecución del sistema...Gracias...")
        case _:
            opcion=True
            peliculas.espereTecla()
            print("\n\t Opción inválida, vuelva a intentarlo")
