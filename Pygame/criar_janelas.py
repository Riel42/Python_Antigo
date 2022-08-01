import pygame
from pygame.locals import * #importará tudo do pygame
from sys import exit #Fecha a janela quando eu clicar no 'X' da janela

pygame.init() #inicia o pygame

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Oi, mundo!')

#para o jogo funcionar ele sempre tem que estar atualizando

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	pygame.display.update()
