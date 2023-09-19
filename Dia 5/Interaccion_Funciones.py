from random import shuffle

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

