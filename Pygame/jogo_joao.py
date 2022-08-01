import pygame
pygame.init()

preto = (0,0,0)
branco = (255,255,255)

janela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Fisica')

player = pygame.Rect(200,200,50,50)
base = pygame.Rect(0,580,800,800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    janela.fill(branco)  
    pygame.draw.rect(janela,preto,player)
    pygame.draw.rect(janela,preto,base)
    pygame.display.update()
    if player.colliderect(base):
        player.y +=0
    else:
        player.y +=1
pygame.quit()
