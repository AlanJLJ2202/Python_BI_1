import pandas as pd

import matplotlib.pyplot as plt


def load(source):
    csv = pd.read_csv(source)
    return csv


iris_csv = load("iris.csv")

print(iris_csv)

# primero

iris_csv.plot()

# segundo

iris_csv["SepalLengthCm"].plot()

# tercero

iris_csv.plot.scatter(x="SepalLengthCm", y="PetalLengthCm", alpha=0.5)

# cuarto

iris_csv.plot.box()

# Quinto

iris_csv.plot.area(figsize=(12, 4), subplots=True)

fig, axs = plt.subplots(figsize=(12, 4))
iris_csv.plot.area(ax=axs)
axs.set_ylabel("Concentración de tamaños")
fig.savefig("concentracion.png")
plt.show()

