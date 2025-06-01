##EJEMPLO 1 CREAR UNA LISTA DE NUMEROS E IMPRIMIR EL CONTENIDO

numeros=[1,2,3,4,5,6,7,8,9]
print (numeros)

lista="["
for i in numeros:
    lista+=f"{i},"
print(f"{lista}]")

##EJEMPLO 2 CREAR UNA LISTA DE PALABRAS Y POSTERIORMENTE BUSCAR LA COINCIDENCIA DE UNA PALABRA

palabras=["hola","Stephanie", "programacion"]

buscar=input("dame la palabra a buscar: ")

if buscar in palabras:
    print("si se encontró en la lista ")
else:
    print("No se encontró la palabra ")


encontro=False
for i in palabras:
    if i==buscar:
        encontro==True
        if encontro:
         print("si se encontró en la lista")
        else:   
            print("no se encontró en la lista")


palabra=buscar in palabras
print(palabra)

##EJEMPLO 3 AÑADIR ELEMENTOS A LA LISTA
numeros=[]
opc=input("deseas agregar otro numero a la lista? SI/NO").upper()

while opc=="SI":
    numero_add=float(input("Dame el numero que deseas agregar: "))
    numeros.append(numero_add)
    opc=input("Desea agregar otro numero? SI/NO").upper()
print (numeros)
    
numeros.append(10)
print (numeros)

##EJEMPLO 4 CREAR UNA LISTA MULTIDIMENSIONAL QUE PERMITA ALMACENAR EL NOMBRE Y EL TELEFONO DE UNA AGENDA



