import agenda


def main():
    age_con={}
    opcion=True
    
    while opcion:
        agenda.borrarPantalla() 
        opcion=agenda.main_principal()
        
        match opcion:
            case "1":
                    agenda.agregar_contacto(age_con)
                    agenda.borrarPantalla()
            case "2":
                    agenda.buscar_contacto(age_con)
                    agenda.borrarPantalla()
            case "3":
                    agenda.mostrar_contacto(age_con)
                    agenda.borrarPantalla()
            case "4":
                    agenda.modificar_contacto(age_con)
                    agenda.borrarPantalla()
            case "5":
                    agenda.eliminar_contacto(age_con)
                    agenda.borrarPantalla()
            case _:
                    agenda.borrarPantalla()

if __name__ == "__main__":
    main()
        