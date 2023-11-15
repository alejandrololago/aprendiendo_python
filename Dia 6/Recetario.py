from pathlib import Path
from os import system

def pedir_opcion():
    opcion = input("Por favor elija una de las siguiente opciones: \n 1-Leer receta \n 2-Crear receta \n 3-Crear categoria \n 4-Eliminar categoria \n 5-Eliminar categoria \n 6-Salir del recetario \n\n Opcion = ")
    return opcion


#def pedir_categoria():



def pedir_receta(ruta):
    for txt in Path(ruta).glob("**/*.txt"):
        print(txt)
    receta = input("Ingrese la receta elegida: ")
    return receta


def leer_receta(ruta):




#def eliminar_receta(receta):



#def eliminar_categoria(categoria):



#def crear_receta():




#def crear_categoria():






directorio = Path(Path.home(), "Documents", "Curso Python", "Dia 6", "Recetas")
opcion = 0

while opcion != 6:
    print('\n' + '*' * 20 + '\n')
    print("Bienvedido al recetario")
    print(f"Ruta de acceso al directorio: {directorio}")
    print('\n' + '*' * 20 + '\n')

    opcion = pedir_opcion()

    match opcion:
        case "1":
            ruta = Path(directorio, "Carnes")
            receta = pedir_receta(ruta)
            print(f"La receta elegida es: {receta}")
            #print("eligio 1")
            #system('cls')
        case "2":
            print("eligio 2")
            system('cls')
        case "3":
            print("eligio 3")
            system('cls')
        case "4":
            print("eligio 4")
            system('cls')
        case "5":
            print("eligio 5")
            system('cls')
        case "6":
            print("eligio 6")
            opcion = 6

