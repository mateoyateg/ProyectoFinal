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
    
    #Pone icono a la ventana
    icon = util.cargar_imagen('imagenes/tux_icono.png')
    pygame.display.set_icon(icon)
    
    #Carga la imagen del tablero
    background_image = util.cargar_imagen('imagenes/tablero.png')
    
    #Mensaje de bienvenida por consola
    print("Bienvenido al Juego")
    print ""
    
    #Crea los objetos ficha, dado & casilla
    ficha = fichas.Ficha()
    dado = dados.Dado((1120,590), (0))
    
    #Inicializa contadores
    contador_dado = 0 #Guarda el estado del dado
    sigue_casilla = 0 #Calcula la siguiente casilla
    pos_anterior = 0 #Guarda la casilla actual
    
    #Al ser varias casillas, este sera un arreglo de posiciones de casillas
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
    tirando = False
    ganando = False
    preguntando = False
    
    #Variables de condiciones para el banner de la respuesta
    condic_banner = 0
    cord_banner = (0,0)
    
    #Ejecucion del juego
    while True:
		
		#Se crea el objeto teclas para leer el teclado
        teclas = pygame.key.get_pressed()
        
        #Captura eventos en el juego
        for event in pygame.event.get():
			
			#Termina ejecucion del juego al pulsar el salir
			if event.type == pygame.QUIT:
				sys.exit() 
			
			#Captura si el mouse fue presionado
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print("El Mouse fue presionado")
				
				#Guarda la posicion del dado
				x,y = event.pos 
				
				#Comprueba si fue presionado el dado
				if dado.rect.collidepoint(x,y):
					print("El dado fue presionado")
					contador_dado = 0	
					tirando = True
					jugando = False
		
		#Si se presiona el espacio, reinicia el tablero y arranca el juego
        if teclas[K_SPACE]:
			
			#Reinicia lo relacionado al dado
			dado.image = dado.imagenes[0]
			contador_dado = 0
			dado.valor = 0
			
			#Reinicia puntaje de la ficha
			ficha.puntos = 0
			
			#Reinicia lo relacionado a la casilla
			sigue_casilla = 0
			pos_anterior = 0
			
			#Reinicia lo relacionado al banner de pregunta
			condic_banner = 0
			cord_banner = (0,0)
			
			#Reinicia estados
			tirando = False
			ganando = False
			preguntando = False
			
			#Inicia el tablero de juego
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
			 
			"""Definir si la respuesta fue buena o no para el banner de pregunta
			Si la condicion del banner arranca en 0, se muestra otro estado"""
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
			
			#Guarda el numero de casilla actual
			pos_anterior = casilla[pos_anterior].numero
			
			#Si la casilla es mayor que 22, buscar un menor numero
			while sigue_casilla > 22:
				sigue_casilla = sigue_casilla - 1
				dado.valor = dado.valor - 1
			
			"""Realizar el update con la nueva casilla, teniendo en cuenta
			que el dado ya habria sido lanzado, sigue_casilla fue calculado
			al momento de lanzar"""
			ficha.update(casilla[sigue_casilla])
			
			#Carga la imagen del dado correspondiente
			dado.image = dado.imagenes[dado.valor]
			
			#Guarda la posicion de la ficha con las casillas
			pos_anterior = sigue_casilla
			
			#Comprueba si la ficha esta en la ultima casilla
			if (ficha.comparar(casilla[sigue_casilla])) and (ficha.numCasilla(casilla[sigue_casilla]) == 22):
				
				#Imprime mensaje por consola
				print("Juego terminado")
				print ""
				
				#Abre el archivo de puntajes
				puntos = open('puntaje.txt', 'r')
				pts = [x[:-1] for x in puntos.readlines()]
				puntos.close()
				pts.append(ficha.puntos)
				
				"""Pone todos los estados en False para mostrar
				la pantalla de inicio"""
				jugando = False
				tirando = False
				preguntando = False
				
				#Escribe los puntajes con el nuevo incluido
				puntos = open('puntaje.txt', 'w')
				for x in pts:
					puntos.write(str(x)+'\n')
				puntos.close()
				
			
			"""Define que tipo de casilla es donde cayo la ficha y captura
			un nombre del archivo de texto de una pregunta relacionada
			a la casilla donde esta la ficha"""
			nombre_pregunta = preguntas.asignarPregunta(casilla[sigue_casilla].codigo)
			
			#Se muestra pregunta dependiendo la casilla y si esta no es la primera ni la ultima
			if (contador_dado !=1 and contador_dado !=2  and ficha.comparar(casilla[sigue_casilla]) and ficha.comparar(casilla[0]) == False 
				and ficha.comparar(casilla[22]) == False):
				
				#Se ingresa al estado de pregunta
				preguntando = True
				
				#Imprime mensaje por consola
				print("A mostrar pregunta")
				
				#Se sale de estado de juego
				jugando = False

	#Si se tira el dado			
	elif tirando:
		#Asigna un dado aleatorio
		dado.valor = random.randint(1,6)
		
		#Imprime mensaje por consola
		print 'Dado nuevo con valor:' , dado.valor
		
		#Calcula la casilla proxima
		sigue_casilla = pos_anterior + dado.valor
		
		#Sale del estao de tirando y preguntando
		tirando = False
		preguntando = False
		
		#Vuelve al estado de juego
		jugando = True
		
	#Si se entra a una pregunta
	elif preguntando:
			
			#Leer la pregunta
			texto_pregunta = preguntas.leerPregunta(nombre_pregunta)
			
			#Carga el cuadro de pregunta y el tipo de pregunta
			cuadro_image = util.cargar_imagen('preguntas/cuadro.png')
			fuente = pygame.font.Font('fuentes/fuente.ttf', 45)
			tipo_pregunta = fuente.render(texto_pregunta[0][:-1],1,(1,1,1))
			fuente = pygame.font.Font('fuentes/fuente.ttf', int(texto_pregunta[28]))
			
			#Guarda las lineas de la pregunta en variables
			texto_1 = fuente.render(texto_pregunta[1][:-1],1,(1,1,1))
			texto_2 = fuente.render(texto_pregunta[2][:-1],1,(1,1,1))
			texto_3 = fuente.render(texto_pregunta[3][:-1],1,(1,1,1))
			fuente = pygame.font.Font('fuentes/fuente.ttf', int(texto_pregunta[29]))
			opc_a = fuente.render(texto_pregunta[4][:-1],1,(1,1,1))
			opc_b = fuente.render(texto_pregunta[5][:-1],1,(1,1,1))
			opc_c = fuente.render(texto_pregunta[6][:-1],1,(1,1,1))
			opc_d = fuente.render(texto_pregunta[7][:-1],1,(1,1,1))
			
			"""Se hace un blit de la pregunta con las propiedades de la misma, 
			usando las que se encuentran escritas en cada archivo de texto"""
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
			#Si la opcion ingresada es la 'a'
			if teclas[K_a]:
				opc = 1
				
				#Si la opc. ingresada 'a' coincide con la real
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					
					#Imprime mensaje por consola
					print("Opcion (A) correcta")
					
					#Se muestra el banner de respuesta correcta
					condic_banner = 1
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True
				
				#Si la opc. ingresada 'a' no es la correcta
				else:
					
					#Imprime mensaje por consola
					print("Opcion (A) incorrecta")
					
					#Carga el banner de respuesta erronea
					condic_banner = 2
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True

			#Si la opcion ingresada es la 'b'
			if teclas[K_b]:
				opc = 2
				
				#Si la opc. ingresada 'b' coincide con la real
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					
					#Imprime mensaje por consola
					print("Opcion (B) correcta")
					
					#Se muestra el banner de respuesta correcta
					condic_banner = 1
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True
				
				#Si la opc. ingresada 'b' no es la correcta
				else:
					
					#Imprime mensaje por consola
					print("Opcion (B) incorrecta")
					
					#Carga el banner de respuesta erronea
					condic_banner = 2
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True

			#Si la opcion ingresada es la 'c'
			if teclas[K_c]:
				opc = 3
				
				#Si la opc. ingresada 'c' coincide con la real
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					
					#Imprime mensaje por consola
					print("Opcion (C) correcta")
					
					#Se muestra el banner de respuesta correcta
					condic_banner = 1
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True
				
				#Si la opc. ingresada 'c' no es la correcta
				else:
					
					#Imprime mensaje por consola
					print("Opcion (C) incorrecta")
					
					#Carga el banner de respuesta erronea
					condic_banner = 2
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					preguntando = False
					jugando = True

			#Si la opcion ingresada es la 'd'
			if teclas[K_d]:
				opc = 4
				
				#Si la opc. ingresada 'd' coincide con la real
				if int(texto_pregunta[8]) == opc:
					ficha.puntos = ficha.puntos + 1
					
					#Imprime mensaje por consola
					print("Opcion (D) correcta")
					
					#Se muestra el banner de respuesta correcta
					condic_banner = 1
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
					jugando = True
					preguntando = False
				
				#Si la opc. ingresada 'd' no es la correcta
				else:
					
					#Imprime mensaje por consola
					print("Opcion (D) incorrecta")
					
					#Carga el banner de respuesta erronea
					condic_banner = 2
					contador_dado = contador_dado + 1
					
					#Sale de la pregunta y vuelve al tablero de juego
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
			
			#Carga los puntajes y los organiza
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
			
			#Carga y muestra el banner de mejores puntajes
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
