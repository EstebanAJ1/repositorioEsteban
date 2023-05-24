import pymongo 

client = pymongo.MongoClient("mongodb+srv://EstebanAJ1:info2@cluster0.6v6oixp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

class Sistema():
    def __init__(self,client):
        mydb = client["Biomecanica"]
        self.__ejercicio = mydb["Ejercicio"]

    def verificar_db(self,cedula):
        x = self.__ejercicio.find_one({"Cedula":int(cedula)})
        if x == None:
            return None, None
        else:
            return x["Nombre"], x["Edad"]

    def cedula(self,cedula):
        x = self.__ejercicio.insert_one({"Cedula": cedula})

    def nombre(self,cedula,nombre,edad,deporte, ruta):
        myquery = {"Cedula":cedula}
        newvalues = {"$set": {"Nombre":nombre, "Edad":edad, "Deporte":deporte, "Ruta":ruta}}
        self.__ejercicio.update_one(myquery,newvalues)



