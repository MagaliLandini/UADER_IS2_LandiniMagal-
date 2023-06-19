# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json
import sys
import random

def ayuda():
    print('-Para ejecutar el archivo es necesario que le pases un archivo json con los token')
    print('-el archivo devolvera un token a utilizar')
    print('-Si hay mas de dos token en el json se debe modificar el programa para que los lea')
try:
    jsonfile = sys.argv[1]
    if (jsonfile == '-h'):
        ayuda()
    else:
        # jsonkey = sys.argv[2]
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        index = random.randint(1, 2)
        print(str(obj['token' + str(index)]))
        # okay decompiling getJason.pyc
except:
    print('Debes ingresar una fuente de tokens o -h para obtener ayuda')


