texto = input("Ingrese un texto: ").lower()
letras = []

"""letra1 = input("Ingrese la 1ra letra: ").lower()
letra2 = input("Ingrese la 2da letra: ").lower()
letra3 = input("Ingrese la 3ra letra: ").lower()
letras = [letra1,letra2,letra3]
letra1_cant= texto.count(letra1)
letra2_cant= texto.count(letra2)
letra3_cant= texto.count(letra3)"""

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la primera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
letra1_cant = texto.count(letras[0])
letra2_cant = texto.count(letras[1])
letra3_cant = texto.count(letras[2])

print(f"Letra '{letras[0]}' aparece: {letra1_cant} veces")
print(f"Letra '{letras[1]}' aparece: {letra2_cant} veces")
print(f"Letra '{letras[2]}' aparece: {letra3_cant} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"La cantidad de palabras que hay en el texto es de: {len(palabras)}")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra es: {primera_letra}")
print(f"La ultima letra es: {ultima_letra}")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_alreves = " ".join(palabras)
print(texto_alreves)

print("\n")
print("BUSQUEDA PALABRA PYTHON")
busqueda_python = "python" in palabras
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[busqueda_python]} se encuentra en el texto")
