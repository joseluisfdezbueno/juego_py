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

    Reloj= pygame.time.Clock()

    Ventana = pygame.display.set_mode((867, 650))
    pygame.display.set_caption("Juego Python")

	# Cargamos las imagenes
    marcador = pygame.image.load("marcador.png")
    Fondo = pygame.image.load("fondo7.png")

    Imagen = pygame.image.load("monigotillo.png")
    transparente = Imagen.get_at((0, 0))
    Imagen.set_colorkey(transparente)
    
    imagen_pala = pygame.image.load("pala.png")
    transparente = imagen_pala.get_at((0, 0))
    imagen_pala.set_colorkey(transparente)
    
    # Ruidito es un objeto Sound creado a partir del archivo *.wav
    Ruidito = pygame.mixer.Sound("ouch.wav")

    # Musica es otro objeto Sound creado a partir del archivo *.wav
    Musica = pygame.mixer.Sound("guitarra.wav")

    coordenadas_monigotillo= (300, 200)
    coordenadas_pala = (coordX_pala, coordY_pala)

    MiMonigotillo = Monigotillo(coordenadas_monigotillo, Imagen)
    miPala = Pala(coordenadas_pala, imagen_pala)

    # Bajamos el volumen de la música (sí, se puede hacer antes o durante la reproducción)
    Musica.set_volume(0.5)

    # Reproducimos nuestro sample de música en un bucle infinito (-1)
    Musica.play(-1)

    while True:

        MiMonigotillo.update(coordenadas_monigotillo)
        miPala.update(coordenadas_pala)
        Ventana.blit(marcador, (0, 0))
		
        Ventana.blit(Fondo, (14, 14))
        Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)
        Ventana.blit(miPala.image, miPala.rect)

        pygame.display.flip()

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
            elif evento.type == MOUSEBUTTONDOWN:

                # ...actualizamos las coordenadas de monigotillo con las del puntero...
                coordenadas_monigotillo = pygame.mouse.get_pos()

                # ...y reproducimos el sonido.
                Ruidito.play(0)
            
            coordenadas_pala = (coordX_pala, coordY_pala)
        Reloj.tick(30)


class Monigotillo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
        pygame.sprite.Sprite.__init__(self)

        self.ImgCompleta = imagen
        a=0
        self.arrayAnim=[]
        while a < 6:
            self.arrayAnim.append(self.ImgCompleta.subsurface((a*32,100,32,64)))
            a= a + 1
        self.anim= 0

        self.actualizado = pygame.time.get_ticks()
        self.image = self.arrayAnim[self.anim]
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        if self.actualizado + 100 < pygame.time.get_ticks():
            self.anim= self.anim + 1
            if self.anim > 5:
                self.anim= 0
            self.image = self.arrayAnim[self.anim]
            self.actualizado= pygame.time.get_ticks()

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

main()
