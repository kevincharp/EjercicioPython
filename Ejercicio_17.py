#Ejercicio 17 Realizar un programa que cuente los numeros pares entre dos numero ingresado por el usuario

num1 = int(input('Intruzca un numero: '))
num2 = int(input('Intruzca un numero: '))
print (f'Numeros ingresados: {num1} y {num2}')

if num1 < num2:
    menor = num1    
    mayor = num2
else:
    menor = num2
    mayor = num1


def numPar (lista):
    pares =[]

    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares

listpar = numPar ((list(range(menor+1, mayor)))) 
(list(range(menor, mayor))) 

print (f'Los numeros pares entre {menor} y {mayor} son: {listpar} ')
print ('Total de numeros pares entre estos son: ',(len(listpar)))
