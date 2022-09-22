import pandas as pd

def load(source_csv, data_series, index_series, name_series):
    csv = pd.read_csv(source_csv)
    Serie = pd.Series(data=csv[data_series].values, index=csv[index_series].values, name=name_series)
    return Serie


series = load("Historico de Contagio de COVID-19 - Estado de Guanajuato_Página 1_Serie temporal.csv", 'Por dia', 'Fecha', 'Serie de prueba')
print('Serie: ', series)


print('Dia:', series.idxmax(), 'Casos:', series.max())

