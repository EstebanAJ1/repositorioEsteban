class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

#Setters
    def asignarNombre(self,rol):
        self.__nombre = input(f"Ingrese el nombre del {rol}: ")   

    def asignarCedula(self,rol):
        self.__cedula = input(f"Ingrese la cedula del {rol}: ")  

    def asignarGenero(self,rol):
        self.__genero = input(f"Ingrese el genero del {rol}: ")  

# getters
    def verNombre(self):
        return self.__nombre

    def verCedula(self):
        return self.__cedula

    def verGenero(self):
        return self.__genero

    def guardarInfo(self):
        return self.__nombre, self.__cedula, self.__genero

class Paciente(Persona):
    def __init__(self):
        super().__init__()
        # Persona.__init__(self)
        self.__servicio = ""
    
    def asignarServicio(self, rol):
        self.__servicio = input(f"Ingrese el servicio del {rol}: ")

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

class Sistema(Persona):
    def __init__(self):
        self.__lista_pacientes = []
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__diccionario_paciente = {}

    def numPacientes(self):
        self.__numero_pacientes = len(self.__lista_pacientes)
        return print(self.__numero_pacientes)

    def ingresarPaciente(self, rol):
        p = Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio(rol)
        self.__lista_pacientes.append(p.guardarInfo())
        self.__lista_nombre.append(p.verNombre())
        self.__lista_cedula.append(p.verCedula())
        self.__lista_genero.append(p.verGenero())
        self.__diccionario_paciente.update({"Nombre": self.__lista_nombre, "Cedula": self.__lista_cedula, "Genero": self.__lista_genero})
        #print(self.__lista_pacientes)
        #print(self.__diccionario_pacientes)
        #print(self.numPacientes())

    def verDatosPacientesLista(self):
        cedula = str(input("Ingresar la cedula del paciente que busca en la lista: "))
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)

    def verDatosPacientesDiccionario(self):
        cedula = (input("Ingresar la cedula del paciente que busca en el diccionario: "))
        for p, c in enumerate(self.__diccionario_paciente["Cedula"]):
            if cedula == c:
                print(self.__diccionario_paciente)
                print(p,c)
                print(f"Nombre: {self.__diccionario_paciente['Nombre'][p]} ")

def main():
    p = Sistema()

    while True:
        opcion = int(input('''
        - 1. Ingresar paciente 
        - 2. Ver datos del paciente
        - 3. ver el numero de pacientes
        - 4. Salir
        > '''))
        if opcion == 1:
            p.ingresarPaciente("Paciente")

        elif opcion == 2:
            p.verDatosPacientesDiccionario()
            #p.verDatosPacientesLista()

        elif opcion == 3:
            p.numPacientes()

        elif opcion == 4:
            break

# main()
if __name__ == '__main__':
    main()