def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(899)
print(resultado)



print("---------------------------------------")
def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)


print("---------------------------------------")
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n > 0:
            continue
        else:
            return False
    return True

resultado2 = todos_positivos([90,99,1,88])
print(resultado2)
