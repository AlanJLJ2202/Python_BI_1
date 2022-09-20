import pandas as pd

import matplotlib.pyplot as plt


# Los nombres de las columnas fueron puestos manualmente en el csv

def extract(ruta):
    csv = pd.read_csv(ruta)
    return csv


def transform(csv):
    # Aquellas plantas cuyo largo de sépalo y largo del pétalo esten entre 4.7 y 6.1

    condicion_1 = csv.loc[(csv['SepalLengthCm'] >= 4.7) & (csv['SepalLengthCm'] <= 6.1)]
    condicion_2 = condicion_1.loc[(csv['PetalLengthCm'] >= 4.7) & (csv['PetalLengthCm'] <= 6.1)]
    ejercicio_1 = condicion_2

    # Aquellas plantas cuyo ancho del pétalo sea mayor que 2.1

    ejercicio_2 = csv[lambda x: x['PetalWidthCm'] > 2.1]

    return ejercicio_1, ejercicio_2


def load(ejercicio_1, ejercicio_2):
    writer = pd.ExcelWriter('ETL.xlsx')
    ejercicio_1.to_excel(writer, sheet_name='Largo_sepalo_petalo', index=True)
    ejercicio_2.to_excel(writer, sheet_name='Ancho_petalo', index=True)
    writer.save()


# load(transform(extract("iris.csv"))[0], transform(extract("iris.csv"))[1])


# csv = pd.read_csv("iris.csv")

# csv_2.plot()
plt.show()