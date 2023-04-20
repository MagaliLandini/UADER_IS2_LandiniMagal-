import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el fusilaje
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Turbinas
      engine = self.__builder.getEngine()
      avion.setEngine(engine)

      # tren de aterrizaje
      alas = self.__builder.getAla()
      avion.setAlas(alas)

      # tren de aterrizaje
      tren = self.__builder.getTren()
      avion.attachTren(tren)

      # Retorna el avion completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__tren = None
      self.__engine = None
      self.__body = None
      self.__ala = None

   def setBody(self, body):
      self.__body = body

   def attachTren(self, tren):
      self.__tren=tren

   def setEngine(self, engine):
      self.__engine = engine

   def setAlas(self, ala):
      self.__ala = ala

   def specification(self):
      print ("fuselaje: %s" % (self.__body.shape))
      print ("Turbina: %d" % (self.__engine.turbina))
      print ("Tren de aterrizaje: %d\'" % (self.__tren.tren_aterrizaje))
      print ("Cantidad de alas: %d\'" % (self.__ala.cant_ala))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getTren(self): pass
      def getEngine(self): pass
      def getBody(self): pass
      def getAla(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un avion
#* Establece instancias para tomar tren, fusilaje, alas y turbina
#* estableciendo las partes específicas que (en un avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   
   def getTren(self):
      tren = Tren()
      tren.tren_aterrizaje = 1
      return tren
   
   def getEngine(self):
      engine = Engine()
      engine.turbina = 2
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "semi-monocasco"
      return body

   def getAla(self):
      ala = Ala()
      ala.cant_ala = 2
      return ala
#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------
class Tren:
   tren_aterrizaje = None

class Engine:
   turbina = None

class Body:
   shape = None

class Ala:
   cant_ala = None
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un avion
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un avion según
#* la hoja de ruta
#*----------------------------------------------------------------
   avion = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   avion.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion")

   main()
