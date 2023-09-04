monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

print("---------------------------------------")
respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

"""
algo = ' '
while algo == ' ':
    pass     # Con esto puedo no poner nada aun en el while y el codigo pasa de largo
print("Algo")
"""

print("---------------------------------------")
nombre = input("Tu nombre")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)


print("---------------------------------------")
nombre = input("Tu nombre")
for letra in nombre:
    if letra == 'r':
        continue   #Continua con la iteracion siguiente
    print(letra)

