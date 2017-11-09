import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
from heroe import *
import util

class Portales(Sprite):
	def __init__(self,coord,cod):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/portal.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		
	def transportar(self, heroe):
         heroe.mover()
