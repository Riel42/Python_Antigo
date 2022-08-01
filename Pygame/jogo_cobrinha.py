import pygame
from pygame.locals import*
from sys import exit

pygame.init()

MUSIC = pygame.mixer.music.load('Drop and Roll - Silent Partner.mp3')
pygame.mixer.music.play(-1)

ALTURA = 650
LARGURA = 750

x = 250
y = 250

COR_PERSONAGEM = (240, 237, 94)
COR_SOLO = (0,255,0)

PERSONAGEM = pygame.Rect(x, y, 65, 65)
SOLO = pygame.Rect(0, 610, 800, 800)


JANELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo Plataforma')

while True:
  JANELA.fill((255,255,255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

    GRAVIDADE = 10
    PERSONAGEM = (GRAVIDADE)

    while GRAVIDADE != SOLO:
      PERSONAGEM.y =- 1
      
  pygame.draw.rect(JANELA, COR_SOLO, SOLO)
  pygame.draw.rect(JANELA, COR_PERSONAGEM, PERSONAGEM)

  pygame.display.update()
  

