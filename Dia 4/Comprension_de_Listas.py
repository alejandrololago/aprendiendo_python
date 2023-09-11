palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

#Esto lo puedo resolver con menos codigo

lista2 = [letra for letra in palabra]
print(lista2)

lista3 = [letra for letra in 'python']
print(lista3)

print("---------------------------------------")
lista4 = [n for n in range(0,21,2)]
print(lista4)

print("---------------------------------------")
lista5 = [n * 2 for n in range(0,21,2)]
print(lista5)

print("---------------------------------------")
lista6 = [n for n in range(0,21,2) if n * 2 > 10]
print(lista6)

print("---------------------------------------")
lista7 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]     #Si pongo el else en la condicion, tengo que colocar la condicion adelante
print(lista7)

print("---------------------------------------")
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)

print("---------------------------------------")
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(gf -32)*(5/9) for gf in temperatura_fahrenheit]
print(grados_celsius)