#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial_OOP:
#funcion que calcula el factorial
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
#funcion que calcula el factorial entre dos extremos
    def run(min,max):
        for i in range (min, max +1):
            calculo= Factorial_OOP.factorial(i)
            print("Factorial ",i,"! es ", calculo) 

        
#Se le cambio la igualdad a 1 para que muestre el mensaje

if len(sys.argv) == 1:
   print("Debe informar un número!")
   sys.exit()
else:
    num=int(sys.argv[1])
    num2=int(sys.argv[2])
   
#Se llama la clase factorial_OOP para que calcule el factorial entre extremos dados
Factorial_OOP.run(num,num2)
