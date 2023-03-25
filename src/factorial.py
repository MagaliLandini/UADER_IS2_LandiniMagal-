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
        while(num >= 1): 
            fact *= num 
            num -= 1
        return(fact)  
         
        
#Se le cambio la igualdad a 1 para que muestre el mensaje

if len(sys.argv) == 1:
   print("Debe informar un número!")
   sys.exit()
else:
#El condicional IF evalua el rango maximo que puede ingresar el usuario
    num=int(sys.argv[1])
    if(num > 60):
        print("Debe ingresar un número menor a 60")
        sys.exit
   

#Se agrego un ciclo for para que devuelva los factoriales entre dos rangos
for i in range (num, 60 +1):
    print("Factorial ",i,"! es ", factorial(i)) 

