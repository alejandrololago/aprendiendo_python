# Ejercicio 1
def devolver_distintos(num1,num2,num3):
    lista_numeros = [num1, num2, num3]
    suma = sum(lista_numeros)
    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    else:
        lista_numeros.sort()
        return lista_numeros[1]

print(devolver_distintos(5,1,6))


print("---------------------------------------")
# Ejercicio 2
def cambiar_orden(palabra):
    set_palabra = set(palabra)
    palabra = list(set_palabra)
    palabra.sort()
    return palabra

print(cambiar_orden("entretenido"))


print("---------------------------------------")
# Ejercicio 3
def verificar_cero(*args):
    anterior = ""
    for arg in args:
        if anterior == arg and arg == 0:
            return True
        else:
            anterior = arg
    return False

print(verificar_cero(5,6,1,0,9,3,5))

#OTRA MANERA MAS OPTIMA
def verificar_veros(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador +1] == 0:
            return True
        else:
            contador += 1
    return False


print("---------------------------------------")
# Ejercicio 4
def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
            else:
                primos.append(iteracion)
                iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))





