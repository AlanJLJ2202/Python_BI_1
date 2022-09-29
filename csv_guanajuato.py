import pandas as pd


def extract(source_csv, data_series, index_series, name_series):
    csv = pd.read_csv(source_csv)
    Serie = pd.Series(data=csv[data_series].values, index=csv[index_series].values, name=name_series)
    return Serie


source = extract("Historico de Contagio de COVID-19 - Estado de Guanajuato_Página 1_Serie temporal.csv",
                 'Por dia', 'Fecha', 'Casos')


# print('Serie: ', series)


def transform(series):

    print('Desviación estandar: \n', series.std())
    print('Mediana: \n', series.median())
    print('Media: \n', series.mean())

    # El dia que hubó mas casos

    pico_maximo_diccionario = {
        'Dia con mas casos': [series.idxmax()],
        'Casos': [series.max()]
    }

    pico_maximo_dataframe = pd.DataFrame(pico_maximo_diccionario)

    print(pico_maximo_dataframe)

    # Los días (fechas) donde hubo más casos con respecto a la mediana (mayores que la mediana).

    casos_mayores_mediana = series[series > series.median()]
    print('Mayor a mediana = \n', casos_mayores_mediana)

    # La desviación estándar.

    desviacion_estandar = series.to_frame()
    print('Desviacion estandar = \n', desviacion_estandar)

    desviacion_estandar_diccionario = {
        'Tipo': ['Desviacion estandar'],
        'Resultado': [series.std()]
    }

    desviacion_estandar_dataframe = pd.DataFrame(desviacion_estandar_diccionario)

    # Los días (fechas) y la cantidad de casos entre la media y la mediana.
    casos_entre_media_mediana = series[series.between(left=series.median(), right=series.mean())]
    print('Casos entre media y mediana = \n', casos_entre_media_mediana)

    return pico_maximo_dataframe, \
           casos_mayores_mediana.to_frame(), \
           desviacion_estandar_dataframe, \
           casos_entre_media_mediana.to_frame()

transform(source)


def load(pico_maximo, mayor_mediana, desviacion_estandar, intervalo_casos):
    writer = pd.ExcelWriter('Historico_contagios_guanajuato.xlsx')
    pico_maximo.to_excel(writer, sheet_name='Pico maximo de casos', index=True)
    mayor_mediana.to_excel(writer, sheet_name='Casos arriba de mediana', index=True)
    desviacion_estandar.to_excel(writer, sheet_name='Desviacion estandar', index=True)
    intervalo_casos.to_excel(writer, sheet_name='Intervalo entre media y mediana', index=True)
    writer.save()


# load(transform(source)[0], transform(source)[1], transform(source)[2], transform(source)[3])
