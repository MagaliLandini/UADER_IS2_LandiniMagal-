import os
#*--------------------------------------------------------------------
#* Ejemplo de pattern Proxy
#* La clase Door verifica una clave que solo puede ser lograda 
#* mediante la "encriptación" de una clave en texto claro
#*--------------------------------------------------------------------
from pythonping import ping
class Ping:
    def open_method(self) -> None:
        pass

    def operation(self, keystr,pin) -> None:
        print("la clave recibida (%s)" %(keystr))
        self.verify(keystr,pin)

    def verify(self, keystr,pin) -> None:
        if keystr == "192":
           print("acceso aceptado, puede proceder")
           self.execute(pin)
        else:
           print("acceso denegado")

    def execute(self,pin):
        for i in range(10):
            ping(pin, verbose=True)
        
    
    def executefree(self,pin):
        ping(pin, verbose=True)
class PingProxi:
    def __init__(self) -> None:
        self._klass = Ping()

    def open_method(self) -> None:
        print(f"Adding security measure to the method of {self._klass}")

    def operation(self,keystr,pin) -> None:
        if keystr == "192":
           newkey="636c6176650000000000000000000000"
        else:
           newkey=keystr
        print("la clave recibida por el proxy es (%s) la enviada es (%s)" % (keystr,newkey))
        self._klass.operation(newkey,pin)
    def execute(self,string,pin):
        if string == "192.168.0.254":
            self._klass.executefree('www.google.com')
        else:
            self._klass.execute(pin)

#*------------------------------------------------------------
#* main
#*------------------------------------------------------------

os.system("clear")
#*--Crea objeto que no se puede acceder directamente
door = Ping()
key="192"
pin='www.google.com'
door.operation(key,pin)


#*-- Crea objeto proxy
secured_door = PingProxi()
secured_door.open_method()
secured_door.operation(key,pin)
