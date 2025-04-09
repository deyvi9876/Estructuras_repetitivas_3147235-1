
paises = [
    {
        "nombre": "Venezuela",
        "capital": "Caracas",
        "moneda": "Bolivar",
        "Poblacion": {
            "censo": 28,
            "densidad": 31
        },
        "superficie": 916445000000,
        "ciudades": [
            "Maracaibo",
            "Valencia",
            "Barquisimeto",
            "Carabobo"
        ]
    },
    {
        "nombre": "Brasil",
        "capital": "Brasilia",
        "moneda": "Real",
        "Poblacion": {
            "censo": 213,
            "densidad": 31
        },
        "superficie": 8515767000000,  
        "ciudades": [
            "Rio de Janeiro",
            "Recife",
            "Natal"
        ]
    },
    {
        "nombre": "Paraguay",
        "capital": "Asunción",
        "moneda": "Peso Guaraní",
        "Poblacion": {
            "censo": 7,
            "densidad": 31
        },
        "superficie": 406752000000, 
        "ciudades": [
            "Concepción",
            "Villarica"
        ]
    }
]


# IMPRESIÓN
for pais in paises:
    print("Ciudades Principales:")
    print("------------------------")
    for ciudad in pais["ciudades"]:
        print("-", ciudad)
    print("Nombre:", pais["nombre"])
    print("------------------------")
    print("Capital:", pais["capital"])
    print("------------------------")
    print("Moneda:", pais["moneda"])
    print("------------------------")
    print("Población:")
    print("------------------------")
    print("- Censo:", pais["Poblacion"]["censo"], "millones")
    print("------------------------")
    print("Superficie:")
    print("------------------------")
    print("- Superficie:", pais["superficie"], "m²")  
    print("------------------------")
