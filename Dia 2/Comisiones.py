nombre = input("Por favor dime tu nombre: ")
ventas = int(input("Dime tus ventas: "))

comision = round ((ventas*13)/100, 2)
print(f"La comision de {nombre} es de: {comision}")

