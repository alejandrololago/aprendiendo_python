from random import randint

nombre = input("Cual es tu nombre: ")
nro_random = randint(1, 100)
intentos = 1
nro_elegido = 0

print(f"Bueno {nombre}, he pensado un numero entre el 1 y el 100 y tienes solo ocho intentos para adivinar cual es numero")
print(nro_random)

"""
termino = 'n'
while (intentos < 9) and (termino == 'n'):
    nro_elegido = int(input("Ingresa un numero: "))
    if (nro_elegido < 0) or (nro_elegido > 100):
        print("Elegiste un numero no permitido")
        intentos += 1
    elif (nro_elegido < nro_random):
        print("El numero que elegiste es menor")
        intentos += 1
    elif (nro_elegido > nro_random):
        print("El numero qu elegiste es mayor")
        intentos += 1
    else:
        print(f"Ganaste! El numero elegido es igual al de sistema que es: {nro_random} y te tomo {intentos} intentos")
        termino = 's'
if intentos == 9:
    print("Se te acabaron los intentos")
"""

while (intentos < 9):
    nro_elegido = int(input("Ingresa un numero: "))
    intentos += 1
    if nro_elegido not in range(1,101):
        print("Tu numero no se encuentra en el rango de 1 a 100")
    elif (nro_elegido < nro_random):
        print("El numero que elegiste es menor")
    elif (nro_elegido > nro_random):
        print("El numero qu elegiste es mayor")
    else:
        print(f"Ganaste! El numero elegido es igual al de sistema que es: {nro_random} y te tomo {intentos} intentos")
        break
#if intentos == 9:
#    print("Se te acabaron los intentos")
if nro_elegido != nro_random:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {nro_random}")



