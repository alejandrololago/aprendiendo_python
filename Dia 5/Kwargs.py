def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))


print("---------------------------------------")
def prueba(num1 ,num2 , *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15, 50, 200, 300, 400,x='uno', y='dos', z='tres')


print("---------------------------------------")
def prueba(num1 ,num2 , *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15, 50, *args, *kwargs)


print("---------------------------------------")
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

print(cantidad_atributos(x='uno', y='dos', z='tres'))


print("---------------------------------------")
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(x='uno', y='dos', z='tres'))


print("---------------------------------------")
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")

    for clave,valor in kwargs.items():
        print(f"{clave} : {valor}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")

