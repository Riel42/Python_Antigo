import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 600
largura = 800
x = largura/2
y = altura/2

fonte = pygame.font.SysFont('comicsansms', 50, True, True)#Fonte do texto
pontos = 0

x_ia = randint(40, 500) #Vai alterar o movimento de forma aleatória da IA dentro da tela.
y_ia = randint(50, 500) #Vai alterar o movimento de forma aleatória da IA dentro da tela.

x_ia2 = randint(40, 500) 
y_ia2 = randint(50, 500)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Oi Mundo')

while True:
  tela.fill((0,0,0))
  mensagem = (f'Pontos: {pontos}')
  texto_formatado = fonte.render(mensagem, True, (255,255,255))#Mostra o texto
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      quit()

  if pygame.key.get_pressed()[K_a]:
    x -= 1
  if pygame.key.get_pressed()[K_d]:
    x += 1
  if pygame.key.get_pressed()[K_w]:
    y -= 1
  if pygame.key.get_pressed()[K_s]:
    y += 1

  jogador = pygame.draw.rect(tela,(1, 200, 30),(x,y,75,75))
  IA = pygame.draw.rect(tela,(222,220,222),(x_ia,y_ia,20,20))
  IA2 = pygame.draw.rect(tela,(222,220,222),(x_ia2,y_ia2,20,20))

  if jogador.colliderect(IA):#Verifica se colidiu o retângulo
    x_ia = randint(40, 500)
    y_ia = randint(50,500)
    pontos += 1

  if jogador.colliderect(IA2):#Verifica se colidiu o retângulo
    x_ia2 = randint(40, 500)
    y_ia2 = randint(50,500)
    pontos += 1
    
  tela.blit(texto_formatado, (500,40))#Posição do texto
  pygame.display.update()
      
