#Realiza imports de pygame y python
import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *

class Pregunta (Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.codigo = 0
	
	#Lee la pregunta de un archivo txt	
	def leerPregunta(self,nombre_archivo):
		pregunta = open(nombre_archivo,"r")
		arreglo=[]
		
		#Guarda la linea en un arreglo
		for linea in pregunta.readlines():
			for i in range(1):
				arreglo.append(linea)
		pregunta.close()
		return arreglo
		
	def asignarPregunta(self,cod):
		#UML
		if cod == 1:
			aux = randint(1,5)
			if aux == 1:
				return ('preguntas/uml/pregunta_1.txt')
			elif aux == 2:
				return ('preguntas/uml/pregunta_2.txt')
			elif aux == 3:
				return ('preguntas/uml/pregunta_3.txt')
			elif aux == 4:
				return ('preguntas/uml/pregunta_4.txt')
			elif aux == 5:
				return ('preguntas/uml/pregunta_5.txt')
		#Diseno
		elif cod == 2:
			aux = randint(1,5)
			if aux == 1:
				return ('preguntas/diseno/pregunta_1.txt')
			elif aux == 2:
				return ('preguntas/diseno/pregunta_2.txt')
			elif aux == 3:
				return ('preguntas/diseno/pregunta_3.txt')
			elif aux == 4:
				return ('preguntas/diseno/pregunta_4.txt')
			elif aux == 5:
				return ('preguntas/diseno/pregunta_5.txt')
		#Conceptos		
		elif cod == 3:
			aux = randint(1,5)
			if aux == 1:
				return ('preguntas/conceptos/pregunta_1.txt')
			elif aux == 2:
				return ('preguntas/conceptos/pregunta_2.txt')
			elif aux == 3:
				return ('preguntas/conceptos/pregunta_3.txt')
			elif aux == 4:
				return ('preguntas/conceptos/pregunta_4.txt')
			elif aux == 5:
				return ('preguntas/conceptos/pregunta_5.txt')

		#Historia
		elif cod == 4:
			aux = randint(1,5)
			if aux == 1:
				return ('preguntas/historia/pregunta_1.txt')
			elif aux == 2:
				return ('preguntas/historia/pregunta_2.txt')
			elif aux == 3:
				return ('preguntas/historia/pregunta_3.txt')
			elif aux == 4:
				return ('preguntas/historia/pregunta_4.txt')
			elif aux == 5:
				return ('preguntas/historia/pregunta_5.txt')
