import os
#*-------------------------------------------------------------------------------
#* Ejemplo de decorator pattern
#* Recursión de objetos para agregarle un "wrapper" con sus propios atributos
#*-------------------------------------------------------------------------------

#*--- Esta es la clase que representa el numero original

class NumeroObtenido:

	def __init__(self, number):
		self._number = number

	def render(self):
		return self._number

#*--- Esta es la clase se encarga de sumar

class Sumar(NumeroObtenido):

	def __init__(self,wrapped):
		self._wrapped = wrapped

	def render(self):
         suma =self._wrapped + 2
         return suma

#*--- Esta es la clase se encarga de mulriplicar

class Multiplicar(NumeroObtenido):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
         multiplicar = self._wrapped * 2
         return multiplicar

#*--- Esta es la clase se encarga de dividir

class Dividir(NumeroObtenido):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
         dividir = self._wrapped / 3
         return dividir

#*------------------------------------------------------------------------
#* main
#*------------------------------------------------------------------------
if __name__ == '__main__':

	os.system("clear")
	number = 6
	before_txt=NumeroObtenido(number)

	print("\nAntes (%s) y antes mas 2 (%s)\n" % (before_txt.render(),Sumar(number).render()))
	print("\nAntes (%s) y antes por 2 (%s)\n" % (before_txt.render(),Multiplicar(number).render()))
	print("\nAntes (%s) y antes dividido 2 (%s)\n" % (before_txt.render(),Dividir(number).render()))
