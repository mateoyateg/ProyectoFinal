import pygame

#Metodo para cargar imagenes
def cargar_imagen(nombre, optimizar=False):
    imagen = pygame.image.load(nombre)

    if optimizar:
        return imagen.convert()
    else:
        return imagen.convert_alpha()
