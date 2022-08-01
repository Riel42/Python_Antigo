import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#tamanho da tela#
altura = 650
largura = 750

#x e y#
x = 100
y = 100

#cores#
azul = ((174, 232, 251))

#jogador e solo#
jogador = pygame.Rect(x,y,20,20)
solo = pygame.Rect(0, 600, 1000, 1000)

#Janela
janela = pygame.display.set_mode((largura,altura))

while True:
  janela.fill(azul)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
      

  pygame.draw.rect(janela, (241, 136, 31), jogador)
  pygame.draw.rect(janela, (29, 138, 26), solo)
  pygame.display.update()

  if jogador.colliderect(solo):
    jogador.y += 0
  else:
    jogador.y += 1

  pygame.display.update()

  
