import pygame

pygame.init()

tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')

tela_aberta = True
while tela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          tela_aberta = False
pygame.quit()