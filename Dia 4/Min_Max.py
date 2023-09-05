lista = [58,96,78,89]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

print("---------------------------------------")
nombres = ['juan','pablo','alicia','carlos']
print(min(nombres))

print("---------------------------------------")
nombre = "Carlos"
print(min(nombre.lower()))      #Primero busca en las letras mayusculas y luego en las minusculas

print("---------------------------------------")
dic = {'C1':45,'C2':11}
print(min(dic))
print(min(dic.values()))

print("---------------------------------------")
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(f"Edad minima: {edad_minima} Ultimo nombre: {ultimo_nombre}")