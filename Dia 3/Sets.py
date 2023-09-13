#En un set solo puede haber elementos unicos, no puede haber repetidos, si hay repetidos deja uno solo
#Los elementos del set no estan ordenados en indices
#Los elementos son inmutables
mi_set = set([1,2,3,4,5])   # No puedo poner ni listas ni diccionarios dentro de un set Si se puede tuples porque son inmutables
print(mi_set)

otro_set = {1,2,3}
print(otro_set)

mi_set2 = set([1,2,3,4,5])
print(len(mi_set2)) #Puedo ver el largo del ser
print(2 in mi_set2) #Puedo consultar si algo se encuentra dentro del set

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(3) #Si quiero eliminar un elemento que no esta en el set me va a dar error
print(s1)

s1.discard(6) #El metodo discard no es igual que eliminar, si descarto un elemento que no esta en el set no dar error como si da error remove

s1.pop() #Aca el metodo no va a borrar el ultimo sino un elemento aleatorio
print(s1)

s1.clear() #Vacia el set
print(s1)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sor = sorteo.pop()
print(sor)


