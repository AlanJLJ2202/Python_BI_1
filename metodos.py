def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


# print(suma(8, 9))
# print(resta(8, 9))
# print(multiplicacion(8, 9))
# print(division(8, 9))

def operaciones(a, b):
    return a * b, a / b


mult, div = operaciones(6, 7)

print(mult, div)
