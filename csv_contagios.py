import pandas as pd


def extract(source_csv, data_series, index_series, name_series):
    csv = pd.read_csv(source_csv)
    Serie = pd.Series(data=csv[data_series].values, index=csv[index_series].values, name=name_series)
    return Serie



csv[1].sum()
series = extract("Historico de Contagio de COVID-19 - Estado de Guanajuato_Página 1_Serie temporal.csv", 'Por dia',
                 'Fecha', 'Serie de prueba')


print('Serie: ', series)

mediana = series.median()
media = series.mean()
print('Desviación estandar: \n', series.std())
print('Mediana: \n', series.median())
print('Media: \n', series.mean())

# El dia que hubó mas casos

print('Dia con mas casos', series.idxmax(), 'Casos', series.max())


# Los días (fechas) donde hubo más casos con respecto a la mediana (mayores que la mediana).

casos_mayores_mediana = series[series > series.median()]
print('Mayor a mediana = \n', casos_mayores_mediana)

# La desviación estándar.

desviacion_estandar = series.std()
print('Desviacion estandar = \n', desviacion_estandar)

# Los días (fechas) y la cantidad de casos entre la media y la mediana.
casos_entre_media_mediana = series[series.between(left=series.median(), right=series.mean())]
print('Casos entre media y mediana = \n', casos_entre_media_mediana)


# def transform(series):
