
def edad_meses(edad):
    return edad * 12

diccionario = {
    "Nombre": "Pepe",
    "Apellido": "Juarez",
    "Edad": 20,
    "Edad_meses": edad_meses(20)
}

print(diccionario["Edad_meses"])