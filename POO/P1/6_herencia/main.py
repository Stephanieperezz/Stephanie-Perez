#Instanciar objetos para posterior implementarlos


from coches import Coches, Camionetas, Camiones

coche=Coches("VW", "Blanco", "2020", 220, 200, 5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Nisssan", "Amarillo", "2025", 180, 200, 4, "trasera", False)
print(camioneta.marca, coche.acelerar())

camion=Camiones("Volvo", "Blanco", "2025", 180, 200, 4, 2, 300)

#num_coches=int(input("¿Cuántos coches deseas?"))

#for i in range (0, num_coches):
    #print(f"\n\t ....datos del coche.... "(i+1))
    #marca=input("Ingresa la marca").upper()
    #color=input("Ingresa el color").upper()
    #modelo=input("Ingresa el modelo").upper()
    #velocidad=int(input("Ingresa la velocidad")).upper()
    #potencia=int(input("Ingresa la potencia")).upper()
    #plazas=int(input("Ingresa las plazas")).upper()

#coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

#coche1=Coches("VW","Blanco","2022",220,150,5, "HSGDG")
#coche2=Coches("Nissan","Azul","2020",180,150,6)
#coche3=Coches("Honda")


#print(f"Los valores del objeto 1 son: {coche1.getMarca},{coche1.getColor}, {coche1.getModelo}, {coche1.getVelocidad}, {coche1.getCaballaje}, {coche1.plazas}")
#print(f"coche 3 marca: {coche3.marca}")
#print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")'''