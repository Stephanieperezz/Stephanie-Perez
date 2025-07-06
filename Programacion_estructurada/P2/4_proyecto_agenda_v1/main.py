import agenda
opcion = True
agenda_contactos={}
while opcion:
    agenda.borrarPantalla()
    print("\n\t\t\t\t\t🧾.::: SISTEMA DE GESTIÓN DE AGENDA DE CONTACTOS:::.🧾")
    print("\t\t\t\t\t 1️⃣ Agregar contacto")
    print("\t\t\t\t\t 2️⃣ Mostrar todos los contactos")
    print("\t\t\t\t\t 3️⃣ Buscar contacto por nombre")
    print("\t\t\t\t\t 4️⃣ Eliminar contacto" )
    print("\t\t\t\t\t 5️⃣ Modificar contacto" )
    print("\t\t\t\t\t 6️⃣ Salir" )
    
    opcion = input("\n\t\t\t\t\t👉 Elige una opción (1-6): ").strip()

    match opcion:
        case "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.espereTecla()
        case "2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.espereTecla()
        case"3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.espereTecla()
        case"4":
            agenda.eliminar_contacto(agenda_contactos)
            agenda.espereTecla()
        case"5":
            agenda.modificar_contacto(agenda_contactos)
            agenda.espereTecla()
        case"6":
            opcion=False
            agenda.borrarPantalla()
            print("\n\t Terminaste la ejecución del sistema GRACIAS ")
        case _:
            print("\n\t Opcion no válida. Intenta de nuevo. ")
