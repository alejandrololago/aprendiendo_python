##UPPER

texto = "Este es el texto de prueba"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

##LOWER

texto = "Este es el texto de prueba"
resultado = texto.lower()
print(resultado)

##SPLIT Para separar el texto en una lista

texto = "Este es el texto de prueba"
resultado = texto.split() ## Asi por defecto toma como separador a los espacion vacios
print(resultado)

texto = "Este es el texto de prueba"
resultado = texto.split("t") ## Asi se cambia el criterio de separacion que toma split
print(resultado)

##JOIN

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

##FIND

texto = "Este es el texto de prueba"
resultado = texto.find("s") ## Si no encuentra lo buscado arroja un -1
print(resultado)

##REPLACE

texto = "Este es el texto de prueba"
resultado = texto.replace("prueba", "Alejandro")
print(resultado)
