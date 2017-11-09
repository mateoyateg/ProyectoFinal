import pygame
from pygame.sprite import Sprite
from pygame import *
from portales import *
from random import *
import util

class Heroe(Sprite):
	def __init__(self):
                Sprite.__init__(self)
                self.puntos = 0
                self.portal = 0
                self.vida = 100
                self.imagenes = [util.cargar_imagen('imagenes/avion_izq.png'),
                                util.cargar_imagen('imagenes/avion_der.png'),
                                util.cargar_imagen('imagenes/avion_arr.png'),
                                util.cargar_imagen('imagenes/avion_aba.png')]
                self.image = self.imagenes[1]
                self.rect = self.image.get_rect()
                self.y = 20
                self.x = 270
                self.rect.move_ip(self.x,self.y)
                
        def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
				self.image = self.imagenes[0]
			elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
				self.rect.x += 10
				self.image = self.imagenes[1]
			if teclas[K_UP] and self.rect.y>=20:
				self.rect.y -= 10
				self.image = self.imagenes[2]
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[3]
				
