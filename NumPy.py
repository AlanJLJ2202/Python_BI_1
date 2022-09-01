import numpy as np


matriz_1 = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])

matriz_2 = np.array([
    [4, 5, 6],
    [4, 5, 5],
    [3, 7, 6],
])

resultado = matriz_1 + matriz_2

print(resultado)

# Suma de matrices
x = np.array([6, 7, 8, 8])
y = np.array([6, 7, 8, 8])
z = x + y

print(z)

# Metodos de NumPy

print("Media: ", np.mean(x))
print("Desviacion estandar: ", np.std(x))
print("Mediana: ", np.median(x))
print("Varianza: ", np.var(x))
print("Maximo: ", np.max(x))
print("Minimo: ", np.min(x))
print("Ordenar: ", np.sort(x))
print("Seno: ", np.sin(x))
print("Num: ", x[1])
print("Ultimo: ", x[-1])

# Distribucion uniforme

aleatorios = np.random.uniform(size=4)
print(aleatorios)
