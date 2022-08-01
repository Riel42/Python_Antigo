import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 800
largura = 600

tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Oi Mundo')

#Para desenhar coisas na tela, utilizamos o plano cartesiano.
#No pygame, o eixo x é na horizontal e o eixo y é na vertical para baixo
#Utilizamos as cores RGB no Pygame

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
      
  pygame.draw.rect(tela, (125, 68, 120), (80, 200, 350, 200))
  pygame.draw.circle(tela, (80, 8, 175), (110, 100), 60)
  pygame.draw.line(tela,(1,50,132),(600,0),(600,600), 5)
  pygame.display.update()
