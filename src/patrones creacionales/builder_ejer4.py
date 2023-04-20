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
	   
   def getFactura(self,monto):
      factura = Factura()
      
      # Primero el importe
      importe = self.__builder.getImporte(monto)
      factura.setImporte(importe)
      
      # tipo de fatcura
      responsble = self.__builder.getCondicionImpositiva()
      factura.condicionImpositiva(responsble)
      
      # Retorna la factura completa
      return factura

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Factura:
      def __init__(self):
         self.importe = None
         self.condicion_impositiva = None

      def setImporte(self, importe):
         self.importe = importe

      def condicionImpositiva(self,condicion_impositiva):
        self.condicion_impositiva= condicion_impositiva

      def specification(self):
         importe =self.importe.size
         condicion=self.condicion_impositiva.condicion
         total=importe * condicion
         print(f"Factura: ", total)

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getImporte(self): pass
      def getCondicionImpositiva(self): pass


#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class FacturaBuilderIvaResponsable(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1.05
      return condicion2

class FacturaBuilderIvaExcento(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1.0
      return condicion2

class FacturaBuilderIvaNoInscripto(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1
      return condicion2

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Importe:
   size = None

class CondicionImpositiva:
   condicion = None


#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main(monto,responsable):

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   if responsable == "IVA Responsable":
      factura = FacturaBuilderIvaResponsable() # initializing the class
   elif responsable == "IVA No Inscripto":
      factura = FacturaBuilderIvaNoInscripto()
   elif responsable == "IVA Exento":
      factura = FacturaBuilderIvaExcento()
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(factura)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   factura = director.getFactura(monto)

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   factura.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")
   total=int(input('ingrese el total de la factura: '))
   responsable=str(input('ingrese el tipo de responsable incripto: '))
   main(total,responsable)
