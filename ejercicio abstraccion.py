class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

#Setters
    def asignarNombre(self,nombre):
        self.__nombre = nombre   

    def asignarCedula(self,cedula):
        self.__cedula = cedula

    def asignarGenero(self,genero):
        self.__genero = genero

# getters
    def verNombre(self):
        return self.__nombre

    def verCedula(self):
        return self.__cedula

    def verGenero(self):
        return self.__genero

class Paciente(Persona):
    def __init__(self):
        self.__servicio = ""
    
    def asignarServicio(self, servicio):
        self.__servicio = servicio

    def verServicio(self):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        self.__turno = ""

    def asignarTurno(self, turno):
        self.__turno = turno
    
    def verTurno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        self.__rango = ""

    def asignarRango(self, rango):
        self.__rango = rango

    def verRango(self):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        self.__especialidad = ""

    def asignarEspecialidad(self,especialidad):
        self.__especialidad = especialidad

    def verEspecialidad(self):
        return self.__especialidad


p1 = Paciente()
p2 = Paciente()
p1.asignarNombre("Juan")
p1.asignarCedula(1097873)
p1.asignarGenero("Hombre")
print(p1.verNombre())
#print(p1.verGenero())
#print(p1.verCedula())