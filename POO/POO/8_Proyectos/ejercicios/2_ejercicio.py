#numero1=input("Num 1: ")
#numero2=input("Num 2: ")

#class Calculadora():
#    def __init__(self, numero1, numero2):
#        self._numero1=numero1
#        self._numero2=numero2
#    def numero1(self):
#        return self._numero1
#    def numero2(self):
#        return self._numero2
#    def suma():
#        numero3=numero1+numero2
#        return numero3
#    def multiplicacion(self):
#        numero3=numero1*numero2
#        return numero3
#    def resta():
#        numero3=numero1-numero2
#        return numero3
#    def division():
#        numero3=numero1/numero2
#        return numero3
    
#operacion=Calculadora(numero1, numero2)
#print(f"La división es: {operacion.division} ")



class Calculadora:
    def __init__(self):
        self._numero1=int(input("Numero 1: "))
        self._numero2=int(input("Numero 2: "))

    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self,numero1):
        self._numero1=numero1

    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self,numero2):
        self._numero2=numero2

    def sumar(self):
        suma=self._numero1+self._numero2
        return suma
    
    def restar(self):
        resta=self._numero1-self._numero2
        return resta
    
    def multiplicar(self):
        multiplicacion=self._numero1*self._numero2
        return multiplicacion
    
    def dividir(self):
        division=self._numero1/self._numero2
        return division
    
operacion=Calculadora()
print(f"{operacion.numero1} + {operacion.numero2}  {operacion.sumar()}")
print(f"{operacion.numero1} - {operacion.numero2}  {operacion.restar()}")
print(f"{operacion.numero1} * {operacion.numero2}  {operacion.multiplicar()}")
print(f"{operacion.numero1} / {operacion.numero2}  {operacion.dividir()}")