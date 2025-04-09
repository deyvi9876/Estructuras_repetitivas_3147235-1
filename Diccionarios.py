# Diccionario que almacena los datos de países

pais1 =  {
        "nombre": "Argentina",
        "Capital": "Buenos Aires",
        "Moneda": "Peso Argentino",
        "ciudades": [
                        "Buenos Aires",
                        "Mar del Plata",
                        "La Plata",
                        "Ciudad de Santa Fe",
                        "Rosario",
                        "Ciudad de Córdoba",
                        "San Miguel de Tucumán"
        ],
        "Población": {
                     "censo": "46",
                     "densidad": "16"
        }
}

pais2 = {
        "nombre": "Ecuador",
        "Capital": "Quito",
        "moneda": "Dólar",
        "ciudades": [
                        "Guayaquil",
                        "Cuenca",
                        "Manta",
                        "Machala",
                        "Loja",
                        "Nueva Loja",
                        "Ibarra",
                        "Santo Domingo" 
                    ],
        "población": {
            "censo": "16",
            "densidad": "70",
        }
}

pais3 = {
    "nombre": "Paraguay",
    "capital": "Asunción",
    "moneda": "Guaraní",
    "ciudades": [
                "Ciudad del Este",
                "Asunción",
                "Pedro Juan Caballero",
                "Encarnación",
                "San Pedro de Ycuamandiyú",
                "Villarica",
                "Concepción",
                "San Juan Bautista",
                "Caacupé"
    ],
    "población": {
                "censo": "7.76",
                "densidad": "18"
    }
}

# Acceder a la información del país
print(pais1['Capital'])  # Accede a la clave 'Capital' con mayúscula
print(pais1["ciudades"][1])  # Accede a la segunda ciudad de la lista (índice 1)
print("----------")

# Iterar las ciudades del Diccionario
for ciudad in pais1["ciudades"]:
    print(ciudad)

# Acceder a datos poblacionales
print('---------------------')
print("Censo:", pais1["Población"]["censo"], "millones de hab")
print("Densidad:", pais1['Población']['densidad'], "por km²")
