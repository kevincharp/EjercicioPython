#Ejercicio 16 Realizar un programa que cuente los numeros pares entre el 1 y un numero ingresado por el usuario

num = int(input('Intruzca un numero y se le dira cuales son y cuantos numeros pares son los que hay entre 1 y el numero ingresado '))
print (f'Numero ingresado: {num}')

def numPar (lista):
    pares =[]

    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares

listpar = numPar ((list(range(1+1,num)))) 

(list(range(1+1, num)))
print (f'Los numeros pares entre 1 y {num} son: {listpar} ')
print ('Total de numeros pares entre estos son: ',(len(listpar)))





