# Divide y venceras

# Herencia, polimorfismo, abstraccion y encapsulamiento

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def correr(self):
        print("Corriendo")


perro1 = Perro("Pingo", 6)
print(perro1.nombre)

perro2 = Perro("Firulais", 2)
print(perro2.nombre)


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        pass

    def dormir(self):
        pass


# Herencia
class Gato(Animal):
    def comer(self):
        print(self.nombre, "Comiendo")


gato1 = Gato("Teodoro", 12)
gato1.comer()

#Media aritmetica, desviacion estandar
#Utiizando ciclos, listas y etodos


# Polimorfismo
# Multiples objetos que tendran comportamientos similares.
# Metodos que se llaman igual, pero dependiendo del objeto se adaptara a su comportamiento

class Pajaro(Animal):
    def comer(self):
        print(self.nombre, "Comiendo")

    def volar(self):
        print(self.nombre, "volando pa")


pajaro1 = Pajaro("Piolin", 2)
pajaro1.comer()