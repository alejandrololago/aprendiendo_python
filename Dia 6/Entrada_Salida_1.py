mi_archivo = open('prueba.txt')

#print(mi_archivo.read())

print("---------------------------------------")

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

print("---------------------------------------")
mi_archivo = open('prueba.txt')

for l in mi_archivo:
    print("Aqui dice: " + l)

mi_archivo.close()


print("---------------------------------------")
mi_archivo = open('prueba.txt')

todas = mi_archivo.readlines()

print(todas)

mi_archivo.close()


print("---------------------------------------")
mi_archivo = open('prueba.txt')

for i, l in enumerate(mi_archivo.readlines()):
    if i == 1:
        print(l)

mi_archivo.close()