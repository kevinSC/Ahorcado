import ahorcado
import os
import time
ahorcado.printIntro('movie.txt')
ahorcado.showMenu({1:'Instrucciones',2:'Modos de juego'},'Por favor ingresa el numero de la opción que deseas:')
lives = 8
inputword = []
gameON = True
option = ahorcado.wrongImput({1:'Instrucciones',2:'Modos de juego'})
while option == 1:
	ahorcado.showInstructions()
	os.system('clear')
	ahorcado.printIntro('intro.txt')
	ahorcado.showMenu({1:'Instrucciones',2:'Modos de juego'},'Por favor ingresa el numero de la opción que deseas:')
	option = ahorcado.wrongImput({1:'Instrucciones',2:'Modos de juego'})
if option == 2:
	os.system('clear')
	ahorcado.printIntro('intro.txt')
	ahorcado.showMenu({1:'Un Jugador',2:'Dos Jugadores'},'Por favor ingresa el numero de la opción que deseas:')
	option = ahorcado.wrongImput({1:'Un Jugador',2:'Dos Jugadores'})
if option == 1:
	os.system('clear')
	print ('Selecciona un tema de la lista')
	for number, topic in ahorcado.dirFiles().items():
		print(number, ':', topic)
	word = ahorcado.pickWord(ahorcado.loadWords(ahorcado.selctDir(int(input(':')))))
elif option == 2:
	os.system('clear')
	word = input('Jugador 2 por favor ingresa una palabra:\n').lower()
	os.system('clear')
print('ok Comenzamos Jugador 1\n ingresa una letra despues de los 2 puntos')
time.sleep(3)
os.system('clear')
while gameON:
	disponibles = ahorcado.obtenerLetrasDisponibles(inputword)
	print(ahorcado.obtenerParteAdivinada(word,inputword))
	print('Las letras disponibles son:\n',disponibles)
	letrica=input(':')
	letrica = letrica.lower()
	verifica = ahorcado.verificarLetraIngresada(letrica,inputword)
	while verifica:
		print('por favor ingresa otra letra diferente, la', letrica, 'ya la ingresaste')
		letrica=input(':')
		letrica = letrica.lower()
		verifica = ahorcado.verificarLetraIngresada(letrica,inputword)
	inputword.append(letrica)
	if word.find(letrica)== -1:
		lives -= 1
		print(lives)
	if lives == 0:
		gameON = False
	else:
		gameON = not ahorcado.palabraAdivinada(word,inputword)
	#os.system('clear')
	


	
