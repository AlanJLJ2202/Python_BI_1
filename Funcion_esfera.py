import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])


def SumCancellation(x):
    return np.sum(1 / (10 ** -5 + (x)))


array_x = np.array([-0.10, 0.01, 0.07, 0.09, 0.11])
array_y = np.array([-0.11, 0.05, 0.075, 0.08, 0.14])

def Validacion(x, y):
    for i in range(1, len(x)):
        if x[i] == y[i]:
            valor = y[i - 1] + x[i]
            if x[i] == valor:
                return 1
            else:
                return 0
        else:
            return 0


if Validacion(x, y) == 1:
    print('SumCancellation: ', SumCancellation(np.absolute(x)))


def Rastrigin(x):
    result = 10 * len(x) + np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x))
    return result


c = np.array([-1, 4, 5, 5])

print('Rastrigin: ', Rastrigin(c))

def two_axes(x):
    sumatoria_1 = 0

    for i in range(0, len(x) // 2):
        sumatoria_1 += ((10 ** 6) * x[i] ** 2 + np.sum(x))

    for i in range((len(x)//2)+1 , len(x)):
        sumatoria_2 = np.sum(x**2)
        return sumatoria_1+sumatoria_2


t = np.array([-1, 4, 5, 5])

print('Two_axes: ', two_axes(t))


def Ellipsoid(x):
    resultado = 0
    for i in x:
        resultado += 10 ** (6 * (i - 1) / (len(x) - 1)) * i ** 2
    return resultado


e = np.array([-1, 4, 5, 5])

print('Ellipsoid: ', Ellipsoid(e))


def Cigar(x):
    for i in range(2, len(x)):
        resultado_1 = np.sum((10 ** 6) * (x ** 2))
    for i in range(1, len(x)):
        resultado_2 = np.sum((x ** 2) + resultado_1)
    return resultado_2


c = np.array([-10, -5, 4, 5, 5])

print('Cigar: ', Cigar(c))


def Tablet(x):
    for i in range(2, len(x)):
        resultado = np.sum(x ** 2)
    for i in range(1, len(x)):
        resultado_2 = np.sum((10 ** 6) * (x ** 2) + resultado)
    return resultado_2

t = np.array([-10, -5, 4, 5, 5])

print('Tablet: ', Tablet(t))



def CigarTablet(x):
    for i in range(2, len(x) - 1):
        resultado = np.sum(((10 ** 4) * x ** 2) + ((10 ** 8) * x[len(x)] ** 2))
    for i in range(1, len(x)):
        resultado_2 = np.sum((x ** 2) + resultado)
    return resultado_2

ct = np.array([-10, -5, 4, 5, 5])

print('CigarTablet: ', Tablet(ct))


def sphere(x):
    return np.sum(x ** 2)

s = np.array([-10, -5, 4, 5, 5])

print('Sphere: ', sphere(s))


def Griewangk(x):
    for i in range(1, len(x)):
        sumatoria = np.sum((x ** 2) / 4000)
        prod = np.prod(np.cos((x / (np.sqrt(i)))))
    return sumatoria - prod + 1

g = np.array([-600, -5, 4, 5, 600])

print('Griewangk: ', Griewangk(g))


def Ackley(x):
    resultado = -20 * np.exp(-.2 * np.sqrt((1 / len(x)) * np.sum(x ** 2))) + np.exp(
        (1 / len(x)) * np.sum(np.cos(2 * np.pi * x))) + 20 + np.exp(1)
    return resultado

a = np.array([-32, -5, 4, 5, 32])

print('Ackley: ', Ackley(a))

'''
def sphere_numpy(x):
    return np.sum(x ** 2)


x = np.array([3, 4, 5, 6])

print(sphere_numpy(x))





# Pendiente






def Rastrigin(x):
    for i in range(1, len(x)):
        sum2 = np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x))
    return (10 * len(x)) + sum2


def TwoAxes(x):
    for i in range(1, len(x) / 2):
        sum1 = np.sum((10 ** 6) * x[i] ** 2)
    for i in range((len(x) / 2) + 1, len(x)):
        sum1 = np.sum(x ** 2)
    return sum + sum1


def Ellipsoid(x):
    for i in range(1, len(x)):
        eli = np.sum((10 ** (6 * ((i - 1) / len(x) - 1))) * x ** 2)
    return eli






def Rosenbrock(x):
    for i in range(2, len(x) - 1):
        ros = np.sum(100 * ((x[i] - x[i - 1] ** 2) ** 2) + (x[i] - 1) ** 2)
    return ros

print(sphere(x))

'''
