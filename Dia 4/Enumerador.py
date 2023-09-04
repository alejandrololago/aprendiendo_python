lista = ['a','b','c']
for item in enumerate(lista):
    print(item)

print("---------------------------------------")
lista = ['a','b','c']
for indice,item in enumerate(lista):
    print(indice,item)

print("---------------------------------------")
for indice,item in enumerate(range(50,55)):
    print(indice,item)

print("---------------------------------------")
#Si queremos convertir una lista en una lista de tuples con el indice y el valor

lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)

print("---------------------------------------")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print("---------------------------------------")
lista_indices = list(enumerate("Python"))
print(lista_indices)

print("---------------------------------------")
lista_nombres2 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres2):
    if nombre[0].lower() == 'm':
        print(f"Indice: {indice}")




