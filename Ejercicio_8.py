#Ejercicio 8

num = (int(input('Ingrese numero ')))

if num >= 0:

    if str(num) == str(num)[::-1]:
        print('%i es capicua' % num)
    else:
        print('%i no es capicua' % num)