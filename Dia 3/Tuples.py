mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2][0])

mi_tuple = list(mi_tuple) #Puedo castear el tuple a una lista
print(type(mi_tuple))

t = (1,2,3)
x,y,z = t
print(x,y,z)

t1 = (1,2,3,1)

print(t1.count(1)) #Metodo para saber cuantas veces aparece un elemento
print(t1.index(2)) #Metodo para saber en que indice esta cierto valor
