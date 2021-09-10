#Ejercicio 15 Realizar un programa que pida un numero y se nos diga cuantos numeros hay entre 1 y el numero

num = int(input('Intruzca un numero y se le dira cuales y cuantos numeros son los que hay entre 1 y el numero ingresado '))

if num > 1:
    print (f'Los numeros entre 1 y {num} son ', (list(range(1+1, num))))
    print('Total de numeros entre estos son: ',(len(list(range(1+1, num)))))
else:
    print (f'Los numeros entre 1 y {num} son ',(list(range(num +1,1))))
    print ('Total de numeros entre estos son: ',(len(list(range(num +1,1)))))