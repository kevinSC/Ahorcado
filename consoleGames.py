import time
import os
def showMovie(movie):
	''' recibe un archivo .txt con imagenes en codigo ascii y lo despliega
		en la pantalla de la consola mediante diapositivas
		
		NOTA: El archivo debe ser una imagenes en codi ascii y cada diapositiva
		y es separada por la palabra NEXT'''
	file = open(movie)
	for line in file:
		if line == 'NEXT\n':
			time.sleep(0.0625)
			os.system('clear')
		else:
			print(line, end = '')
	file.close()
def showMenu(menu, message, option):
	print(message)
	print('----------------------------------------------------------------')
	for key, value in menu.items():
		print(key+':', value, end = " | ")
	print('\n----------------------------------------------------------------')
	return option
def instructions(instructions):
	os.system('more '+instructions)
showMovie('movie.txt')
menu = {'a':1,'b':3}
showMenu(menu, "hola")
instructions('movie.txt')
	