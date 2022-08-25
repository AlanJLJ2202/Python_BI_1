print("Hello world")

a = 5
b = 6
c = a + b

print(a, "+", b, "=", c)

# Para convertir a String es str(a)
# y para concatenar enteros seria str(a)+

# INPUT

# Por lo general los inputs son str y se tienen que castear

x = int(input("Escribe algo: "))
y = float(input("Escribe algo: "))
print(x + y)

"""
Comentarios en multiples
lineas
"""

# Condiciones

a = int(input("Escribe un numero: "))

if a >= 10:
    print(a, "Es mayor o igual a 10")
else:
    print(a, "Es menor a 10")

# Condiciones anidadas

if (a >= 10) | (a <= 20):
    print(a, "Es mayor y menor que 20")
    # Para poner un else if se pone la palabra reservada elif
elif a < 17:
    print(a, "Es menor a 10 o mayor a 20")
else:
    print("Otro caso")

# Ciclos

for i in range(10):
    print(i)

# Condicion que va del 0 a menos 10 de 2 en 2
for i in range(0, 10, 2):
    print(i)



# Listas

list = [1, 2, 3, "Cadena", False]

# Lista de listas
list2 = [1, "XD", list]

print(list)

# Foreach
for val in list:
    print(val)
