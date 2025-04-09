
# Es una estructura o una conoxion de datos
# que los almacena en pares clave y valor
# - un diccionario comienza y termina en llaves (curly braces).
# - la clave se separa del valor por dos puntos (:)
# - cada clave es un string 
# el valor puede ser de cualquier tipo
# - cada elemento se separa por una coma. 

#EJEMPLO DICCIONARIO
#Diccionario que almacene los datos de pais
pais1 = {
            "nombre":"argentina", 
            "Capital":"Buenos aires",
            "moneda":"peso argentino",
            "ciudades" :
                     [
                         "Cordoba",
                         "Rosario",
                         "Mendoza",
                     ],
            "poblacion":{
                "Censo" : "46",
                "densidad" : "16",
                        }
        }

        

#informacion del diccionario
print(pais1["Capital"])

pais2 = {
            "nombre":"Ecuador", 
            "Capital":"Quito",
            "moneda":"Dolar",
            "ciudades" :
                     [
                         "Guayaquil",
                         "manta",
                         "Cuenca",
                     ],
           "poblacion":{
                "Censo" : "30",
                "densidad" : "8",
                        }          
        }


pais3 = {
            "nombre":"Chile", 
            "Capital":"Santiago",
            "moneda":"Dolasian",
            "ciudades" :
                     [
                         "cante",
                         "nieves",
                         "motevideo",
                     ],
           
           "poblacion":{
                "Censo" : "30",
                "densidad" : "8",
                        }             
        }
#acceder a info del pais
print(pais1["moneda"])
#ciudad del pais
print(pais1["ciudades"][1])

#iterar las ciudades del pais
for ciudad in pais1["ciudades"]:
    print(ciudad)

#acceder a datos poblacionales 
print("----------")
print("censo:", pais1["poblacion"]["censo"],
      "millones de habitantes")
print("densidad:", pais1["poblacion"]["densidad"],
      "por km")