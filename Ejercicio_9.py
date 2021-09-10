#Pedir una nota en numero y decir si es Insuficiente, Suficiente, Bien, Muy Bien, Exelente
num = int(input('Ingrese nota del 1 al 10: '))
if num <= 3:
    print('NOTA INSUFICIENTE')
if num <= 5:
    print('NOTA SUFICIENTE')
if num <= 7:
    print('NOTA BIEN')
if num <= 9:
    print('NOTA MUY BIEN')
if num == 10:
    print('NOTA EXELENTE')
if num > 10:
    print('Calificacion invalida')
