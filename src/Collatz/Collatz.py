import matplotlib.pyplot as plt
import numpy as np


def collatz(numero):
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
    return iteraciones

#Se crearon dos array que guarden los valores que va tomando x e y

x=[]
y=[]    
for i in range (1,10000):
    y.append(collatz(i))
    x.append(i)
print(x)
print(y)


# X axis parameter:
xaxis = np.array(x)

# Y axis parameter:
yaxis = np.array(y)
#Se uso scatter para que grafique puntos y no lineas
plt.scatter(xaxis, yaxis)
plt.xlabel("N° de partida")
plt.ylabel("iteraciones")
plt.show()