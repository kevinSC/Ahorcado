import time
import os
from os import listdir
def prinIntro(movie):
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
def showMenu(menu, message = ""):
    '''
    Esta funcion imprime un menu con con sus respectivas opcines.
    recibe como paramentros un diccionario de opciones deseadas a desplegar
    y un string como mensaje
    '''
    print(message)
    print('----------------------------------------------------------------')
    for key, value in menu.items():
        print(value+':', key, end = " | ")
    print('\n----------------------------------------------------------------')
def showInstructions(instructions):
    os.system('more '+instructions)
def dirFiles(path):
    temas = listdir(path)
    numbes = range(1,len(temas)+1)
    return dict(zip(numbes, temas))
#def printIntro(fileName):
def loadWords(path):
    '''
    Firma:
        (string) -> (string)

    Sinopsis:
        Función que solicita el nombre de un archivo cualquiera y devuelve una cadena 
        de caracteres con su contenido

    Entradas y salidas:
        - filename: string que contiene el nombre del archivo con las palabras secretas
        - returns: string con todas las palabras secretas

    Ejemplos de uso:
        >>> loadWords("superHeroes.txt")
        'capitan centella, capitan planeta, batman, superman, robin, mujer maravilla, aquaman, flash,
        cyborg, capitan marciano, linterna verde,flash gordon, liga de la justicia, defensores de la 
        tierra, el fantasma, spider man, hulk, thor, iron man, los vengadores, robocop, terminator, 
        capitan america, hombre hormiga, la avispa, goku, vegeta, gohan, piccolo, trunks, spawn, 
        tintin, ghost rider, blade, tortugas ninja, soldado del invierno, el castigador, 
        el predicador, leonidas, kick ass, el comediante, el chapulin colorado, wolverine,
        flecha verde, el profesor super o, los autobots, robin hood\n'

    '''

    # Desarrolle el cuerpo de la función aquí... 
    words=''
    file = open(path)
    for line in file:
        words += line
    file.close()
    # Cadena retornada
    return words
    


#    '''
#    Firma:
#        (string)
#
#    Sinopsis:
#        función que imprime el contenido de un archivo en pantalla, en este 
#       caso, el mensaje de bienvenida al juego
#
#    Entradas y salidas:
#        - inputFile: Nombre del archivo que contiene la presentación del juego
#        - returns: None, solo imprime el archivo leído en pantalla
#
#    Ejemplos de uso:
#
#        >>> printIntro("intro.txt")
#        ___  _                             _             +---+ 
#       / _ \| |                           | |            |   | 
#      / /_\ \ |__   ___  _ __ ___ __ _  __| | ___        O   |    
#      |  _  | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \      /|\  |    
#      | | | | | | | (_) | | | (_| (_| | (_| | (_) |     / \  |
#      \_| |_/_| |_|\___/|_|  \___\__,_|\__,_|\___/           |  
#                                                      =========
#    '''
#
#    # Desarrolle el cuerpo de la función aquí...
#
#
#
#
#def inputSecret():
#    '''
#    Firma:
#        () -> (string)
#
#    Sinopsis:
#        Función que solicita al usuario la palabra secreta
#
#    Entradas y salidas:
#        - inputs: None
#        - returns: string con la palabra secreta ingresada por el usuario
#
#    Ejemplos de uso:
#
#        >>> p = inputSecret()
#        Ingrese la palabra o frase oculta: UdeA
#
#        >>> print(p)
#        UdeA 
#    '''
#
#    # Desarrolle el cuerpo de la función aquí... 
#
#
#    # Valor retornado
#    return pSec
#
#
#
#def countWords(palabras,separador):
#    '''
#    Firma:
#        (string,string) -> (int)
#
#    Sinopsis:
#        Función cuenta la cantidad de palabras o frases disponibles en una cadena
#
#    Entradas y salidas:
#        - palabras: Conjunto de palabras o frases separadas por un delimitador
#        - separador: Delimitador que separa una palabra o frase de otra dentro de la cadena de entrada (palabras)
#        - returns: cantidad de palabras secretas
#
#    Ejemplos de uso:
#        >>> materias = 'español,calculo,geometria vectorial,geometria euclidiana'
#        >>> countWords(materias,',')
#        4
#
#        >>> countWords('gallo-gallina','-')
#        2
#        '''
#
#    # Desarrolle el cuerpo de la función aquí...
#
#	# Retorno de la cantidad de palabras	
#    return conta   
#
#def pickWord(palabras,separador):
#    '''
#    Firma:
#        (string,string) -> (string)
#
#    Sinopsis:
#        Función que permite seleccionar una palabra o frase secreta correspondiente a una posicion 
#        dada de un conjunto de palabras separadas por un delimitador.  
#
#    Entradas y salidas:
#        - palabras: Conjunto de palabras o frases secretas separadas por un delimitador
#        - separador: Delimitador que separa una palabra o frase secreta de otra
#        - returns: Palabra o frase de la posiciónon elegida
#
#    Ejemplos de uso:
#        >>> x = 'homero_marge_bart_lisa_maggie' 
#        >>> pickWord(x,'_')
#        'homero'
#
#        >>> palabra = pickWord('marcos, lucas, mateo, juan',',')
#        >>> print(palabra)
#        'mateo'
        #
