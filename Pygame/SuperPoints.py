import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica = pygame.mixer.music.load('Drop and Roll - Silent Partner.mp3')
pygame.mixer.music.play(-1)
colisao_som = pygame.mixer.Sound('som_game.wav')
colisao_som.set_volume(0.3)

altura = 600
largura = 780
x = int(largura/2)
y= int(altura/2)

fonte = pygame.font.SysFont('arial',50,True,True)
pontos = 0

x_ia = randint(20, 500)
y_ia = randint(15, 500)
x_ia2 = randint(20, 500)
y_ia2 = randint(15, 500)

a1 = 255
a2 = 255
a3 = 255

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Super Points - Music Credits: Audionautix')


while True:
  tela.fill([a1,a2,a3])
  #tela.fill([206,143,52])
  mensagem = (f'Pontos: {pontos}')
  mensagem1 = ('AVISO: O')
  mensagem2 = ('O jogo pode causar')
  mensagem3 = ('ataques epiléticos.')
  final_mensagem = ('Obrigado por ter jogado =)...')
               
  texto_formatado = fonte.render(mensagem, True, (15,15,15))
  texto_formatado1 = fonte.render(mensagem1, True, (15,15,15))
  texto_formatado2 = fonte.render(mensagem2, True, (15,15,15))
  texto_formatado3 = fonte.render(mensagem3, True, (15,15,15))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      quit

  if pygame.key.get_pressed()[K_a]:
    x -= 1
  if pygame.key.get_pressed()[K_d]:
    x += 1
  if pygame.key.get_pressed()[K_w]:
    y -= 1
  if pygame.key.get_pressed()[K_s]:
    y += 1

  if pontos >= 250:
    if pygame.key.get_pressed()[K_a]:
      x -= 1.5
    if pygame.key.get_pressed()[K_d]:
      x += 1.5
    if pygame.key.get_pressed()[K_w]:
      y -= 1.5
    if pygame.key.get_pressed()[K_s]:
      y += 1.5
    

  jogador = pygame.draw.rect(tela,(1,200,30), (x,y,50,55))
  IA = pygame.draw.rect(tela,(100,23,255), (x_ia,y_ia,16,16))
  IA2 = pygame.draw.rect(tela,(200,10,5), (x_ia2,y_ia2,16,16))

  if pontos >= 250:
    a1 = randint(0, 255)
    a2 = randint(0, 255)
    a3 = randint(0, 255)
    jogador = pygame.draw.rect(tela,(255,240,0), (x,y,85,85))

  if pontos == 270:
    quit()
    
  if jogador.colliderect(IA):
    x_ia = randint(20, 500)
    y_ia = randint(15, 500)
    pontos += 1
    colisao_som.play()

  if jogador.colliderect(IA2):
    x_ia2 = randint(20, 500)
    y_ia2 = randint(15, 500) 
    pontos += 1
    colisao_som.play()
    
  tela.blit(texto_formatado, (460,30))
  tela.blit(texto_formatado1, (20,35))
  tela.blit(texto_formatado2, (20,85))
  tela.blit(texto_formatado3, (20,135))
  pygame.display.update()
    
  
