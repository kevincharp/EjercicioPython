#Pedir un numero de 0 al 9999 y decir cuantas cifras tienes 
num = (int(input('Ingrese numero ')))
cont = 0
while num != 0:
    num //= 10
    cont += 1

print (f'El numero ingresado tiene {cont} cifras')