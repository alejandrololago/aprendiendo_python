dic = {'clave1':100,'clave2':500}

a = dic.popitem()
print(a)
print(dic)

print("---------------------------------------")

frase = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(frase.lstrip(',:%_# '))

print("---------------------------------------")

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

print("---------------------------------------")

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)