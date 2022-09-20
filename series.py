import pandas as pd

# poblacion = pd.Series([45, 54, ])

poblacion = pd.Series({
    "Mexico": 127,
    "Peru": 40,
    "Argentina": 45,
    "Colombia": 30,
    "Chile": 15,
    "Guatemala": 20
}, name="Latinoamerica")

print(poblacion)


# Se puede modificar los datos despues de haber creado la Serie

poblacion = poblacion * 1000 # todos los datos se van a multiplicar por mil

poblacion["Mexico"] = 127 #Se modifica el dato en cierta pocision

poblacion_menor = poblacion < 70000
poblacio_mayor = poblacion >= 100000
print(poblacio_mayor)

print('Media: ', poblacion.mean()) #Media
print('Mediana: ', poblacion.median()) #Mediana
print('Std: ', poblacion.std()) #Desviacion estandar
