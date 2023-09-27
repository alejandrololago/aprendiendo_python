from random import choice

def elegir_palabra(lista):
    palabra = choice(lista)
    return palabra


def mostrar_guiones(palabra):
    cant_letras = len(palabra)
    cant = 0
    palabra_guiones = []
    while cant < cant_letras:
        palabra_guiones.append('_')
        cant += 1
    return palabra_guiones


def pedir_letra():
    letra = ""
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
    while letra not in abecedario:
        letra = input("Ingresa una letra: ").lower()
    return letra

def buscar_letra(letra, palabra):
    if letra in palabra:
        return True
    else:
        return False


def comprobar_completa(palabra_guiones):
    for p in palabra_guiones:
        if p != "_":
            continue
        else:
            return False
    return True


def rellenar_giones(letra, palabra, palabra_guiones):
    indice = 0
    for l in palabra:
        if l == letra:
            palabra_guiones[indice] = l
            indice += 1
        else:
            indice += 1
    return palabra_guiones

def jugar():
    palabra = elegir_palabra(["auto", "barco", "motocicleta"])
    vidas = 6
    palabra_guiones = mostrar_guiones(palabra)
    print(palabra_guiones)
    while vidas > 0:
        letra_elegida = pedir_letra()
        esta_letra = buscar_letra(letra_elegida,palabra)
        if esta_letra:
            if letra_elegida not in palabra_guiones:
                rellenar_giones(letra_elegida, palabra, palabra_guiones)
                if comprobar_completa(palabra_guiones):
                    print(f"Ganaste, la palabra es: {palabra_guiones}")
                    break
                else:
                    print(f"Acerstaste, la palabra va quedando asi {palabra_guiones}")
            else:
                print("Ya ingresaste esa letra")
        else:
            print("No acertaste")
            vidas -= 1
    if vidas == 0:
        print("Te quedaste sin vidas")


#palabra_elegida = elegir_palabra(["auto", "barco", "motocicleta"])
jugar()

