from PyQt5 import QtWidgets
import sys
import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

from modelo import Sistema,client
from vista import Ventana
from vista2 import Ventana2


class comunicacion(object):
    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__view = Ventana()
        self.__view2 = Ventana2()
        self.system = Sistema()
        self.controller = ctrl(self.__vista, self.system)
        self.controller2 = ctrl(self.__vista2, self.system)
        self.__view.conexionconelcontrolador(self.controller)
        self.__view2.conexionconelcontrolador(self.controller2)


    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec_())

class ctrl(object):
    def __init__(self,view,system):
        self.__view = view
        self.system = system

    def agregarPaciente(self,cedula,nombre,edad):
        self.system.nombre(cedula,nombre)
        self.system.cedula(cedula)
        self.system.edad(cedula,edad)
        
    def buscarEnSistema(self,cedula):
        nombre = self.system.verificar_db(cedula)
        if nombre != None:
            self.__view.rellenar_datos(nombre)
        else:
            print(">>> El paciente no exixte <<<")

def validarNum(msj):
    while True:
        try:
            a = int(input(msj))
            return a 
        except ValueError:
            print(">>> INGRESE UN VALOR NUMERICO <<<")

if __name__ == "__main__":
    controller = comunicacion()
    controller.main()


