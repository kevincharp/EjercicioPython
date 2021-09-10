#Ejercicio_2
print ('Pedir el radio de un circulo y calcular su area y longitud')
radio = float (input('Ingresar radio '))
import math
area = math.pi * radio **2
longitud = 2 * math.pi * radio
print (f'El area es {area:.2f}')
print (f'La longitud es {longitud:.2f}')