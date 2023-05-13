import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content
		

class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""
		self.history = [] # lista para almacenar los mementos anteriores

	def write(self, string):
		self.content += string


	def save(self):
		memento = self.history.append(Memento(self.file,self.content))
		return memento

	def undo(self, memento=None, history_index= 1):
		if len(self.history) >= history_index:
			memento = self.history[-history_index-1]
		else:
			return
			
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:


	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)
	
	print("Se graba información adicional")
	writer.write("Material adicional 2\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional 3\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)
	
	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("Estados historicos")


	writer.undo(history_index=0)
	print(writer.content)
	


