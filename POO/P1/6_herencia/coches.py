##A ESTO TMBN SE LE VA A AGREGAR ALGO MAS PERO NO SE Q 

import os
os.system("cls")

class Coches:
    """Método constructor, con este método se inicializa un objeto cuando es creado con valores iniciales"""
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca=""
        self._color=""
        self._modelo=""
        self._velocidad=0
        self._caballaje=0
        self._plazas=0
    


    #PRIMER FORMS DE CREAR
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
       self._marca=marca

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
       self._color=color

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
       self._modelo=modelo

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
       self._velocidad=velocidad

    @property
    def caballaje(self):
        return self._caballaje
    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje=caballaje

    @property
    def plazas(self):
        return self._plazas
    @plazas.setter
    def plazas(self, plazas):
        self._plazas=plazas

    def acelerar(self):
        return "El coche está acelerando"

    def frenar(self):
        return "El coche está frenando" 

class Camiones(Coches):
        def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad_carga):
            super().__init__(marca, color, modelo, velocidad, caballaje, plazas) #Cuando son más de una clase hay q quitar el super y poner el nombre de la clase
            self.__eje=eje
            self.__capacidad_carga=capacidad_carga

        #Métodos set y get
        @property
        def eje(self):##Unica manera de acceder cuando es priv
            return self._eje
        @eje.setter
        def eje(self,eje):
            self._eje=eje
        
        @property
        def capacidad_carga(self):##Unica manera de acceder cuando es priv
            return self._capacidad_carga
        @capacidad_carga.setter
        def capacidad_carga(self,capacidad_carga):
            self._capacidad_carga=capacidad_carga

        def cargar(self, tipo_carga):
            self._tipo_carga=tipo_carga
            return self._tipo_carga

class Camionetas(Coches):
        def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
            super().__init__(marca, color, modelo, velocidad, caballaje, plazas) #Cuando son más de una clase hay q quitar el super y poner el nombre de la clase
            self._traccion=traccion
            self._cerrada=cerrada

        #Métodos set y get
        @property
        def traccion(self):##Unica manera de acceder cuando es priv
            return self._traccion
        @traccion.setter
        def traccion(self,traccion):
            self._traccion=traccion
        
        @property
        def cerrada(self):##Unica manera de acceder cuando es priv
            return self._cerrada
        @cerrada.setter
        def cerrada(self,cerrada):
            self._cerrada=cerrada

        def transportar(self, num_pasajeros):
            self.__num_pasajeros=num_pasajeros
            return self.__num_pasajeros


