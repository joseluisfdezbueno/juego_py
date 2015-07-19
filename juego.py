#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()

    # coords pala
    coordX_pala = 300
    coordY_pala = 600
	
	# objeto reloj
    Reloj= pygame.time.Clock()

	# establecemos la ventana
    Ventana = pygame.display.set_mode((867, 650))
    pygame.display.set_caption("Juego Python")

	# Cargamos las imagenes
    marcador = pygame.image.load("marcador.png")
    fondo = pygame.image.load("fondo7.png")
    imagen_pala = pygame.image.load("pala.png")
    transparente = imagen_pala.get_at((0, 0))
    imagen_pala.set_colorkey(transparente)
    
    # Ruidito es un objeto Sound creado a partir del archivo *.wav
    # Ruidito = pygame.mixer.Sound("ouch.wav")

    # cargamos la música de fondo
    Musica = pygame.mixer.Sound("guitarra.wav")

	# inicializamos la pala
    coordenadas_pala = (coordX_pala, coordY_pala)
    miPala = Pala(coordenadas_pala, imagen_pala)

    # seleccionamos el volumen
    Musica.set_volume(0.8)

    # reproducimos la música de fondo indefinidamente
    Musica.play(-1)

    while True:

		# actualizamos las coordenadas de la pala
        miPala.update(coordenadas_pala)
		
		# mostramos los sprites
        Ventana.blit(marcador, (0, 0))		
        Ventana.blit(fondo, (14, 14))
        Ventana.blit(miPala.image, miPala.rect)

        pygame.display.flip()

		# tratamos los eventos generados
        for evento in pygame.event.get():
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
        Reloj.tick(30)


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

# ejecutamos el juego
main()
