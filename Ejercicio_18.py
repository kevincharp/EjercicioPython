import getpass

print ('Cargando juego ahorcado...')
input ('Presione Enter para continuar')
print ('Jugador 1 debe escribir una palabra (la misma no se mostrara en pantalla)')
print ('Jugador 2 debera ingresar letras para adivinar la palabra escrita por el Jugador 1')
print ('Puede equivocarse 6 veces')
input ('Presione Enter para continuar')


palabra = getpass.getpass('Jugador 1 Ingrese palabra: ')
errores = 0

aciertos = []
for i in range(len(palabra)):
    aciertos.append("_ ")

palabraEspacio = []
for char in palabra:
    palabraEspacio.append(char + ' ')

letrasel = []
#Dibuja ahoracado por cada un error se agrega una parte del cuerpo
while errores < 7:
    if errores == 0:
        print(' _____ ')
        print(' |   | ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif errores == 1:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif errores == 2:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif errores == 3:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |  /  ')
        print(' |     ')
        print('---    ')
    elif errores == 4:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
    elif errores == 5:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |  /| ')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
    elif errores == 6:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |  /|\\')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
        print('Perdiste!')
        break
    print(''.join(aciertos))
    print("Letras usadas: ", letrasel)
    print('Selecciona una letra:')
    letra = input()
    if letra in letrasel:
        print('Esta letra ya la usaste')
    else:
        letrasel.append(letra)

        error = True
        for i in range(len(palabra)):
            if letra == palabra[i]:
                aciertos[i] = letra + ' '
                error = False
#suma a variable errores + 1 por cada error
        if error:
            errores += 1
        
        if palabraEspacio == aciertos:
            print(''.join(aciertos))
            print('Ganaste!')
            break