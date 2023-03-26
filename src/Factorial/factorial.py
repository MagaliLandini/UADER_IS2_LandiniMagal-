#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#Se le cambio la igualdad por 0 para que solicite que informe un numero
if len(sys.argv) == 1:
   print("Debe informar un número!")
   sys.exit()
else:
    num=int(sys.argv[1])
    num2=int(sys.argv[2])



#Se agrego un ciclo for para que devuelva los factoriales entre dos rangos
for i in range (num, num2 + 1):
    print("Factorial ",i,"! es ", factorial(i)) 