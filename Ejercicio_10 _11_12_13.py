# Ejercicio_10 Pedir el dia, mes y año e indicar si la fecha es correcta suponiendo que todos los meses son de 30 dias
# Ejercicio_11 Pedir el dia, mes y año de una fecha correcta y mostrar la fecha siguiente
# Ejercicio_12 Pedir el dia, mes y año de una fecha correcta y mostrar la fecha siguiente suponiendo que todos los meses son de 30 dias
# Ejercicio_13 Pedir el dia, mes y año de una fecha correcta y mostrar la fecha siguiente

from datetime import datetime
from datetime import timedelta
while True:
    try:
        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        format_date = "%d-%m-%Y"
        fecha_ing = datetime.strptime(fecha, format_date)
        print('la fecha que usted ingreso es: ', fecha)
        fecha_sig = fecha_ing + timedelta(days=1)
        fecha_sig = fecha_sig.strftime('%d-%m-%Y')
        print('la fecha siguiente es:  ', fecha_sig)
        break
    except ValueError:
        print("Fecha inválida")
