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
			aux = randint(1,10)
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
			elif aux == 6:
				return ('preguntas/uml/pregunta_6.txt')
			elif aux == 7:
				return ('preguntas/uml/pregunta_7.txt')
			elif aux == 8:
				return ('preguntas/uml/pregunta_8.txt')
			elif aux == 9:
				return ('preguntas/uml/pregunta_9.txt')
			elif aux == 10:
				return ('preguntas/uml/pregunta_10.txt')
		#Diseno
		elif cod == 2:
			aux = randint(1,16)
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
			elif aux == 6:
				return ('preguntas/diseno/pregunta_6.txt')
			elif aux == 7:
				return ('preguntas/diseno/pregunta_7.txt')
			elif aux == 8:
				return ('preguntas/diseno/pregunta_8.txt')
			elif aux == 9:
				return ('preguntas/diseno/pregunta_9.txt')
			elif aux == 10:
				return ('preguntas/diseno/pregunta_10.txt')
			elif aux == 11:
				return ('preguntas/diseno/pregunta_11.txt')
			elif aux == 12:
				return ('preguntas/diseno/pregunta_12.txt')
			elif aux == 13:
				return ('preguntas/diseno/pregunta_13.txt')
			elif aux == 14:
				return ('preguntas/diseno/pregunta_14.txt')
			elif aux == 15:
				return ('preguntas/diseno/pregunta_15.txt')
			elif aux == 16:
				return ('preguntas/diseno/pregunta_16.txt')
		
		#Conceptos		
		elif cod == 3:
			aux = randint(1,15)
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
			elif aux == 6:
				return ('preguntas/conceptos/pregunta_6.txt')
			elif aux == 7:
				return ('preguntas/conceptos/pregunta_7.txt')
			elif aux == 8:
				return ('preguntas/conceptos/pregunta_8.txt')
			elif aux == 9:
				return ('preguntas/conceptos/pregunta_9.txt')
			elif aux == 10:
				return ('preguntas/conceptos/pregunta_10.txt')
			elif aux == 11:
				return ('preguntas/conceptos/pregunta_11.txt')
			elif aux == 12:
				return ('preguntas/conceptos/pregunta_12.txt')
			elif aux == 13:
				return ('preguntas/conceptos/pregunta_13.txt')
			elif aux == 14:
				return ('preguntas/conceptos/pregunta_14.txt')
			elif aux == 15:
				return ('preguntas/conceptos/pregunta_15.txt')

		#Historia
		elif cod == 4:
			aux = randint(1,10)
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
			elif aux == 6:
				return ('preguntas/historia/pregunta_6.txt')
			elif aux == 7:
				return ('preguntas/historia/pregunta_7.txt')
			elif aux == 8:
				return ('preguntas/historia/pregunta_8.txt')
			elif aux == 9:
				return ('preguntas/historia/pregunta_9.txt')
			elif aux == 10:
				return ('preguntas/historia/pregunta_10.txt')
