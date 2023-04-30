import os
#*--------------------------------------------------------------------
#* Este es un ejemplo de patrón bridge
#*
#*--- Se definen los métodos de producción, cada uno toma los mismos
#*--- tres atributos genéricos length, breadth and height produce un
#*--- cubo acorde a esa especificación
#*--------------------------------------------------------------------

#*--- Abstracción de implementación (API1)
class ProducingLamina5mt:

	def produceLamina(self, ancho,espesor):

		print("Se esta produciendo en el tren laminador de 5 metros",ancho,espesor)

#*--- Abstracción de implementación (API2)
class ProducingLamina10mt:

	def produceLamina(self, ancho,espesor):

		print("Se esta produciendo en el tren laminador de 10 metros",ancho,espesor)

#*---Clase cuboid  con sus propiedades pero con método de fabricación flexible
 
class Lamina:

	def __init__(self, ancho,espesor, producingAPI):

		self._ancho = ancho
		self._espesor = espesor


		self._producingAPI = producingAPI

#*---- cuando se invoca la producción invoca al objeto cuyo puntero se almacenó al crear

	def produce(self):

		self._producingAPI.produceLamina(self._ancho,self._espesor)


	def setproducingAPI(self, producingAPI):

		self._producingAPI = producingAPI


#*-----------------------------------------------------------
#* main
#*-----------------------------------------------------------

os.system("clear")

#*--- implementa un primer cuboide y le asigna ProducingAPI1()
lamina1 = Lamina(0.5,1,ProducingLamina5mt())
lamina1.produce()

#*--- implementa un segundo cuboide y le asigna ProducingAPI2()
lamina2 = Lamina(0.5,1, ProducingLamina10mt())
lamina2.produce()



print("\n Cambia método de producción en run-time API2->API1\n")
lamina2.setproducingAPI(ProducingLamina5mt())
lamina2.produce()