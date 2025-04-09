paises = [
            {
             "nombre":"Venezuela",
             "capital":"Caracas",
             "Moneda":"Bolivar",
             "superficie":"916.445 km²",
             "poblacion":{
                    "censo": 28,
                    "densidad":31,
                         
                         },
             
             "ciudades":{
                     "Maracaibo",
                     "Valencia",
                     "Barquisimeto"

                        }
            },

            {
             "nombre":"Brasil",
             "capital":"Brasilia",
             "modena":"Real",
             "superficie":"8,51 millones km²",
             "poblacion":
                  {
                    "censo": 213,
                    "densidad":25,
                  },

              "ciudades":{
                     "Sao Paulo",
                     "Rio de Janeiro",
                     "Salvador",

                        }    
            },
             
            {
             "nombre":"Paraguay",
             "capital":"Asuncion",
             "moneda":"Guarani",
             "superficie":"406.752 km²",
             "poblacion":
                  {
                    "censo": 213,
                    "densidad":25,
                  },

             "ciudades":{
                     "Ciudad del este",
                     "Encarnacion",

                        }    
            },
         ]

for pais in paises:
    print("nombre:", pais["nombre"])

#recorrer todos los paises:
    print("recorriendo todos los paises")
for pais in paises:
    print("ciudades principales:")
    for ciudad in pais ["ciudades"]:
        print("-",ciudad)
for pais in paises:
    print("nombre:", pais["nombre"])
    print("capital", pais["capital"])
    print("superficie", pais["superficie"])
    print("poblacion:")
    print("- censo: ", pais["poblacion"]["censo"], "millones")
    print("---------------")
    print("ciudades principales:")
    
