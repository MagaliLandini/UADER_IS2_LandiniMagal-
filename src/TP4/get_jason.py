"""copyright IS2 © 2022,2023 todos los derechos reservados"""
import json
import sys
import random
import os
from collections.abc import Iterable, Iterator
if __debug__:
    print("__debug__ es true--> Codigo nuevo")
else:
    print("__debug__ es false-> Codigo viejo")
saldo_cuenta=[1000,2000]

def ayuda():
    """Proporciona ayuda al usuario"""
    print('-Para ejecutar el archivo es necesario que le pases un archivo json con los token')
    print('-el archivo devolvera un token a utilizar')
    print('-Si hay mas de dos token en el json se debe modificar el programa para que los lea')


def codigo_viejo(file):
    """Codigo recuperado y modificado de getJason.pyc"""
    # jsonkey = sys.argv[2]
    with open(file, 'r', encoding="utf-8") as (myfile):
        data = myfile.read()
    obj = json.loads(data)
    index = random.randint(1, 2)
    print(str(obj['token' + str(index)]))
    # okay decompiling getJason.pyc


class AbstractToken:
    """Se crea la clase abstracta, en ella podemos
    elegir que codigo vamos a ejecutar(el viejo o el nuevo)"""

    def __init__(self):
        self.key = ClassToken()

    def token(self, file, num):
        """si debug es true ejecuta el nuevo codigo, si no el viejo"""
        if __debug__:
            return self.key.obtener_token(file, num)
        else:
            codigo_viejo(file)


class ClassToken:
    """creamos la clase token que contiene la nueva funcion para obtener tokens"""

    def __init__(self):
        self.name = "ClassToken constructor()"

    def obtener_token(self, file, num):
        """Obtiene el token a partir del archivo"""
        with open(file, 'r', encoding="utf-8") as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        cuenta = (obj['token' + str(num)])
        return str(cuenta)


class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request, file, pedido,collection):
        if self.nextHandler == None:
           print("La lista de actuadores se ha terminado, no se puede resolver el formato")
           return
        self.nextHandler.handle(request, file, pedido,collection)

# *-------------------------------- token 2


class Token1(Handler):

    def handle(self, request, file, pedido,collection):
        def cuenta1():
            return saldo_cuenta[0]
        if cuenta1()>= request:
            saldo_cuenta[0]=saldo_cuenta[0]- request
            t = AbstractToken()
            collection.add_item("Numero de Pedido: "+ str(pedido) + " Saldo: " +str(request)+" Cuenta con la que se realizo el pago: "+str(t.token(file, 1)))
        else:
            super(Token1, self).handle(request, file, pedido,collection)


# *-------------------------------- token 2

class Token2(Handler):
    def handle(self, request, file, pedido,collection):
        def cuenta2():
            return saldo_cuenta[1]
        if cuenta2() >= request:
            saldo_cuenta[1]=saldo_cuenta[1]-request
            t = AbstractToken()
            t.token(file, 2)
            collection.add_item("Numero de Pedido: "+ str(pedido) + " Saldo: " +str(request)+" Cuenta con la que se realizo el pago: "+str(t.token(file, 2)))
        else:
            super(Token2, self).handle(request, file, pedido,collection)


class NoConsumidotHandler(Handler):
    def handle(self, request, Null,pedido,collection):
        print('Sus cuentas no poseen saldo suficiente')


class Iterator2(Iterator):
    _index: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._index = -1 if reverse else 0

    def __next__(self):
        try:
            result = self._collection[self._index]
            self._index += -1 if self._reverse else 1
            return result
        except IndexError:
            print("<eol>")
            raise StopIteration


class Collection(Iterable):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator2(self._items)

    def get_reverse_iterator(self):
        return Iterator2(self._items, True)

    def add_item(self, item):
        self._items.append(item)


if __name__ == '__main__':
    os.system("clear")
# *---------------------------------------------------------------
# * Inicializa los actuadores de formatos conocidos
# *---------------------------------------------------------------
    collection = Collection()
    token_1 = Token1()
    token_2 = Token2()
    error_token = NoConsumidotHandler()
    # ejecutamos con try exepcion.
    # la opcion -h nos devuelve la ayuda al usuario
    try:
        JSON_FILE = sys.argv[1]
        if JSON_FILE == '-h':
            ayuda()
        else:
            i= str(input('¿Desea realizar una transaccion?: '))
            while i == 'si':
                pedido = int(input('Ingrese el numero del pedido de pago: '))
                saldo = int(input('Ingrese el monto a pagar: '))
                token_1.nextHandler = token_2
                token_2.nextHandler = error_token
                token_1.handle(saldo, JSON_FILE, pedido,collection)
                i= str(input('¿Desea realizar una transaccion: ?'))
            for item in collection:
                    print(item)
            print("\n")
            

    except IndexError:
        print('Debes ingresar una fuente de tokens o -h para obtener ayuda')
    except FileNotFoundError:
        print('parametro incorrecto')
    except json.decoder.JSONDecodeError:
        print('ingrese un archivo json')
    except KeyError:
        print('El numero ingresado no se encuentra en el archivo json')
