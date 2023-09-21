from random import *


# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


print("---------------------------------------")
from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados in range(7, 10):
        return  (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))


print("---------------------------------------")
# EJERCICIO DE CODIFICACION 101
from statistics import mean
def reducir_lista(lista_numeros):
    mi_set = set(lista_numeros)
    lista_nueva = list(mi_set)
    lista_nueva.pop(-1)
    return lista_nueva

def promedio(lista):
    prom = mean(lista)
    return prom

lista_numeros = [6, 8, 10, 7, 9, 8,11]
lista = reducir_lista(lista_numeros)
print(lista)


print("---------------------------------------")
# EJERCICIO DE CODIFICACION 102
def lanzar_moneda():
        moneda = ['Cara', 'Cruz']
        tiro = choice(moneda)
        return tiro

def probar_suerte2(tiro, lista_numeros2):
    if tiro == 'Cara':
        print('La lista se autodestruirá')
        lista_numeros2.clear()
        return lista_numeros2
    else:
        print('La lista fue salvada')
        return lista_numeros2

lista_numeros2 = [1, 2, 3]
tiro = lanzar_moneda()
probar_suerte2(tiro, lista_numeros2)
print(lista_numeros2)

