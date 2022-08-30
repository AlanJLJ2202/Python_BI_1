import math

# Practica 1 - Media aritmetica

x = [1, 2, 3, 4, 5]
sumatoria = 0

for i in x:
    print(i)
    sumatoria += i

print('Sumatoria', sumatoria)

resultado = sumatoria / len(x)

print('Resultado', resultado)


# Practica 1 - Desviacion estandar

y = [1, 2, 3, 4, 5]
sumatoria_2 = 0

for i in x:
    print(i)
    sumatoria_2 += (i - resultado)**2

print(sumatoria_2)

s = math.sqrt(sumatoria_2 / len(x))

print('Desviacion', s)



