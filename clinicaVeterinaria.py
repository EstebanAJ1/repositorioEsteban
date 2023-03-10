import pymongo

class Medicamento():
    def __init__(self, client):
        mydb = client["ClinVeterinaria"]
        self.__medicamentos = mydb["Medicamentos"] 

# METODOS 
    def asignarNombre(self,nombre_med):
        f = self.__medicamentos.insert_one({"Nombre": nombre_med})

    def asignarDosis(self, nombre_med,dosis):
        myquery = {"Nombre": nombre_med}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__medicamentos.update_one(myquery, newvalues)
        #self.__medicamento = self.__medicamentos.insert_one({"Dosis":dosis})
        #return self.__medicamento

    def asignarHistClin(self,nombre_med,historia):
        myquery = {"Nombre":nombre_med}
        newvalues = {"$set": {"Historia": historia}}
        self.__medicamentos.update_one(myquery,newvalues)

class Mascota:
    def __init__(self,client, historia):
        mydb = client["ClinVeterinaria"]
        self.__mascotas = mydb["Mascotas"]
        self.__historia = historia
    
# METODOS
    def asignarNomMascota(self,nom_mascota):
        myquery = {"Historia Clinica ": self.__historia}
        newvalues = {"$set": {"Nombre":nom_mascota}}
        self.__mascotas.update_one(myquery,newvalues)

    def asignarNumHistoria(self):
        h = self.__mascotas.insert_one({"Historia":self.__historia})

    def asignarTipo(self,tipo):
        myquery = {"Historia":self.__historia}
        newvalues = {"$set":{"Tipo mascota": tipo}}
        self.__mascotas.update_one(myquery,newvalues)

    def asignarFechaIng(self,fecha_ing):
        myquery = {"Historia":self.__historia}
        newvalues = {"$set":{"Fecha_ingreso": fecha_ing}}
        self.__mascotas.update_one(myquery,newvalues)

    def asignarPeso(self,peso):
        myquery = {"Historia":self.__historia}
        newvalues = {"$set":{"Peso":peso}}
        self.__mascotas.update_one(myquery,newvalues)

    def asginarMedicamento(self,med):
        myquery = {"Historia":self.__historia}
        newvalues = {"$set":{"Medicamento":med}}
        self.__mascotas.update_one(myquery,newvalues)

class Sistema:
    def __init__(self,client):
        mydb = client["ClinVeterinaria"]
        self.__medicamentos = mydb["Medicamentos"]
        self.__mascotas = mydb["Medicamentos"]

    def verificarMascota( self, historia ):
        a = list(self.__mascotas.find({"Historia": historia}))
        if len(a) == 0:
            return False
        else: 
            return True 

    def verFechaingreso(self,historia):
        vfi = list(self.__mascotas.find({"Historia": historia}))
        try:
            print(vfi[-1]["Fecha_ingreso"])
        except:
            print(">>> No hay fecha de ingreso con este número de historia clinica <<<")  

    def verNumMascota(self):
        vnm = list(self.__mascotas.find())
        return len(vnm)
    
    def verMedAdmin(self,historia):
        med = list(self.__medicamentos.find({"Historia":historia}))
        for m in med:
            print(f"Nombre del medicamento: {m['Nombre']}\n Dosis: {m['Dosis']}")

    def eliminarMascota(self,historia):
        a = list(self.__mascotas.find({"Historia": historia}))
        self.__mascotas.delete_one(a[-1])
        b = list(self.__medicamentos.find({"Historia": historia }))
        for eliminar in b:
            self.__medicamentos.delete_one(eliminar)


def validarNum(msj):
    while True:
        try:
            a = int(input(msj))
            return a
        except ValueError: 
            print(">>> Error. Ingrese un numero entero <<<")

def main():
    
    client = pymongo.MongoClient("mongodb+srv://EstebanAJ1:info2@cluster0.6v6oixp.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    s = Sistema(client)
    
    while True:
        opc = input('''-Ingrese alguna de las opciones:
        1. Ingresar mascota
        2. Ver fecha de ingreso de la mascota
        3. Ver número de mascotas en el servicio
        4. Ver el medicamento que se está administrando a una mascota
        5. Eliminar una mascota 
        6. Salir
        > ''')

        if opc == "1": # Ingresar nueva mascota
            #Se verifica que haya espacio
            if s.verNumMascota() >= 10:
                print(">>> No hay espacio <<<")
                continue
            
            # Se pide el numero de la historia clinia y se ve que no este
            num_hist = validarNum("-Ingrese el número de la historia clinica: ")
            if s.verificarMascota(num_hist) == True:
                print(">>> Ya se encuentra esta historia clinica <<<")
                continue

            # Si la historia no esta, pido nuevos datos
            nom = input("-Ingrese el nombre de la mascota: ")
            tipo = input("-Ingrese el tipo de mascota, canino o felino: ")
            tipo2 = tipo.upper()
            peso = input("-Ingrese el peso de la mascota: ")
            fecha_ing = input("-Ingrese la fecha de ingreso así, dd/mm/aaaa: ")
            cant_med = validarNum(input("-Ingrese la cantidad de medicamentos: "))
            
            # Por cada medicamento pido los datos
            
            for x in range(0,cant_med):
                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                dosis = validarNum("Ingrese la dosis: ")
                medicamento = Medicamento(client)
                medicamento.asignarNombre(nombre_medicamentos)
                medicamento.asignarDosis(nombre_medicamentos,dosis)
                medicamento.asignarHistClin(nombre_medicamentos, num_hist)

            # Creo la mascota y le asigno informacion y la ingreso al sistema
            masc = Mascota(client,num_hist)
            masc.asignarNomMascota(nom)
            masc.asignarTipo(tipo2)
            masc.asignarPeso(peso)
            masc.asignarFechaIng(fecha_ing)
            masc.asignarNumHistoria()
            print(f">> Mascota de nombre {nom} ingresada.")

        elif opc == "2":
            num_hist = validarNum("-Ingrese el número de la historia clinica: ")
            if s.verificarMascota(num_hist) == False:
                print(">>> La mascota no está en el sistema <<<")
                continue
            s.verFechaingreso(num_hist)

        elif opc == "3":
            print("El sistema tiene " + str(s.verNumMascota()) + " mascotas")

        elif opc == "4":
            num_hist = validarNum("-Ingrese el número de la historia clinica: ")
            if s.verificarMascota(num_hist) == False:
                print(">>> La mascota no está en el sistema <<<")
                continue
            s.verMedAdmin(num_hist)

        elif opc == "5":
            num_hist = validarNum("-Ingrese el número de la historia clinica a eliminar: ")
            if s.verificarMascota(num_hist) == False:
                print(">>> La mascota no está en el sistema <<<")
                continue
            s.eliminarMascota(num_hist)
            print(">>> Se eliminó la mascota del sistema <<<")

        elif opc == "6":
            print(">>> Ha salido del programa <<<")
            break

        else:
            print("Opcion no valida: ")

if __name__ == "__main__":
    main()
    



    
