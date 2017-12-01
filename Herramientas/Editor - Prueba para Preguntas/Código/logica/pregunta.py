#Realiza imports de pygame y python
import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *

class Pregunta (Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.codigo = 0
		
	def leerPregunta(self,nombre_archivo):
		pregunta = open(nombre_archivo,"r")
		"""aux = pregunta.readline()"""
		arreglo=[]
		"""while aux != '':
			aux = pregunta.readline()"""
		
		for linea in pregunta.readlines():
			for i in range(1):
				arreglo.append(linea)
		"""print (arreglo)"""
		pregunta.close()
		return arreglo
		
