lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: " + letra)

print("---------------------------------------")
lista2 = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

print("---------------------------------------")
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

print("---------------------------------------")
palabra = 'python'

for letra in palabra:
    print(letra)

print("---------------------------------------")
mi_lista = [[1, 2], [3, 4], [5, 6]]
for objeto in mi_lista:
    print(objeto)

for a, b in mi_lista:
    print(a)
    print(b)

print("---------------------------------------")
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic:   #Solamente se imprimen las claves
    print(item)

for item in dic.items():   #Se imprimen los items completos
    print(item)

for item in dic.values():   #Se imprimen los valores
    print(item)

for a,b in dic.items():   #Distinta manera de ver claves y valores
    print(a,b)


lista_numeros = [2,1,4,3,3,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
print(f"Pares: {suma_pares} Impares: {suma_impares}")