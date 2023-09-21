def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(8,8))

print("---------------------------------------")
# Otra forma mas corta
def suma(*args):
    return sum(args)

print(suma(9, 9))


