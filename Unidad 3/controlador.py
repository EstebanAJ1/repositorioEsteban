from PyQt5 import QtWidgets
import sys

from modelo import Sistema,client

from vista import Ventana

class comunicacion(object):
    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__view = Ventana()
        self.system = Sistema()
        self.controller = ctrl(self.__vista, self.system)
        self.__view.conexionconelcontrolador(self.controller)


    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec_())

class ctrl(object):
    def __init__(self,view,system):
        self.__view = view
        self.system = system

    def agregarPaciente(self,cedula,nombre):
        self.system.nombre(cedula,nombre)
        self.system.cedula(cedula)
        
    def buscarEnSistema(self,cedula):
        nombre = self.system.verificar_db(cedula)
        if nombre != None:
            self.__view.rellenar_datos(nombre)
        else:
            print(">>> El paciente no exixte <<<")

if __name__ == "__main__":
    controller = comunicacion()
    controller.main()