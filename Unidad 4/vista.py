from PyQt5 import QtWidgets, uic

class Ventana(QtWidgets.QMainWindow):
    '''Clase principal'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("menu_ingreso.ui",self)

        self.verificar.clicked.connect(self.verificar_dato)
        self.agregar.clicked.connect(self.agregar_dato)
        self.salir.clicked.connect(self.cerrar)
        self.continuar.setEnabled(False)
        self.continuar.clicked.connect(self.continuar_dato)

    def conexionconelcontrolador(self,control):
        self.mi_controlador = control

    def verificar_dato(self):
        self.mi_controlador.buscarEnSistema(self.input_cedula.text())

    def rellenar_dato(self,nombre,edad,deporte,ruta):
        self.verificar.setEnabled(False)
        self.input_nombre.setText(nombre)
        self.input_edad.setText(str(edad))
        self.input_deporte.setText(deporte)
        self.input_ruta.setText(ruta)

    def agregar_dato(self):
        self.mi_controlador.agregarPaciente(self.input_cedula.text(),self.input_nombre.text(),self.input_edad.text(),self.input_deporte.text(),self.input_ruta.text())
        self.agregar.setEnabled(False)
        self.continuar.setEnabled(True)

    def cerrar(self):
        self.close()

    def continuar_dato(self):
        print("menu_grafica")