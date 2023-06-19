"""copyright IS2 © 2022,2023 todos los derechos reservados"""
import json
import sys
import random

if __debug__:
    print("__debug__ es true--> Codigo nuevo")
else:
    print("__debug__ es false-> Codigo viejo")
def ayuda():
    """Proporciona ayuda al usuario"""
    print('-Para ejecutar el archivo es necesario que le pases un archivo json con los token')
    print('-el archivo devolvera un token a utilizar')
    print('-Si hay mas de dos token en el json se debe modificar el programa para que los lea')

def codigo_viejo(file):
    """Codigo recuperado y modificado de getJason.pyc"""
    # jsonkey = sys.argv[2]
    with open(file, 'r',encoding="utf-8") as (myfile):
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
    def token(self, file):
        """si debug es true ejecuta el nuevo codigo, si no el viejo"""
        if __debug__:
            self.key.obtener_token(file)
        else:
            codigo_viejo(file)

class ClassToken:
    """creamos la clase token que contiene la nueva funcion para obtener tokens"""
    def __init__(self):
        self.name = "ClassToken constructor()"

    def obtener_token(self, file):
        """Obtiene el token a partir del archivo"""
        with open(file, 'r',encoding="utf-8") as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        index = random.randint(1, 2)
        print(str(obj['token' + str(index)]))
# creamos una instancia de token
t = AbstractToken()
# ejecutamos con try exepcion.
# la opcion -h nos devuelve la ayuda al usuario
try:
    JSON_FILE = sys.argv[1]
    if JSON_FILE == '-h':
        ayuda()
    else:
        t.token(JSON_FILE)
except IndexError:
    print('Debes ingresar una fuente de tokens o -h para obtener ayuda')
except FileNotFoundError:
    print('parametro incorrecto')
except json.decoder.JSONDecodeError:
    print('ingrese un archivo json')
