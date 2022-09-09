import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic)

# Tipos de datos
print(titanic.dtypes)

#Para describir el csv
print(titanic.describe())

#Informacion detallada de los datos que estan cargados
print(titanic.info())

#Para acceder a uno de los indices
print(titanic["Cabin"])

#titanic.to_html("titanic.html")
