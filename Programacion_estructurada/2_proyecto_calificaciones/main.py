import calificaciones

def main():
    guardar=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(guardar)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(guardar)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(guardar)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscar_calificaciones(guardar)
                calificaciones.esperarTecla() 
            case "5":
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\t`\u2705Terminaste la ejecucion")
            case _:
                calificaciones.borrarPantalla()
                print("\n\tOpción invalida vuelva a intentarlo ... por favor")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()