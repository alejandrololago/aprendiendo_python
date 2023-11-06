from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/Ale/Documents/GitHub/aprendiendo_python/Dia 6/Prueba.txt")

print(carpeta.read_text())


print("---------------------------------------")

print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genia, existe")


print("---------------------------------------")
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)