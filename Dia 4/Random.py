from random import *

aleatorio = randint(1,50)
print(aleatorio)

print("---------------------------------------")
aleatorio2 = round(uniform(1,5),1)
print(aleatorio2)

print("---------------------------------------")
aleatorio3 = random()       #Elige un valor decimal (entre 0 y 1)
print(aleatorio3)

print("---------------------------------------")
colores = ['azul','rojo','verde','amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

print("---------------------------------------")
numeros = list(range(5,50,5))
shuffle(numeros)        #Mezcla la lista aleatoriamente
print(numeros)