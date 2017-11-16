#Realiza imports de pygame y python
import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
import util

class Casilla (Sprite):
	def __init__(self,coord,cod):
		Sprite.__init__(self)
		#Asigna coordenadas a las casillas
		self.coordenada_x = coord[0]
		self.coordenada_y = coord[1]
		self.codigo = cod
