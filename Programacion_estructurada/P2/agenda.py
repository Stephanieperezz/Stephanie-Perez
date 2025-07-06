#####AGREGARLO A GITHUB PERO YA CON ICONOS  
"""AGENDA_CONTACTOS={
            "STEPHANIE": "6188045696": stephanie@GMAIL.COM
            "ALONDRA": "6188045696": alondra@GMAIL.COM
            "DAGOBERTO": "6188045696": dago@GMAIL.COM
                    }"""
 
def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(".::Presione ENTER para continuar::.")

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t👤.::Agregar contactos::.👤")
    nombre=input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t ❌Este contacto ya existe")
    else:                                      
        tel=input("Telefono: ").upper().strip()
        email=input("Email: ").lower().strip()
        agenda[nombre]={tel, email}
        print("\n\t\t✅.::Acción realizada con éxito::.") 

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t 👤.::Mostrar contactos::.")
    if not agenda:
        print("\n\t❌No hay contactos registrados")
    else:
        print(f"{'Nombre':<15}{'# Teléfono':<15}{'E-mail':<10}")
        print(f"-"*60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<10}")
            print(f"-"*60) 

def eliminar_contacto(agenda):
    borrarPantalla()
    print("eliminar un contacto")
    if not agenda:
        print("❌No hay contactos")
    else:
        nombre=input("Ingresa el nombre del contacto que deseas eliminar: ")
        espereTecla()
        if nombre in agenda:
            agenda.pop(nombre) ##pop elimina el atributo
            print("✅LA OPERACION SE REALIZO CON EXITO") 
        else:
            print("❌Este nombre no está en la agenda. ")

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔍Buscar contactos ")
    if len (agenda)>0:
        nombre=input("Ingrese el nombre del contacto que deseas buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'# Teléfono':<15}{'E-mail':<10}")
            print(f"{'Nombre':<15}{agenda[nombre][0]:<15}{'E-mail':<10}") 
            ##{agenda} es traer al diccionario [contacto] es el atributo [0] es la posicion del diccionario
            print(f"-"*60)
        else:
            print("❌Este contacto no se encuentra en agenda ")
    else:
        print("❌No hay contactos en la agenda")

def modificar_contacto(agenda):
    borrarPantalla()
    print("👤Modificar contactos ")
    if not agenda: ##SI NO HAY ALGO EN AGENDA
        print ("❌No hay contactos en la agenda. ")
    else:
        nombre=input("Ingrese el nombre del contacto que deseas buscar: ").upper().strip()
        if nombre in agenda:
            print(f"Nombre: {nombre}\n Telefono: {agenda[nombre][0]}\n E-mail: {agenda[nombre][1]}")
            resp=input("¿Desea cambiar los valores? si/no: ").lower().strip()
            if resp=="si":
                tel=input("Telefono: ").upper().strip()
                email=input("Email: ").lower().strip()
                agenda[nombre]={tel, email}
        else:
            print("❌Este contacto no existe. ")


