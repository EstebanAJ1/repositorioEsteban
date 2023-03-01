import pymongo

client = pymongo.MongoClient("mongodb+srv://EstebanAJ1:esteban123@cluster0.6v6oixp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["bbdd"] # Base de datos
mycol = mydb["clientes"] # Coleccion

mydict = {"nombre": "Esteban", "direccion": "C/ Mayor 1"}
x =mycol.insert_one(mydict) 

print(x.inserted_id)

#Para actualizar valores
myquery = {"nombre": "Esteban", "direccion": "C/ Mayor 1" }
newvalues = {"$set": {"nombre":"Luis"}}

mycol.update_one(myquery, newvalues)

#Buscar los datos en la base de datos
for y in mycol.find(): 
    print(y)
    
# Buscar un dato en especifico de la base de datos
for x in mycol.find({"nombre": "Luis"}): 
    print(x)
    #print(x["nombre"])