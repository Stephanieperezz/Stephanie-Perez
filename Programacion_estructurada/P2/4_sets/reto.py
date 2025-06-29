"""CREAR UN PROGRAMA QUE SOLICITE LOS EMAIL DE ALUMNOS DE UTD. ALMACENAR EN UNA LISTA
Y POSTERIORMENTE MOSTRAR EN LA PANTALLA, LOS EMAIL SIN DUPLICADOS"""

##SOLUCION 2
respuesta="SI"
emails=[]
while respuesta=="SI":
    emails.append(input("AGREGAR EMAIL: "))
    respuesta=input("Desea agregar otro email? SI/NO: ").upper()
    
print (emails)
emails_set=set(emails)##QUITO LOS DUPLICADOS
print(emails_set)
