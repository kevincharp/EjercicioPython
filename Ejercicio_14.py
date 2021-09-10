#Ejercio_14 Diseñe una aplicacion que muestra las tablas de multiplicacion del 1 al 10 
tabla = int(input('Ingrese tabla de multiplicar a mostrar del 1 al 10' ))

for i in range(1, 11):
    print (f'{i} x {tabla} = {i * tabla}')