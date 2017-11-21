#Realiza imports de pygame y python
import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
import util

class Dado (Sprite):
	def __init__(self,coord,valor):
		Sprite.__init__(self)
		#Asigna valor al dado dado
		self.valor = valor
		#Carga imagenes de las 6 caras del dado
		self.imagenes = [util.cargar_imagen('imagenes/dado_0.png'),
						 util.cargar_imagen('imagenes/dado_1.png'),
						 util.cargar_imagen('imagenes/dado_2.png'),
						 util.cargar_imagen('imagenes/dado_3.png'),
						 util.cargar_imagen('imagenes/dado_4.png'),
						 util.cargar_imagen('imagenes/dado_5.png'),
						 util.cargar_imagen('imagenes/dado_6.png')]
		#Primera imagen a mostrar
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0],coord[1])

