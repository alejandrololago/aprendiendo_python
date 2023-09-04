nombres = ['Ana','Hugo','Valeria']
edades = [30,25,20]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

print("---------------------------------------")
for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')


print("---------------------------------------")
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados2 = list(zip(capitales,paises))
for capital,pais in combinados2:
    print(f'La capital de {pais} es {capital}')


print("---------------------------------------")
numeros_espanol = ['uno','dos','tres','cuatro','cinco']
numeros_portugues = ['um','dois','três','quatro','cinco']
numeros_ingles = ['one','two','three','four','five']

numeros = list(zip(numeros_espanol,numeros_portugues,numeros_ingles))
print(numeros)