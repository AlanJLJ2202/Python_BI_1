import numpy as np
'''
def sphere(x):
    sum = 0
    for val in x:
        sum += val**2
    return sum
# x = [4, 5, 6, 7]

print(sphere([3, 4, 5, 6]))

def sphere_numpy(x):
    return np.sum(x**2)

x = np.array([3, 4, 5, 6])

print(sphere_numpy(x))

# def sum_cancellation():
'''
def Rastrigin(x):
    result = 10 * len(x) + np.sum(x**2 - 10 * np.cos(2*np.pi*x))
    return result

c = np.array([-1, 4, 5, 5])

print('Rastrigin: ', Rastrigin(c))

# Pendiente

def two_axes(x):
    resultado = 0

    for i in range(0, len(x) // 2):
        resultado += (10**6 * i**2 + np.sum(x))
        return resultado

t = np.array([-1, 4, 5, 5])

print('Two_axes: ', two_axes(t))

def Ellipsoid(x):
    resultado = 0
    for i in x:
        resultado += 10**(6 * (i-1)/(len(x)-1)) * i**2
    return resultado

e = np.array([-1, 4, 5, 5])

print(Ellipsoid(e))



