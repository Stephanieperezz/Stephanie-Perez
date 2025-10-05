""" EJERCICIO: #PRACTICA 2 MODELAR Y DIAGRAMAR EN POO"""
import os
os.system("cls")
"""Lo que esta comentado # NO ES UN BUENA PRACTICA Y SOLO ES CUANDO LA CLASE ESTA EN PUBLICO"""
#PROTEGIDO ES Q SI SE QUIERE IMPRIMIR DENTRO DEL COCHE1._COLOR, SI DEJA MOSTRAR EL VALOR TANTO EN PUBLIOC COMO PROTEGIDO PERO NO ES UNA UENA PRACTICA LO DE POTEGIFO


class Coches:
    #color="Blanco"
    #marca="Toyota"
    #velocidad=220
    #METODO CONSTRUCTOR QUE INICIALIZA LOS VALORES CUANDO SE INSTANCIA UN OBJETO DE LA CLASE
    ##Atributos del objeto
    ##VENTAJAS: 
      #SE HACE GLOBAL Y SE PUEDE USAR EN LOS METODOS DENTRO DE CLASE
      # 
      #        
    def __init__(self, color, marca, velocidad): ##EN LUGAR DE SELF SE PUEDE USAR CUALQUIER OTRA PALABRA
       self.__color=color
       self.__marca=marca
       self.__velocidad=velocidad  #__ ES PARA HACERLO PRIVADO, _ ES PROTEGIDO 

    ##Metodos del objeto
    def acelerar(self, incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
    def frenar(self, decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    def tocar_claxon(self):
        print("PIIIIIII")

##Instanciar o crear objetos en la clase Coches
#coche1=Coches()
#coche1.marca#PARA QUE SE LE ASIGNE EL VALOR
#print(coche1.marca)##Imprimirlo

#coche2=Coches()
#coche2.marca
#print(coche2.marca)

coche1=Coches("Blanco", "Toyota", 220)
coche2=Coches("Rojo", "Honda", 180)
print(coche1.acelerar(50))
print(coche2.frenar(100))
print(coche1.tocar_claxon())


##ESTO ES ANTES DE HACERLOS PRIVADOS
#220 a 270 180 a 80
#coche1=Coches("Blanco", "Toyota", 220)
#coche2=Coches("Rojo", "Honda", 180)
print(f"Los valores del objeto 1 son: {coche1.__marca},{coche1.__color},{coche1.__velocidad}")
#print(f"El coche 1 acelero de {coche1.__velocidad} a {coche1.acelerar(50)}")
#print(f"Los valores del objeto 2 son: {coche2.__marca},{coche2.__color},{coche2.__velocidad}")
#print(f"El coche 2 freno de {coche2.velocidad} a {coche2.frenar(100)}")