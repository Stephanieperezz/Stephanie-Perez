class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_matricula(self):
        return self.__matricula
    def inscribirse (self):
        return "Estoy inscrito"
    def estudiar (self):
        pass

Alumno2=Alumnos("Alondra", 19, 31412402)
Alumno1 = Alumnos("Stephanie", 18, 31412401)
print(f"Los valores de Alumno 1 son: {Alumno1.get_nombre()}, {Alumno1.get_edad()}, {Alumno1.get_matricula()}")
print(Alumno1.inscribirse())
print(f"Los valores de Alumno 2 son: {Alumno2.get_nombre()}, {Alumno2.get_edad()}, {Alumno2.get_matricula()}")
print(Alumno2.inscribirse())

class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
    def get_nombre(self):
        return self.__nombre
    def get_codigo(self):
        return self.__codigo
    def get_creditos(self):
        return self.__creditos
    def asignar():
        pass

Curso1=Cursos("Matematicas", 1234, 12)
Curso2=Cursos("Programacion", 4321, 20)
print(f"Los valores de curso 1 son: {Curso1.get_nombre()}, {Curso1.get_codigo()}, {Curso1.get_creditos()}")
print(f"Los valores de curso 2 son: {Curso2.get_nombre()}, {Curso2.get_codigo()}, {Curso2.get_creditos()}")

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
    def get_nombre(self):
        return self.__nombre
    def get_experiencia(self):
        return self.__experiencia
    def get_num_profesor(self):
        return self.__num_profesor
    def impartir(self):
        pass
    def evaluar(self):
        pass
    
Profesor1=Profesores("Dagoberto", 13, 30412401)
Profesor2=Profesores("Omar", 15, 30412402)
print(f"Los valores de profesor 1 son: {Profesor1.get_nombre()}, {Profesor1.get_experiencia()}, {Profesor1.get_num_profesor()}")
print(f"Los valores de profesor 2 son: {Profesor2.get_nombre()}, {Profesor2.get_experiencia()}, {Profesor2.get_num_profesor()}")