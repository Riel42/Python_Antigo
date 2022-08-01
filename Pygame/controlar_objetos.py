import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 600
largura = 800
x = largura/2
y = altura/2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Oi Mundo')

while True:
  tela.fill((0,0,0)) #Não deixa rastro do objeto que se move.
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      quit()
      '''
    AQUI, SE EU SEGURAR A TECLA, ELA NÃO IRÁ PARAR O OBJETO
    
    if event.type == KEYDOWN:
      if event.key == K_a:
        x -= 20
      if event.key == K_d:
        x += 20
      if event.key == K_w:
        y -= 20 #Pelo o Pygame fazer o contrário, para subir é com menos.
      if event.key == K_s:
        y += 20
        '''
  #Aqui eu posso segurar a tecla e o objeto se movimentará.
  if pygame.key.get_pressed()[K_a]:
    x -= 1
  if pygame.key.get_pressed()[K_d]:
    x += 1
  if pygame.key.get_pressed()[K_w]:
    y -= 1
  if pygame.key.get_pressed()[K_s]:
    y += 1
    
  pygame.draw.rect(tela,(225, 80, 100),(x,y,60,60))
  pygame.display.update()
		
