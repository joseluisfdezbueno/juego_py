#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()
    acabado = False
    ranking = False
    nombre = ""
    puntuacion = 0	
    tiempo = 30
    incX = 0
    
    # coords iniciales
    coordX_pala = 300
    coordY_pala = 600    
    coordX_rojo = 370
    coordY_rojo = 60
    coordX_azul = 240
    coordY_azul = 60
    coordX_verde = 110
    coordY_verde = 60
    coordX_verde2 = 500
    coordY_verde2 = 60

    coords_rojo = (coordX_rojo, coordY_rojo)
    coords_azul = (coordX_azul, coordY_azul)            
    coords_verde = (coordX_verde, coordY_verde)
    coords_verde2 = (coordX_verde2, coordY_verde2)
	
	# objeto reloj
    Reloj= pygame.time.Clock()

	# establecemos la ventana
    Ventana = pygame.display.set_mode((867, 650))
    pygame.display.set_caption("Juego Python")
    
    # establecemos la fuente y renderizamos los mensajes que queremos escribir en pantalla"
    fuente= pygame.font.Font(None, 30)
    msj_puntuacion = fuente.render("PUNTUACION", 1, (255,255,255))
    valor_puntuacion = fuente.render(str(puntuacion), 1, (255,255,255))
    tiempo_restante = fuente.render(str(tiempo), 1, (255,255,255))
    msj_pedir_nombre = fuente.render("Introduce tu nombre:", 1, (255,255,255))
    msj_nombre = fuente.render("", 1, (255,255,255))
    msj_marcador = fuente.render("MARCADOR", 1, (255,255,255))

	# cargamos las imagenes
    marcador = pygame.image.load("marcador.png")
    fondo = pygame.image.load("fondo7.png")
    game_over = pygame.image.load("game_over.jpg")
        
    imagen_pala = pygame.image.load("pala.png")
    transparente = imagen_pala.get_at((0, 0))
    imagen_pala.set_colorkey(transparente)
    
    # cargamos la imagen del cubo rojo. Si lo tocamos en el juego, perdemos.
    imagen_cubo_rojo = pygame.image.load("cubo_rojo.png")
    transparente = imagen_cubo_rojo.get_at((0, 0))
    imagen_cubo_rojo.set_colorkey(transparente)
    # cargamos la imagen del cubo rojo. Si lo tocamos en el juego, perdemos puntos.
    imagen_cubo_azul = pygame.image.load("cubo_azul.png")
    transparente = imagen_cubo_azul.get_at((0, 0))
    imagen_cubo_azul.set_colorkey(transparente)
    # cargamos la imagen del cubo verde. Si lo tocamos en el juego, ganamos puntos.
    imagen_cubo_verde = pygame.image.load("cubo_verde.png")
    transparente = imagen_cubo_verde.get_at((0, 0))
    imagen_cubo_verde.set_colorkey(transparente)
        
    # cargamos la música de fondo
    Musica = pygame.mixer.Sound("guitarra.wav")

	# inicializamos la pala
    coordenadas_pala = (coordX_pala, coordY_pala)
    miPala = Pala(coordenadas_pala, imagen_pala)
    # inicializamos cubos
    cubo_rojo = Cubo(coords_rojo, imagen_cubo_rojo)
    cubo_azul = Cubo(coords_azul, imagen_cubo_azul)
    cubo_verde = Cubo(coords_verde, imagen_cubo_verde)
    cubo_verde2 = Cubo(coords_verde2, imagen_cubo_verde)

    # seleccionamos el volumen
    Musica.set_volume(0.8)

    # reproducimos la música de fondo indefinidamente
    Musica.play(-1)

    while True:

		# actualizamos las coordenadas
        miPala.update(coordenadas_pala)
        cubo_rojo.update(coords_rojo)
        cubo_azul.update(coords_azul)
        cubo_verde.update(coords_verde)
        cubo_verde2.update(coords_verde2)

		# mostramos los sprites
        Ventana.blit(marcador, (0, 0))		
        Ventana.blit(fondo, (14, 14))
        Ventana.blit(msj_puntuacion, (700, 28))
        Ventana.blit(valor_puntuacion, (755, 65))
        Ventana.blit(tiempo_restante, (755, 95))
        Ventana.blit(miPala.image, miPala.rect)
        Ventana.blit(cubo_rojo.image, cubo_rojo.rect)
        Ventana.blit(cubo_azul.image, cubo_azul.rect)
        Ventana.blit(cubo_verde.image, cubo_verde.rect)
        Ventana.blit(cubo_verde2.image, cubo_verde2.rect)
        if acabado:
			Ventana.blit(game_over, (0, 0))
			Ventana.blit(msj_pedir_nombre, (130, 460))
			Ventana.blit(msj_nombre, (355, 460))
        if ranking:
			Ventana.fill((0, 0, 0))
			Ventana.blit(msj_marcador, (355, 130))
			Ventana.blit(msj_nombre, (205, 300))
			Ventana.blit(valor_puntuacion, (555, 300))
        
		# visualizamos
        pygame.display.flip()

		# tratamos los eventos generados
        for evento in pygame.event.get():
			# para salir del juego cerrando la ventana
            if evento.type == QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if acabado:
					if evento.key == pygame.K_RETURN:
						    acabado = False
						    ranking = True
					if evento.key > 31 and evento.key < 123:															
						letra = chr(evento.key)
						nombre = nombre + letra
						msj_nombre = fuente.render(nombre, 1, (255,255,255))
						print letra
                    
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()
                elif evento.key == pygame.K_RIGHT:
						incX = 35
                elif evento.key == pygame.K_LEFT:					
						incX = -35
            if evento.type == pygame.KEYUP:				
				incX = 0
	
		# incrementos
        if coordY_rojo < 610:
			coordY_rojo = coordY_rojo +10
        else:
			coordY_rojo = 60
        if coordY_azul < 601:
			coordY_azul = coordY_azul +19
        else:
			coordY_azul = 60
        if coordY_verde < 605:
			coordY_verde = coordY_verde + 15
        else:
			coordY_verde = 60
        if coordY_verde2 < 595:
			coordY_verde2 = coordY_verde2 + 25
        else:
			coordY_verde2 = 60
                        
		# colisiones		
        if pygame.sprite.collide_rect(miPala, cubo_rojo):
			acabado = True
			
        if pygame.sprite.collide_rect(miPala, cubo_azul):
			if (acabado == False) and (ranking == False):
			    puntuacion = puntuacion - 30
			coordY_azul = 60
			
        if pygame.sprite.collide_rect(miPala, cubo_verde):
			if (acabado == False) and (ranking == False):			
			    puntuacion = puntuacion + 10
			coordY_verde = 60
			
        if pygame.sprite.collide_rect(miPala, cubo_verde2):
	        if (acabado == False) and (ranking == False):
				puntuacion = puntuacion + 10
	        coordY_verde2 = 60
	        		
		# seleccionamos las nuevas coordenadas
        if coordX_pala +incX > 35 and coordX_pala +incX <632:
			coordX_pala = coordX_pala + incX
        coordenadas_pala = (coordX_pala, coordY_pala)
        coords_rojo = (coordX_rojo, coordY_rojo)
        coords_azul = (coordX_azul, coordY_azul)            
        coords_verde = (coordX_verde, coordY_verde)
        coords_verde2 = (coordX_verde2, coordY_verde2) 	
		
		# tiempo
        segundos = pygame.time.get_ticks()/1000
        tiempo = 30 - segundos
        valor_puntuacion = fuente.render(str(puntuacion), 1, (255,255,255))
        tiempo_restante = fuente.render(str(tiempo), 1, (255,255,255))		
        if tiempo == 0:
			acabado = True
		            
        # esperamos
        Reloj.tick(25)


class Pala(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
        pygame.sprite.Sprite.__init__(self)

        self.image = imagen      
        self.actualizado = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas

    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        if self.actualizado + 100 < pygame.time.get_ticks():            
            self.actualizado= pygame.time.get_ticks()
            
class Cubo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
        pygame.sprite.Sprite.__init__(self)

        self.image = imagen      
        self.actualizado = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas

    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        if self.actualizado + 50 < pygame.time.get_ticks():            
            self.actualizado= pygame.time.get_ticks()           

# ejecutamos el juego
main()
