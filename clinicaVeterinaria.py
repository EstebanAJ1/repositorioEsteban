import pymongo

class Medicamento():
    def __init__(self, client):
        mydb = client["ClinVeterinaria"]
        self.__medicamentos = mydb["medicamentos"]

    def verNombre(self,nombre):
        for x in self.__medicamentos.find({"Nombre": nombre}):
            return print(x)
        
    #def verNombre(self):      DE MANERA MAS GENERAL, PARA QUE ME TRAIGA LOS NOMBRES
    #    for x in self.__medicamentos.find({"Nombre"}):
    #        return print(x)

    def asignarDosis(self, nombre_med,dosis):
        self.__medicamento = self.__medicamentos.insert_one({"Nombre": nombre_med, "Dosis":dosis})
        return self.__medicamento

def main():
    
    client = pymongo.MongoClient("mongodb+srv://EstebanAJ1:<password>@cluster0.6v6oixp.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    nm = int(input("Ingrese la cantidad de medicamento de la mascota: "))
    m = 0
    while m<nm:
        nombre_medicamentos = input("Ingrese el nombre: ")
        dosis = int(input("Ingrese la dosis: "))
        medicamento = Medicamento(client)
        medicamento.asignarDosis(nombre_medicamentos,dosis)
        medicamento.verNombre("Dolex")
        m+=1

if __name__ == "__main__":
    main()



    
