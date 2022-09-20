import pandas as pd


def load(source):
    csv = pd.read_csv(source)
    return csv

csv = load("Historico de Contagio de COVID-19 - Estado de Guanajuato_Página 1_Serie temporal.csv")
print('CSV: ', csv)


serie = csv.transpose()
serie.name = 'Contagios'

json = csv['Fecha'].to_json()

print(json)

series = pd.read_json(json, typ='series', orient='records')
print('Serie: ', series.values)