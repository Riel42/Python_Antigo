"""
import pygame
from pygame.locals import *

pygame.init()

altura = 650
largura = 750

branco = (255,255,255)
preto = (0,0,0)

x = 400
y = 400

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('No Cube')
while True:
  tela.fill((branco))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      quit()

  jogador = pygame.draw.rect(tela,preto,(x,y,20,20))
  solo = pygame.draw.rect(tela,preto,(0, 610, 820, 820))
  if jogador.colliderect(solo):
    jogador.y += 0
  else:
    jogador.y += 1
  pygame.display.update()
pygame.quit()
"""

import pygame
pygame.init()


altura = 650
largura = 750

preto =(0,0,0)
branco = (255,255,255)

x = 400
y = 400

janela = pygame.display.set_mode((largura,altura))

jogador = pygame.Rect(x,y,30,30)
base = pygame.Rect(0,600,900,900)

deve = True
while deve:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve = False
    janela.fill(branco)
    pygame.draw.rect(janela,preto,jogador)
    pygame.draw.rect(janela,preto,base)
    pygame.display.update()
    if jogador.colliderect(base):
        jogador.y +=0
    else:
        jogador.y +=1
pygame.quit()
