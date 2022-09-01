import math

x = [3, 4, 3]


class practica_1:

    def media_aritmetica(self):
        sumatoria = 0

        for i in x:
            sumatoria += i

        print('Sumatoria', sumatoria)
        media = sumatoria / len(x)
        print('Media', media)
        return media

    def desviacion_estandar(self, media):
        # Practica 1 - Desviacion estandar
        sumatoria_2 = 0

        for i in x:
            sumatoria_2 += (i - media) ** 2

        s = math.sqrt(sumatoria_2 / len(x))
        print('Desviacion', s)


test = practica_1()

media = test.media_aritmetica()
test.desviacion_estandar(media=media)
