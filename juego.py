#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()

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
    
    # puntuación actual
    puntuacion = '0'
	
	# objeto reloj
    Reloj= pygame.time.Clock()

	# establecemos la ventana
    Ventana = pygame.display.set_mode((867, 650))
    pygame.display.set_caption("Juego Python")
    
    # establecemos la fuente y renderizamos la palabra "puntuación"
    fuente= pygame.font.Font(None, 30)
    msj_puntuacion = fuente.render("PUNTUACION", 1, (255,255,255))
    valor_puntuacion = fuente.render(puntuacion, 1, (255,255,255))

	# cargamos las imagenes
    marcador = pygame.image.load("marcador.png")
    fondo = pygame.image.load("fondo7.png")
    
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
        Ventana.blit(miPala.image, miPala.rect)
        Ventana.blit(cubo_rojo.image, cubo_rojo.rect)
        Ventana.blit(cubo_azul.image, cubo_azul.rect)
        Ventana.blit(cubo_verde.image, cubo_verde.rect)
        Ventana.blit(cubo_verde2.image, cubo_verde2.rect)
        
		# visualizamos
        pygame.display.flip()

		# tratamos los eventos generados
        for evento in pygame.event.get():
			# para salir del juego cerrando la ventana
            if evento.type == QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()
                if evento.key == pygame.K_RIGHT:
					if coordX_pala < 600:
						coordX_pala = coordX_pala + 40
                if evento.key == pygame.K_LEFT:
					if coordX_pala > 60:
						coordX_pala = coordX_pala - 40

            # Si el evento es una pulsación de ratón...
            #elif evento.type == MOUSEBUTTONDOWN:
            
            # seleccionamos las nuevas coordenadas
            coordenadas_pala = (coordX_pala, coordY_pala)                        
            coords_rojo = (coordX_rojo, coordY_rojo)
            coords_azul = (coordX_azul, coordY_azul)            
            coords_verde = (coordX_verde, coordY_verde)
            coords_verde2 = (coordX_verde2, coordY_verde2)

		# incrementos
        coordY_rojo = coordY_rojo +8
        coordY_azul = coordY_azul +17
        coordY_verde = coordY_verde + 13
        coordY_verde2 = coordY_verde2 + 23
        
        # seleccionamos las nuevas coordenadas                                  
        coords_rojo = (coordX_rojo, coordY_rojo)
        coords_azul = (coordX_azul, coordY_azul)            
        coords_verde = (coordX_verde, coordY_verde)
        coords_verde2 = (coordX_verde2, coordY_verde2)         
            
        # esperamos
        Reloj.tick(10)


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
