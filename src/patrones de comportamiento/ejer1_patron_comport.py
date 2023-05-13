#!/usr/python
import os
import sys
#*--------------------------------------------------------------------
#* Implementación de chain of responsibility determina si un numero es primo,
#* par o ninguno
#*--------------------------------------------------------------------
class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        if self.nextHandler == None:
           print("La lista de actuadores se ha terminado, no se puede resolver el formato")
           return
        self.nextHandler.handle(request)

#*-------------------------------- Primo Handler

class PrimoHandler(Handler):

    def handle(self, request):
        print("Handler primo:(%s)" % request)
        
        def primo (num):
            if num < 2:
                return False
            for i in range (2,num):
                if num % i == 0:
                    return False
            return True
        if primo(num) ==  True:
            print('es primo')
        else:
            print("Handler primo: pasa al siguiente actuador")
            super(PrimoHandler, self).handle(request)


#*-------------------------------- Par Handler

class ParHandler(Handler):
    def handle(self, request):
        print("Handler par: (%s)" % request)
        par = (request // 2)*2
        if request  == par:
            print('es par')
        else:
            print("Handler par: pasa al siguiente actuador")
            super(ParHandler, self).handle(request)

#*-------------------------------- No consumido Handler 

class NoConsumidotHandler(Handler):
    def handle(self, request):
        print('No consumido')
      
#*-------------------------------- Word Handler

class ErrorHandler(Handler):

    def handle(self, request):
        print ("Invalid request")




if __name__ == '__main__':

    os.system("clear")
#*---------------------------------------------------------------
#* Inicializa los actuadores de formatos conocidos
#*---------------------------------------------------------------
    primo_handler = PrimoHandler()
    par_handler = ParHandler()
    ninguno_handler = NoConsumidotHandler()

#*---- Establece ahora la cadena de llamada

   
    for i in range (100):
        num = i
        primo_handler.nextHandler = par_handler
        par_handler.nextHandler= ninguno_handler
        primo_handler.handle(num)
