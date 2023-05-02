import numpy as np
import cv2
import scipy.io as sio
import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sns


class Sistema():
    def __init__(self,client):
        mydb = client["Hospital"]
        self.__neurologia = mydb["Neurología"]
    
    def ingresarCedula(self,cedula):
        ced = self.__neurologia.insert_one({"Cedula":cedula})

    def ingresarPaciente(self,cedula,nombre,edad,ruta):
        myquery = {"Cedula":cedula}
        newvalues = {"$set": {"Nombre":nombre, "Edad":edad,"Ruta":ruta}}
        self.__neurologia.update_one(myquery,newvalues)
        

    def tamañoSeñal(self):
        cedula = validarNum("-- Ingrese la cedula del paciente: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return 
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"]
        print("-- La señal tiene dimensión: ",señal.ndim ,", y tamaño: ",señal.shape)

    def graficaContinua(self):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"] 
        sensores = señal.shape[0] 
        puntos = señal.shape[1] 
        epocas = señal.shape[2] 

        señal_continua = np.reshape(señal,(sensores,puntos*epocas), order="F")
        #print(señal_continua.shape)

        plt.subplots()
        plt.plot(señal[0,:,0])

        plt.subplot() 
        plt.plot(señal_continua[0,0:1999]) 

        plt.show() 

    def graficarEpocas(self): # (8,2000,176)
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"]  
        # Seleccionar la primera época de señal
        epoch = señal[0]
        # Crear un arreglo de tiempo
        time = np.arange(len(epoch)) / 176  # Divido entre el numero de epocas
        # Graficar la señal
        plt.plot(time, epoch)
        plt.title('Señal de epocas de EEG')
        # Mostrar la figura
        plt.show()

    def guardarGraficaContinua(self):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"] 
        sensores = señal.shape[0] 
        puntos = señal.shape[1] 
        epocas = señal.shape[2] 

        señal_continua = np.reshape(señal,(sensores,puntos*epocas), order="F")

        plt.subplots()
        plt.plot(señal[0,:,0])

        plt.subplot() 
        plt.plot(señal_continua[0,0:1999],color="purple") 

        rut = r"C:\Users\Alvarez Jaramillo\Desktop\Esteban\Info 2\Señal_EEG.png"
        plt.savefig(rut)
        plt.show() 
        myquery = {"Cedula":cedula}
        newvalues = {"$set": {"Señal":rut}}
        self.__neurologia.update_one(myquery,newvalues)

    def dfContinua(self):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return False
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"] 
        sensores = señal.shape[0] 
        puntos = señal.shape[1] 
        epocas = señal.shape[2] 
        señal_continua = np.reshape(señal,(sensores,puntos*epocas), order="F")

        dataframeC = pd.DataFrame(señal_continua)
        promedio = dataframeC.mean(axis=1)
        return promedio
                
        
    def dfEpocas(self):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return 
        ruta = paciente["Ruta"]
        cdata = sio.loadmat(ruta)
        señal = cdata["data"]  
        return señal

    def validarCedula(self):
        while True:
            ced = validarNum("-- Ingrese la cedula del paciente: ")
            paciente = self.__neurologia.find_one({"Cedula": ced})
            if paciente == None:
                return ced
            else:
                print(">>> YA ESTA REGISTRADA ESTA CEDULA <<<")
                continue

    def guardarImagen(self,rut):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return
        myquery = {"Cedula":cedula}
        newvalues = {"$set": {"Imagen de calor":rut}}
        self.__neurologia.update_one(myquery,newvalues)

    def imagenByN(self, rut):
        cedula = validarNum("-- Ingrese la cedula del paciente a buscar: ")
        paciente = self.__neurologia.find_one({"Cedula": cedula})
        if paciente == None:
            print(">>> PACIENTE NO ENCONTRADO <<<")
            return
        ruta = paciente["Imagen de calor"]
        img = cv2.imread(ruta)
        imgG = img[:,:,0]
        cv2.imwrite('HeatmapBlancoYnegro.png',imgG)
        cv2.imshow('HeatMap', imgG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        myquery = {"Cedula":cedula}
        newvalues = {"$set": {"Imagen de calor (Blanco y Negro)":rut}}
        self.__neurologia.update_one(myquery,newvalues)

def validarNum(msj):
    while True:
        try:
            a = int(input(msj))
            return a 
        except ValueError:
            print(">>> INGRESE UN VALOR NUMERICO <<<")
            
def main():
    
    client = pymongo.MongoClient("mongodb+srv://EstebanAJ1:info2@cluster0.6v6oixp.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    sist = Sistema(client)
    print("\n"+"===== MENÚ PRINCIPAL =====")
    ced = sist.validarCedula()
    nom = input("-- Ingrese su nombre: ")
    ed = validarNum("-- Ingrese su edad: ")
    nom_arch = input("-- Ingrese el nombre del archivo de la señal (sin el .mat): ")
    ruta = (r"C:\Users\Alvarez Jaramillo\Desktop\Esteban\Info 2\drive-download-20230331T031844Z-001"+"\\"+nom_arch+".mat")
    sist.ingresarCedula(ced)
    sist.ingresarPaciente(ced,nom,ed,ruta)
    while True:
        print("\n"+"===== SISTEMA DE LECUTURA DE SEÑALES =====")
        print("===== MENU 1 =====")
        menu1 = validarNum('''
        1.Imprimir el tamaño de la señal
        2.Graficar una señal de EEG continua
        3.Graficar una época de una señal de EEG
        4.Graficar la señal con un color determinado y guardarla
        5.Análisis de los datos
        6.Salir
        > ''')
        if menu1 < 1 or menu1 > 6:
            print(">> INGRESE UNA OPCION DENTRO DEL RANGO DADO <<")
            continue

        if menu1 == 1: # TAMAÑO DE LA SEÑAL
            sist.tamañoSeñal()

        elif menu1 == 2: # GRAFICO SEÑAL EEG CONTINUA
            sist.graficaContinua()
            
        elif menu1 == 3: # GRAFICA DE EPOCA DE SEÑAL EEG 
            sist.graficarEpocas()            

        elif menu1 == 4: # SEÑAL CON COLOR Y GUARDAR
            sist.guardarGraficaContinua()

        elif menu1 == 5: # ANALISIS DE DATOS
            print("\n"+"===== SISTEMA DE ANALISIS DE SEÑALES =====")
            print("===== MENU 2 =====")
            menu2 = validarNum('''
            1. Ver el promedio de las 8 filas de la señal continua
            2. Ver el histograma del promedio del punto 1
            3. Ver una imagen de calor
            4. Imagen en blanco y negro
            5. salir
            > ''')
            if menu2 < 1 or menu2 > 5: 
                print(">> INGRESE UNA OPCION DENTRO DEL RANGO DADO <<")
                continue

            if menu2 == 1: # PROMEDIO DE LAS FILAS 8 DE LA SEÑAL CONTINUA
                print(sist.dfContinua())

            elif menu2 == 2: # HISTOGRAMA DEL PROMEDIO DEL PUNTO 1
                plt.hist(sist.dfContinua())
                plt.show()
                

            elif menu2 == 3: # IMAGEN DE CALOR
                hm_epocas = (sist.dfEpocas()[0,:100,:-100])
                dataframeE = pd.DataFrame(hm_epocas)
                heatmap = sns.heatmap(dataframeE, cmap="PuOr")
                rut = r"C:\Users\Alvarez Jaramillo\Desktop\Esteban\Info 2\Heatmap.png"
                plt.savefig(rut)
                plt.show()
                print("------ Para confirmar y guardar la imagen en la base de datos, ingrese la siguiente información:")
                sist.guardarImagen(rut)

            elif menu2 == 4: # IMAGEN EN BLANCO Y NEGRO
                rut = r"C:\Users\Alvarez Jaramillo\Desktop\Esteban\Info 2\HeatmapBlancoYnegro.png"
                sist.imagenByN(rut)
                
            elif menu2 == 5:
                continue

        elif menu1 == 6:
            break

if __name__ == '__main__':
    main() 

   