#Realiza imports de pygame y python
import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *

#Realiza import locales
from casillas import *
import util

class Ficha (Sprite):
	def __init__(self):
		Sprite.__init__(self)
		#Inicializa los valores de la ficha
		self.puntos = 0
		self.image = util.cargar_imagen('imagenes/ficha.png')
		self.rect = self.image.get_rect()
		#Coordenadas de aparicion
		self.x = 90
		self.y = 440
		self.rect.move_ip(self.x,self.y)
	
	#Movimiento de la ficha
	def update(self,casilla):
		#Busca la coordenada en x
		if self.rect.x < casilla.coordenada_x:
			self.rect.x = self.rect.x + 1
		if self.rect.x > casilla.coordenada_x:
			self.rect.x = self.rect.x - 1
		#Busca la coordenada en y
		if self.rect.y < casilla.coordenada_y:
			self.rect.y = self.rect.y + 1
		if self.rect.y > casilla.coordenada_y:
			self.rect.y = self.rect.y - 1
	
	#Compara la posicion de la ficha y la casilla
	def comparar(self,casilla):
		if self.rect.x == casilla.coordenada_x and self.rect.y == casilla.coordenada_y:
			return True
		else:
			return False
		
