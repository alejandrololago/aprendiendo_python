archivo = open("prueba1.txt", "w")

lista = ['hola','mundo','aqui','estoy']

for p in lista:
    archivo.writelines(p + '\n')

archivo.close()


print("---------------------------------------")
#Con a se escribe a partir del ultimo punto del archivo
archivo = open("prueba.txt", "a")

archivo.write('bienvenido')

archivo.close()


print("---------------------------------------")
archivo = open("registro.txt","a")
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for p in registro_ultima_sesion:
    archivo.writelines(p + "\t")
archivo.close()
archivo = open("registro.txt","r")
print(archivo.read())
archivo.close()