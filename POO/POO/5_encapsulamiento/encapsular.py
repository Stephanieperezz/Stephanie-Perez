##Encapsular: Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos 
# y métodos de una clase a la hora de usar un objeto o una herencia.
#Error

import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo público"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__ (self, color, tamanio):
        self.__color=color
        self.__tamanio=tamanio

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio=tamanio 

    @property
    def atributopublico(self):
        return self.atributo_publico
    
    @atributopublico.setter
    def atributopublico (self, atributo_publico):
        self.atributo_publico=atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    
    @atributo_protegido.setter
    def atributo_protegido (self, atributo_protegido):
        self._atributo_protegido=atributo_protegido
    
    @property
    def atributo_privado(self):
        return self.__atributo_privado
    
    @atributo_privado.setter
    def atributo_privado (self, atributo_privado):
        self.__atributo_privado=atributo_privado

    def getAtributoPrivado(self):
        return self.__atributo_privado


#Utilizar la clase

objeto=Clase("Rojo", "Grande")
#print(objeto.atributo_publico)________NO ES UNA BUENA PRÁCTICA ACCEDER A LOS VLORES DIRECTAMENTE.
#print(objeto._atributo_protegido)
print(objeto.atributo_privado)
print(objeto.atributopublico)
print(objeto.atributo_protegido)
objeto.color="morilla"
print(objeto)
print(objeto.color)