#    '''
#    # Desarrolle el cuerpo de la función aquí...
#    import random
#
#
#    # Eliminación de espacios de la palabra...
#    palabra = palabra.lstrip()
#    palabra = palabra.rstrip()
#
#    # Retorno de la palabra elegida
#    return palabra
#
#
#def obtenerParteAdivinada(palabraSecreta,letrasIntentadas):
#    '''
#    Firma:
#        (string,list) -> (string)
#
#    Sinopsis:
#        Imprime la parte de la cadena que ha sido adivinada.  
#
#    Entradas y salidas:
#        - palabraSecreta: string, palabra que el usuario esta adivinando
#        - letrasIntentadas: list, letras intentadas por el usuario para adivinar la palabra
#        - returns: string, compuesto de letras y caracteres raya bajo que representan las letras aun no adivinadas
#
#    Ejemplos de uso:
#        >>> palabraSecreta = 'perro'
#        >>> letrasIntentadas = ['a', 'e', 'i', 'o', 'u', 's', 'p']
#        >>> print obtenerParteAdivinada(palabraSecreta, letrasIntentadas)
#        'p e _ _ o'
#
#        >>> obtenerParteAdivinada('frodo', [])
#        '_ _ _ _ _'  
#
#    '''
#
#    # Desarrolle el cuerpo de la función aquí...
#
#    # Retorno de la palabra elegida
#    return pPrint       
#
#def obtenerLetrasDisponibles(letrasIntentadas):
#    '''
#    Firma:
#        (list) -> (string)
#
#    Sinopsis:
#        Devuelve las palabras que no se han empleado en los turnos.  
#
#    Entradas y salidas:
#        - letrasIntentadas: list, letras intentadas por el usuario para adivinar la palabra
#        - returns: string, compuesto de letras que no han sido ingresado
#
#    Ejemplos de uso:
#        >>> letrasIntentadas = ['a', 'b', 'f', 's']
#        >>> print obtenerLetrasDisponibles(letrasIntentadas)
#        cdeghijklmnopqrtuvwxyz
#
#    '''
#
#    # Desarrolle el cuerpo de la función aquí...
#    import string
#
#
#	# Retorno de las palabras del alfabeto que aun no han sido usadas
#    return resto
#
#def verificarLetraIngresada(letra,letrasIntentadas):
#    '''
#    Firma:
#        (bool) -> (string,list)
#
#    Sinopsis:
#        Devuelve True si la letra ingresada se encuentra dentro de la lista de palabras intentadas.  
#
#    Entradas y salidas:
#        - letra: Letra a verificar
#        - letrasIntentadas: Lista con las letras a comparar
#        - returns: La función devuelve False si ninguna la letra no se encuentra en ninguna de la 
#                   lista. En caso contrario, devuelve True.
#
#    Ejemplos de uso:
#        >>> letrasIntentadas = ['a', 'b', 'f', 's']
#        >>> verificarLetraIngresada('z',letrasIntentadas)
#        False
#
#        >>> verificarLetraIngresada('x',['v', 'w', 'x', 'y', 'z'])
#        True
#
#    '''
#
#    # Desarrolle el cuerpo de la función aquí... 
#
#def palabraAdivinada(palabra,letrasIntentadas):
#    '''
#    Firma:
#        (bool) -> (string,list)
#
#    Sinopsis:
#        Devuelve True si algunas o todas las letras de la lista pueden formar la palabra.  
#
#    Entradas y salidas:
#        - palabra: Palabra o frase a verificar
#        - letrasIntentadas: Lista con las letras a comparar
#        - returns: Devuelve True si con las letras de la lista pueden formar la palabra y False, en 
#             caso contrario.
#
#    Ejemplos de uso:
#        >>> palabraAdivinada('bilbo',['b','s','n','l','i','o'])
#        True
#
#        >>> palabraAdivinada('karman',['c','a','m',])
#        False
#
#    '''
#
#    # Desarrolle el cuerpo de la función aquí...