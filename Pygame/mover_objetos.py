import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 800
largura = 600
x = 0
y = 0

tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Oi Mundo')
relogio = pygame.time.Clock()

while True:
  relogio.tick(380)
  tela.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()

  
  pygame.draw.rect(tela,(150,80,25),(x, y, 80, 80))
  if y >= altura:
    if x >= altura:
      y = 0
      x = 0
  y += 1
  x += 1
  pygame.display.update()#Esta função sempre no final
  
 
