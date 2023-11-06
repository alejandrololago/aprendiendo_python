import os

ruta = os.chdir("C:\\Users\\Ale\\Documents\\GitHub\\aprendiendo_python\\Alternativo")

archivo = open('otro_archivo.txt')
print(archivo.read())

print("---------------------------------------")
#PARA CREAR CARPETA
ruta = os.makedirs("C:\\Users\\Ale\\Documents\\GitHub\\aprendiendo_python\\Alternativo\\Otra")

archivo.close()


print("---------------------------------------")
ruta2 = ("C:\\Users\\Ale\\Documents\\GitHub\\aprendiendo_python\\Dia 6\\Prueba.txt")

elemento = os.path.basename(ruta2)
print(elemento)

elemento2 = os.path.dirname(ruta2)
print(elemento2)

elemento3 = os.path.split(ruta2)
print(elemento3)


print("---------------------------------------")
#ELIMINAR CARPETA

os.rmdir("C:\\Users\\Ale\\Documents\\GitHub\\aprendiendo_python\\Alternativo\\Otra")


print("---------------------------------------")
#ABRIR ARCHIVO SIN USAR OS COLOCANDO LA RUTA

otro_archivo = open("C:\\Users\\Ale\\Documents\\GitHub\\aprendiendo_python\\Alternativo\\otro_archivo.txt")
otro_archivo.close()

print("---------------------------------------")
from pathlib import Path

carpeta = Path("C:/Users/Ale/Documents/GitHub/aprendiendo_python/Alternativo")
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

#OTRA OPCION MAS CORTA
carpeta = Path("C:/Users/Ale/Documents/GitHub/aprendiendo_python/Alternativo") / 'otro_archivo.txt'