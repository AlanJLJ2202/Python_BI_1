import pandas as pd



# lista_columnas = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]

#iris = pd.read_csv("iris.csv", usecols=[0, 1, 2, 3, 4, 5], names=["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"],  header=None)


iris = pd.read_csv("iris.csv")


primer_condicion = iris.loc[(iris['SepalLengthCm'] >= 4.7) & (iris['SepalLengthCm'] <= 6.1)]
print(primer_condicion.loc[(iris['PetalLengthCm'] >= 4.7) & (iris['PetalLengthCm'] <= 6.1)])

print(iris[lambda x: x['PetalWidthCm'] > 2.1])

