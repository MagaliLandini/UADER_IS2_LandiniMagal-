import matplotlib.pyplot as plt
import numpy as np

numero = int(input("Ingrese un numero: "))
x=numero
#guarda el N° de iteraciones que llevo calcular la conjetura
iteraciones= 1
#guarda todos los valores que se fueron obteniendo en cada paso
arry=[]

#Calcula la conjetura de collatz
arry.append(numero)
while numero != 1:
    iteraciones +=1
#si es par ingresa al if
    if numero % 2 == 0:
        numero = numero / 2
        arry.append(numero)
#si es impar ingresa al else
    else:
        numero = (numero * 3) + 1
        arry.append(numero)


    
#Para graficar usamos matplotlib
print(arry)

# X axis parameter:
xaxis = np.array([x])

# Y axis parameter:
yaxis = np.array([iteraciones])

plt.scatter(xaxis, yaxis)
plt.xlabel("N° de partida")
plt.ylabel("iteraciones")
plt.show()