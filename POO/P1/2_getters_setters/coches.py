
###A ESTE LE FALTA 

import os
os.system("cls")
class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Crear  los métodos setters y getters, estos métodos son importantes y necesarios en todas las clases para que el programador interactúe
    #con los valores de los atributos y a través de estos métodos; Digamos que es la manera mas adecuada y recomendable para solicitar un valor 
    #(get) y/o para ingresar o cambiar un valor (set) a un atributo en un particular de la clase a traves de un objeto.

    #En teoría se debería de crear un método getter y setter para cada atributo que contenga la clase
    #Los métodos get siempre regresar valor, es decir, el valor de la propiedad a través de un return
    #Por otro lado el metodo set siempre recibe parémetros para cambiar o modificar el valor del atributo o propiedad en cuestión 
    #Métodos, acciones o funciones que hace el objeto 

    #PRIMER FORMS DE CREAR
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
       self.__marca=marca

    def getColor(self):
        return self.color
    
    def setColor(self, color):
       self.__color=color

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
       self.__modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
       self.__velocidad=velocidad

    def getCaballaje(self):
        return self.caballaje
    
    def setCaballaje(self, caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.plazas

    def setPlazas(self, plazas):
        self.__plazas=plazas

    def acelerar(self):
      pass

    def frenar(self):
      pass  

    #Fin definir clase

    #Crear un objetos o instanciar la clase

coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2022")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#SEGUNDA FORMA 
