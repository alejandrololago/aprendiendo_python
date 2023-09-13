def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)
print(resultado)


print("---------------------------------------")

def invertir_palabra(palabra):
    palabra = palabra.upper()
    lista = []
    for p in palabra:
        lista.append(p)
    lista.reverse()
    invertida_final = "".join(lista)
    return invertida_final

palabra = "Python"
print(invertir_palabra(palabra))

palabra = "Curso de Python"


print("---------------------------------------")
#Otro metodo mas sencillo
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

print(invertir_palabra("Curso de Python"))


print("---------------------------------------")
#Otro metodo sencillo
def invertir_sencillo(palabra):
    invertido = ""
    for p in palabra:
        invertido = p + invertido
    return invertido.upper()

print(invertir_sencillo(Python))