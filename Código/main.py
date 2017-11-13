#Importa modulos de Python & Pygame
import sys, pygame, copy
import random
from pygame.locals import *

#Importa modulos propios del juego
from logica import util
from logica import dados
from logica import casillas
from logica import fichas
from logica import pregunta

#Define ancho y alto de la pantalla
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


#Metodo para ordenar las puntuaciones
def ordenar(lista):
    for x in range(0,len(lista)):
        for y in range(0,len(lista)):
            if int(lista[x]) > int(lista[y]):
                temp = lista[x]
                lista[x] = lista[y]
                lista[y] = temp

#Metodo principal del juego
def game():
	
	#Inicializa todos los modulos de Pygame
    pygame.init()
    
    #Inicializa el modulo del mixer (Pygame)
    pygame.mixer.init()
    
    #Establece el mouse visible en la pantalla
    pygame.mouse.set_visible(True)
    
    #Crea la pantalla del juego
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    
    #Nombra la ventana
    pygame.display.set_caption( "Juego de Mesa" )
    
    #Carga la imagen del tablero
    background_image = util.cargar_imagen('imagenes/tablero.png')
    
    #Crea los objetos ficha, dado & casilla
    ficha = fichas.Ficha()
    dado = dados.Dado((1120,590), (0))
    contador = 0
    #Al ser varias casillas, este sera un arreglo de posiciones
    casilla = [casillas.Casilla((90,440)),casillas.Casilla((205,380)),
			   casillas.Casilla((260,260)),casillas.Casilla((220,170)),
			   casillas.Casilla((160,75)),casillas.Casilla((160,75))
			   ]
			   
    #Crea el objeto pregunta, donde se leen las mismas
    preguntas = pregunta.Pregunta()
    #Se define que el juego no arranque en el tablero
    jugando = False
    preguntando = False
    
    #Ejecucion del juego
    while True:
		
		#Se crea el objeto teclas para leer el teclado
        teclas = pygame.key.get_pressed()
        
        for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() 
		
		#Si se presiona el espacio, arranca el tablero
        if teclas[K_SPACE]:
			jugando = True
        
        #Tablero de juego
        if jugando:
			
			#'Blit' del tablero, dado y ficha
			screen.blit(background_image, (0,0))
			screen.blit(dado.image,dado.rect)
			screen.blit(ficha.image,ficha.rect)			
			"""dado.image = dado.imagenes[0]"""
			
			cont = 0
			aux=0
			aux2=0
			#Si se presiona la tecla '', se tira el dado
			
			if teclas[K_t]:
				#Modifica el valor del dado
				contador = 0
				dado.valor = random.randint(1,4)
				dado.image = dado.imagenes[dado.valor]
				aux = dado.valor
				cont = cont + 1
			
			#Se actualiza la posicion de la ficha con respecto al dado
			
			
			if cont!=1:
				aux2=aux + dado.valor
			else:
				aux2=aux2
			
			ficha.update(casilla[aux2])
			
			
			#Se muestra pregunta dependiendo la casilla y si esta no es la primera
			if (ficha.comparar(casilla[dado.valor]) and ficha.comparar(casilla[0]) == False and contador != 1):
				preguntando = True
				jugando = False
				contador = contador + 1
				
				
	elif preguntando:
			#Leer la pregunta
			auxiliar = preguntas.leerPregunta('preguntas/pregunta_1.txt')
			#Carga el cuadro de pregunta
			cuadro_image = util.cargar_imagen('preguntas/cuadro.png')
			fuente = pygame.font.Font('fuentes/fuente.ttf', 45)
			#Se muestra el texto de la misma
			tipo_pregunta = fuente.render(auxiliar[0],1,(1,1,1))
			texto_1 = fuente.render(auxiliar[1],1,(1,1,1))
			texto_2 = fuente.render(auxiliar[2],1,(1,1,1))
			texto_3 = fuente.render(auxiliar[3],1,(1,1,1))
			opc_a = fuente.render(auxiliar[4],1,(1,1,1))
			opc_b = fuente.render(auxiliar[5],1,(1,1,1))
			opc_c = fuente.render(auxiliar[6],1,(1,1,1))
			opc_d = fuente.render(auxiliar[7],1,(1,1,1))
			#Se hace un blit de todo
			screen.blit(cuadro_image,(220,45))
			screen.blit(tipo_pregunta,(240,65))
			screen.blit(texto_1,(340,110))
			screen.blit(texto_2,(410,150))
			screen.blit(texto_3,(540,190))
			screen.blit(opc_a,(240,270))
			screen.blit(opc_b,(670,270))
			screen.blit(opc_c,(280,380))
			screen.blit(opc_d,(630,380))
			#Pedir al usuario respuesta
			if teclas[K_a]:
				opc = 'a'
				if auxiliar[8] == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien A")
					preguntando = False
					jugando = True
				else:
					print("Error A")
					preguntando = False
					jugando = True

			if teclas[K_b]:
				opc = 'b'
				if auxiliar[8] == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien B")
					preguntando = False
					jugando = True
				else:
					print("Error B")
					preguntando = False
					jugando = True

			if teclas[K_c]:
				opc = 'c'
				if auxiliar[8] == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien C")
					preguntando = False
					jugando = True
				else:
					print("Error C")
					preguntando = False
					jugando = True

			if teclas[K_d]:
				opc = 'd'
				if auxiliar[8] == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien D")
					jugando = True
					preguntando = False
					
					
				else:
					print("Error D")
					jugando = True
					preguntando = False
					


			
			
			
			

        #Pantalla de bienvenida         
        else:
			#Carga las imagenes para la pantalla inicial
			conceptos_image = util.cargar_imagen('imagenes/conceptos.png')
			historia_image = util.cargar_imagen('imagenes/historia.png')
			diseno_image = util.cargar_imagen('imagenes/diseno.png')
			inicio_image = util.cargar_imagen('imagenes/fondo.png')
			tux_image = util.cargar_imagen('imagenes/tux.png')
			uml_image = util.cargar_imagen('imagenes/uml.png')
			
			#Realiza el 'blit' en orden de dichas imagenes 
			screen.blit(inicio_image, (0, 0))
			screen.blit(historia_image, (350,135))
			screen.blit(uml_image, (430, 130))
			screen.blit(diseno_image, (530, 110))
			screen.blit(conceptos_image, (640, 90))
			screen.blit(tux_image, (700,500))
			
			
			#Carga puntajes y los organiza
			puntos = open('puntajes/puntaje.txt', 'r')
			pts = [x[:-1] for x in puntos.readlines()]
			puntos.close()
			ordenar(pts)
			
			#Carga y muestra el banner principal
			fuente = pygame.font.Font('fuentes/fuente.ttf', 70)
			texto_titulo = fuente.render("Adivina - Programacion", 1 ,(255,255,255))
			screen.blit(texto_titulo, (330, 20))
			
			#Carga y muestra el banner de espacio
			fuente = pygame.font.Font('fuentes/fuente.ttf', 50)
			texto_espacio = fuente.render("Pulse espacio para continuar...", 1 ,(255,255,255))
			screen.blit(texto_espacio, (350, 400))
			
			#Carga y mmuestra el banner de mejores puntajes
			fuente = pygame.font.Font('fuentes/fuente.ttf', 30)
			texto_puntos = fuente.render("Mejores puntajes: ", 1, (255, 255, 255))
			screen.blit(texto_puntos, (50, 550))
			
			#Imprime los mejores 10 puntajes
			linea = 50
			fuente = pygame.font.Font('fuentes/fuente.ttf', 27)
			for x in pts[:10]:
				if int(x) == 1:
					color = (255,255,0)
				else:
					color = (255,255,255)
					
				texto_puntos = fuente.render(str(x), 1, color)
				screen.blit(texto_puntos, (linea, 585))
				linea += 70
        
        #Realiza el update de la pantalla           
        pygame.display.update()
        
        #Pausa el programa por un momento
        pygame.time.delay(10)

#Si el juego se ejecuta
if __name__ == '__main__':
    game()
