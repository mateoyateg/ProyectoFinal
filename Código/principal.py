import sys, pygame, util
from pygame.locals import *
from random import *
import copy

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def ordenar(lista):
    for x in range(0,len(lista)):
        for y in range(0,len(lista)):
            if int(lista[x]) > int(lista[y]):
                temp = lista[x]
                lista[x] = lista[y]
                lista[y] = temp

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Juego de Mesa" )
    background_image = util.cargar_imagen('imagenes/tablero.png')
    inicio_image = util.cargar_imagen('imagenes/fondo.png')
    pygame.mouse.set_visible(True)
    primer_dado = util.cargar_imagen('imagenes/dado_1.png')
    tux_image = util.cargar_imagen('imagenes/tux.png')
    
    uml_image = util.cargar_imagen('imagenes/uml.png')
    diseno_image = util.cargar_imagen('imagenes/diseno.png')
    conceptos_image = util.cargar_imagen('imagenes/conceptos.png')
    historia_image = util.cargar_imagen('imagenes/historia.png')
    
    jugando = False

    while True:
        teclas = pygame.key.get_pressed()
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()    
        if teclas[K_SPACE]:
                jugando = True
                
        if jugando:
                fuente = pygame.font.Font(None,25)
                cont = 0

                screen.blit(background_image, (0,0))
                screen.blit(primer_dado, (1120,590))

                 
        else:
                screen.blit(inicio_image, (0, 0))
                screen.blit(tux_image, (700,500))
                
                puntos = open('puntaje.txt', 'r')
                pts = [x[:-1] for x in puntos.readlines()]
                puntos.close()
                ordenar(pts)
                
                
                
                fuente = pygame.font.Font('fuente.ttf', 70)
                texto_titulo = fuente.render("Adivina - Programacion", 1 ,(255,255,255))
                screen.blit(texto_titulo, (330, 20))
                
                fuente = pygame.font.Font('fuente.ttf', 50)
                texto_banner = fuente.render("Pulse espacio para continuar...", 1 ,(255,255,255))
                screen.blit(texto_banner, (350, 400))
                
                linea = 50
                
                fuente = pygame.font.Font('fuente.ttf', 30)
                texto_puntos = fuente.render("Mejores puntajes: ", 1, (255, 255, 255))
                screen.blit(texto_puntos, (50, 550))
                fuente = pygame.font.Font('fuente.ttf', 27)
                
                screen.blit(uml_image, (170, 150))
                screen.blit(diseno_image, (220, 150))
                screen.blit(conceptos_image, (280, 150))
                screen.blit(historia_image, (350, 150))
                
                
                for x in pts[:10]:
					if int(x) == 1:
						color = (255,255,0)
					else:
						color = (255,255,255)
					texto_puntos = fuente.render(str(x), 1, color)
					screen.blit(texto_puntos, (linea, 585))
					linea += 70
                    
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
