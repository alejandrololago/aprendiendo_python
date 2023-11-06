from pathlib import Path

base = Path.home()
ruta = Path(base,"Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
ruta2 = ruta.with_name("La_Pedrera.txt")

print(ruta)
print(ruta2)

print("---------------------------------------")

print(ruta.parent.parent)

print("---------------------------------------")

guia = Path(Path.home(), "Documents","GitHub", "aprendiendo_python", "Dia 6", "Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)

print("---------------------------------------")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

print("---------------------------------------")

ruta = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = ruta.relative_to(Path("Europa"))
en_espania = ruta.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
