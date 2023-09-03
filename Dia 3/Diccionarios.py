diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Perez','peso':88,'talla':1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())

dic3 = {1:'a',2:'b'} #Agregar una nueva clave a un diccionario
print(dic3)

dic3[3] = 'c'
print(dic3)

dic3[2] = 'B'
print(dic3)

print(dic3.keys()) #Conocer todas las claves que hay en un diccionario
print(dic3.values()) #Conocer todos los valores de un diccionario
print(dic3.items()) #Conocer todos lo que hay en un diccionario