import pygame

pygame.init()

background = pygame.image.load('pista.jpg')
tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')

tela_aberta = True
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          tela_aberta = False
    tela.blit(background, (0,0))
    pygame.display.update()
pygame.quit()