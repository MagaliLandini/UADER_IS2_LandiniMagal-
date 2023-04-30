import os
#*--------------------------------------------------------------------
#* Ejemplo de pattern composite
#* Se genera una clase LeafElement que representa nodos terminales y una
#* CompositeLement que representa al arbol (de CompositeElement y LeafElement)
#* que de el dependen.
#*--------------------------------------------------------------------

#*------------- Define una clase para los nodos terminales (leaf)
#torta:tiene bizcochuelo(leche,harina,huevo,azucar), merengue(clara de huevo,azucar,agua), dulce de leche(leche,azucar,canela), 
class LeafElement:

	def __init__(self, *args):

#*--- indenta las posiciones a medida que se agregan
		self.position = args[0]

#*--- lista elementos

	def showDetails(self):

		'''Prints the position of the child element.'''
		print("\t", end ="")
		print(self.position)

#*---- Elemento compuesto, representa objetos en cualquier nivel de la jerarquia excepto el último

class CompositeElement:

	def __init__(self, *args):

		self.position = args[0]
		self.children = []

#*----- Crea jerarquia

	def add(self, child):

		self.children.append(child)

#*---- Remueve jerarquia

	def remove(self, child):

		self.children.remove(child)

#*---- muestra detalles (itera a los niveles inferiores


	def showDetails(self):

		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":

    os.system("clear")

#*------ Crea el top level de la jerarquia

    topLevelMenu = CompositeElement("Torta")

#*----- Crea el primer producto

    subMenuItem1 = CompositeElement("Bizcochuelo")
    subMenuItem2 = CompositeElement("Dulce de leche")
    subMenuItem3 = CompositeElement("Merengue")


    subMenuItem11 = LeafElement("leche")
    subMenuItem12 = LeafElement("harina")
    subMenuItem13 = LeafElement("huevo")
    subMenuItem14= LeafElement('azucar')

    subMenuItem21 = LeafElement("leche")
    subMenuItem22 = LeafElement("azucar")
    subMenuItem23 = LeafElement("vainilla")
    subMenuItem24= LeafElement('canela')

    subMenuItem31 = LeafElement("clara de huevo")
    subMenuItem32 = LeafElement("azucar")
    subMenuItem33 = LeafElement("esencia")

    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem1.add(subMenuItem13)
    subMenuItem1.add(subMenuItem14)

    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem23)
    subMenuItem2.add(subMenuItem24)

    subMenuItem3.add(subMenuItem31)
    subMenuItem3.add(subMenuItem32)
    subMenuItem3.add(subMenuItem33)

#*---- Agregando subconjunto opcional
    subMenuItem4 = CompositeElement("Ingrediente adicionales que puedes agregarle")

    subMenuItem41 = LeafElement("roclets")
    subMenuItem42 = LeafElement("chips de chocolate")
    subMenuItem43 = LeafElement("grajeas")
    subMenuItem44= LeafElement('crocante de mani')

    subMenuItem4.add(subMenuItem41)
    subMenuItem4.add(subMenuItem42)
    subMenuItem4.add(subMenuItem43)
    subMenuItem4.add(subMenuItem44)
#*---- Agrega ahora las dos gerencias al nivel raiz

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.add(subMenuItem3)
    topLevelMenu.add(subMenuItem4)


#*---- Muestra el resultado
    topLevelMenu.showDetails()
