#Reto 3
print("----------- RETO 3 ----------")
"""Piensa un escenario en el que se quiere decidir un restaurante para una celebración.
Los organizadores quieren que cumpla uno de los siguientes puntos:
• Que haya 3 platos en el menú, que incluya DJ y dos horas de barra libre.
• Que haya cóctel de bienvenida, menú con dos platos y una hora de barra libre.
Utilizar los bloques try-except-finally para las posibles excepciones que se produzcan"""

# Restaurante 1
platos_menu1 = 3
dj_presente1 = True
horas_barra_libre1 = 2
coctel_bienvenida1 = False
platos_menu21 = 2
horas_barra_libre21 = 1

# Restaurante 2
platos_menu2 = 2
dj_presente2 = False
horas_barra_libre2 = 2
coctel_bienvenida2 = True
platos_menu22 = 3
horas_barra_libre22 = 1

# Comprobación del restaurante 1
try:
    if (platos_menu1 == 3 and dj_presente1 and horas_barra_libre1 == 2) or (coctel_bienvenida1 and platos_menu21 == 2 and horas_barra_libre21 == 1):
        print("El restaurante 1 cumple con una de las condiciones.")
    else:
        raise Exception("El restaurante 1 no cumple con ninguna de las condiciones.")
except Exception as e:
    print("Excepción:", str(e))
finally:
    print("Fin de la comprobación del restaurante 1.")

# Comprobación del restaurante 2
try:
    if (platos_menu2 == 3 and dj_presente2 and horas_barra_libre2 == 2) or (coctel_bienvenida2 and platos_menu22 == 2 and horas_barra_libre22 == 1):
        print("El restaurante 2 cumple con una de las condiciones.")
    else:
        print("El restaurante 2 no cumple con ninguna de las condiciones.")
except Exception :
    print("Excepción:")
finally:
    print("Fin de la comprobación del restaurante 2.")


#Reto 4
print("----------- RETO 4 ----------")
"""Teniendo la siguiente estructura de un diccionario:
persona =
{
"nombre" : str,
"apellido" : str,
"anyoNacimiento" : int,
"aficiones": array of str,
"dni": { "anyoExpedicion" : int,
"lugarNacimento": str},
"colorPelo" : str
}
Crear una lista de personas con 4 diccionarios de la estructura persona definida en el punto anterior.
Tomando como base la lista anterior:
Mostrar el nombre de todos aquellas personas de la lista que tengan el pelo castaño.
Mostrar la edad de todos los que sean mayores de 30.
Utilizar los bloques try-except-else-finally para tratar las posibles excepciones que
ocurran."""

#la lista de personas
persona1 = {
    "nombre": "José Luis",
    "apellido": "García",
    "anyoNacimiento": 1999,
    "aficiones": ["fútbol", "música", "viajar"],
    "dni": {
        "anyoExpedicion": 2000,
        "lugarNacimiento": "Madrid"
    },
    "colorPelo": "castaño"
}

persona2 = {
    "nombre": "Ana",
    "apellido": "López",
    "anyoNacimiento": 1989,
    "aficiones": ["leer", "cocinar", "caminar"],
    "dni": {
        "anyoExpedicion": 1999,
        "lugarNacimiento": "Tenerife"
    },
    "colorPelo": "castaño"
}

persona3 = {
    "nombre": "Luis",
    "apellido": "Martínez",
    "anyoNacimiento": 1989,
    "aficiones": ["senderismo", "cine", "buceo"],
    "dni": {
        "anyoExpedicion": 2002,
        "lugarNacimiento": "Valencia"
    },
    "colorPelo": "Calvo"
}

persona4 = {
    "nombre": "Laura",
    "apellido": "González",
    "anyoNacimiento": 1987,
    "aficiones": ["yoga", "guitarra", "jardinería"],
    "dni": {
        "anyoExpedicion": 2006,
        "lugarNacimiento": "Sevilla"
    },
    "colorPelo": "pelirrojo"
}


personas = [persona1, persona2, persona3, persona4]

# Mostrar personas con pelo castaño
try:
    print("Personas con pelo castaño:")
    if personas[0]["colorPelo"] == "castaño":
        print(personas[0]["nombre"])
    if personas[1]["colorPelo"] == "castaño":
        print(personas[1]["nombre"])
    if personas[2]["colorPelo"] == "castaño":
        print(personas[2]["nombre"])
    if personas[3]["colorPelo"] == "castaño":
        print(personas[3]["nombre"])

# Mostrar personas mayores de 30 años
    print("Personas mayores de 30 años:")
    edad_persona1 = 2023 - personas[0]["anyoNacimiento"]
    if edad_persona1 > 30:
        print(personas[0]["nombre"])
    edad_persona2 = 2023 - personas[1]["anyoNacimiento"]
    if edad_persona2 > 30:
        print(personas[1]["nombre"])
    edad_persona3 = 2023 - personas[2]["anyoNacimiento"]
    if edad_persona3 > 30:
        print(personas[2]["nombre"])
    edad_persona4 = 2023 - personas[3]["anyoNacimiento"]
    if edad_persona4 > 30:
        print(personas[3]["nombre"])
except Exception:
    print("Error: sin datos")
finally:
    print("¡Fin del programa!")