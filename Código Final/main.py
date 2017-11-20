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
    
    #Contador para el estado del dado
    contador_dado = 0
    dado_final = 0
    sigue_casilla = 0
    pos_anterior = 0
    cont2 = 0
    
    #Al ser varias casillas, este sera un arreglo de posiciones
    casilla = [casillas.Casilla((90,440),0,0),casillas.Casilla((205,380),1,1),
			   casillas.Casilla((260,260),2,2),casillas.Casilla((220,170),3,3),
			   casillas.Casilla((160,75),4,4),casillas.Casilla((261,2),1,5),
			   casillas.Casilla((369,70),2,6),casillas.Casilla((495,2),3,7),
			   casillas.Casilla((610,70),4,8),casillas.Casilla((525,160),1,9),
			   casillas.Casilla((455,235),2,10),casillas.Casilla((476,350),3,11),
			   casillas.Casilla((565,427),4,12),casillas.Casilla((683,400),1,13),
			   casillas.Casilla((750,325),2,14),casillas.Casilla((785,210),3,15),
			   casillas.Casilla((840,120),4,16),casillas.Casilla((906,24),1,17),
			   casillas.Casilla((1020,5),2,18),casillas.Casilla((1105,80),3,19),
			   casillas.Casilla((1110,175),4,20),casillas.Casilla((1110,285),1,21),
			   casillas.Casilla((1112,430),0,22)]
			   
    #Crea el objeto pregunta, donde se leen las mismas
    preguntas = pregunta.Pregunta()
    #Se define que el juego no arranque en el tablero
    jugando = False
    preguntando = False
    tirando = False
    ganando = False
    
    dado_estado = True
    
    #Variables de condiciones para el banner de la respuesta
    condic_banner = 0
    cord_banner = (0,0)
    
    #Ejecucion del juego
    while True:
		
		#Se crea el objeto teclas para leer el teclado
        teclas = pygame.key.get_pressed()
        
        for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() 
		
		#Si se presiona el espacio, arranca el tablero
        if teclas[K_SPACE]:
			
			contador_dado = 0
			dado_final = 0
			sigue_casilla = 0
			dado.valor = 0
			ficha.puntos = 0
			pos_anterior = 0
			cont2 = 0
			
			condic_banner = 0
			cord_banner = (0,0)
			dado.image = dado.imagenes[0]
			
			jugando = False
			preguntando = False
			tirando = False
			ganando = False

			dado_estado = True
			
			jugando = True
        
        #Tablero de juego
        if jugando:
			
			#Render de los puntos y el banner de pregunta
			fuente = pygame.font.Font('fuentes/fuente.ttf', 30)
			ficha_puntos = fuente.render("Puntos: " + str(ficha.puntos), 1 ,(255,255,255))
			respuesta_pregunta = fuente.render("A Jugar", 1 ,(255,255,255))
			
			#Blit del tablero, dado, ficha y los puntos
			screen.blit(background_image, (0,0))
			screen.blit(dado.image,dado.rect)
			screen.blit(ficha.image,ficha.rect)			
			screen.blit(ficha_puntos, (80, 680))
			 
			#Definir si la respuesta fue buena o no para el banner de pregunta
			if (condic_banner == 0):
				respuesta_pregunta = fuente.render("A Jugar", 1 ,(255,255,255))
				cord_banner = (90,595)
			elif (condic_banner == 1):
				respuesta_pregunta = fuente.render("Correcto", 1 ,(255,255,255))
				cord_banner = (90,595)
			elif (condic_banner == 2):
				respuesta_pregunta = fuente.render("Error", 1 ,(255,255,255))
				cord_banner = (100,595)
			
			#Blit del banner para la respuesta
			screen.blit(respuesta_pregunta, cord_banner)
			
			#Si se presiona la tecla 't', se tira el dado
			
			pygame.key.set_repeat(True)
			
			"""pos_anterior = casilla[sigue_casilla].posicion"""
			
			
			
			"""print(pos_anterior)"""
			
			pos_anterior = casilla[pos_anterior].numero
			
			while sigue_casilla > 22:
				sigue_casilla = sigue_casilla - 1
				dado.valor = dado.valor - 1
			
			ficha.update(casilla[sigue_casilla])
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					x,y = event.pos
					
					if dado.rect.collidepoint(x,y): 
						contador_dado = 0
						print("Buena la re gonorrea")
						tirando = True
						jugando = False
					
						
			
			dado.image = dado.imagenes[dado.valor]
			
			
			pos_anterior = sigue_casilla
			
			"""print(contador_dado)"""
			"""print(pos_anterior)"""
			
			"""print(sigue_casilla)"""
			
			#Direcciona la ficha a la casilla del dado


			if ficha.comparar(casilla[sigue_casilla]) and ficha.numCasilla(casilla[sigue_casilla]) == 22:
				print ("Ganador")
				
				puntos = open('puntaje.txt', 'r')
				pts = [x[:-1] for x in puntos.readlines()]
				puntos.close()
				pts.append(ficha.puntos)
				jugando = False
				tirando = False
				preguntando = False
				puntos = open('puntaje.txt', 'w')
				for x in pts:
					puntos.write(str(x)+'\n')
				puntos.close()
				
				
				
				
				
				
			
			#Define que tipo de casilla es donde cayo la ficha
			nombre_pregunta = preguntas.asignarPregunta(casilla[sigue_casilla].codigo)
			#Se muestra pregunta dependiendo la casilla y si esta no es la primera
			if (contador_dado !=1 and contador_dado !=2  and ficha.comparar(casilla[sigue_casilla]) and ficha.comparar(casilla[0]) == False and ficha.comparar(casilla[22]) == False  ):
				preguntando = True
				print("ede")
				jugando = False
				dado_estado = True
							
			

	#Si se entra a una pregunta			
	elif tirando:
		dado.valor = random.randint(1,6)
		
		"""while pos_anterior + dado.valor > 22:
			dado.valor = random.randint(1,6)"""
		
		dado.valor = random.randint(1,6)
		sigue_casilla = pos_anterior + dado.valor
		tirando = False
		jugando = True
		preguntando = False
	
	elif preguntando:
			
			#Leer la pregunta
			texto_pregunta = preguntas.leerPregunta(nombre_pregunta)
			#Carga el cuadro de pregunta y el tipo de pregunta
			cuadro_image = util.cargar_imagen('preguntas/cuadro.png')
			fuente = pygame.font.Font('fuentes/fuente.ttf', 45)
			tipo_pregunta = fuente.render(texto_pregunta[0][:-1],1,(1,1,1))
			fuente = pygame.font.Font('fuentes/fuente.ttf', int(texto_pregunta[28]))
			#Guarda las lineas de la pregunta
			texto_1 = fuente.render(texto_pregunta[1][:-1],1,(1,1,1))
			texto_2 = fuente.render(texto_pregunta[2][:-1],1,(1,1,1))
			texto_3 = fuente.render(texto_pregunta[3][:-1],1,(1,1,1))
			fuente = pygame.font.Font('fuentes/fuente.ttf', int(texto_pregunta[29]))
			opc_a = fuente.render(texto_pregunta[4][:-1],1,(1,1,1))
			opc_b = fuente.render(texto_pregunta[5][:-1],1,(1,1,1))
			opc_c = fuente.render(texto_pregunta[6][:-1],1,(1,1,1))
			opc_d = fuente.render(texto_pregunta[7][:-1],1,(1,1,1))
			#Se hace un blit de la pregunta
			screen.blit(cuadro_image,(220,45))
			screen.blit(tipo_pregunta,(240,65))
			screen.blit(texto_1,(int(texto_pregunta[9]),int(texto_pregunta[10])))
			screen.blit(texto_2,(int(texto_pregunta[11]),int(texto_pregunta[12])))
			screen.blit(texto_3,(int(texto_pregunta[13]),int(texto_pregunta[14])))
			screen.blit(opc_a,(int(texto_pregunta[16]),int(texto_pregunta[17])))
			screen.blit(opc_b,(int(texto_pregunta[19]),int(texto_pregunta[20])))
			screen.blit(opc_c,(int(texto_pregunta[22]),int(texto_pregunta[23])))
			screen.blit(opc_d,(int(texto_pregunta[25]),int(texto_pregunta[26])))
			
			#El usuario ingresa respuesta por medio del teclado
			if teclas[K_a]:
				opc = 1
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien A")
					condic_banner = 1
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True
				else:
					print("Error A")
					fuente = pygame.font.Font('fuentes/fuente.ttf', 30)
					condic_banner = 2
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True

			if teclas[K_b]:
				opc = 2
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien B")
					condic_banner = 1
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True
				else:
					print("Error B")
					condic_banner = 2
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True

			if teclas[K_c]:
				opc = 3
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien C")
					condic_banner = 1
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True
				else:
					print("Error C")
					condic_banner = 2
					contador_dado = contador_dado + 1
					preguntando = False
					jugando = True

			if teclas[K_d]:
				opc = 4
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					print("Bien D")
					condic_banner = 1
					contador_dado = contador_dado + 1
					jugando = True
					preguntando = False
				else:
					print("Error D")
					condic_banner = 2
					contador_dado = contador_dado + 1
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
			puntos = open('puntaje.txt', 'r')
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
				if int(x) == ficha.puntos:
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
