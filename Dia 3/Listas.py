mi_lista = ['a','b','c']
resultado = len(mi_lista)
print(resultado)
print(mi_lista[1])
print(mi_lista[0:2])

mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)

eliminado = mi_lista3.pop(0) #Si lo dejo vacio elimina el ultimo elemento
print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort() #Metodo para ordenar lista
print(lista)

lista.reverse() #Metodo que ordena lista al reves
print(lista)

