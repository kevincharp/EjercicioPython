#Ejercicio_6
print('Ordenar numeros de menor a mayor')
numeros = []
numeros.append (int(input('Ingrese primer numero ')))
numeros.append (int(input('Ingrese segundo numero ')))
numeros.append (int(input('Ingrese tercer numero ')))
numeros.sort(reverse=True)
print (numeros)