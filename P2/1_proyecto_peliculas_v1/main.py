"""
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menú de opciones- Agregar, borrar, modificar, 
mostrar, buscar, limpiar una lista de películas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo(módulo)
2.- Utilizar listas para almacenar los nombres de películas
"""

import peliculas
opcion=True


while opcion:
    peliculas.borrarPantalla()
    print ("\n\t\t\t GESTION DE PELICULAS. \n\t\t 1. Agregar \n\t\t 2. Borrar \n\t\t 3. Modificar \n\t\t 4. Mostrar \n\t\t 5. Buscar \n\t\t 6. Limpiar \n\t\t 7. Salir ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case"3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case"4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case"5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case"6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case"7":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\t Terminaste la ejecución del sistema GRACIAS ")
        case _:
            print("\n\t Opción inválida, vuelva a intentarlo")


