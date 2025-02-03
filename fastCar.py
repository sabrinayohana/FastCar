import pygame

pygame.init()

#carro1
posicao_x = 360
posicao_y = 850
velocidade = 10

#carro2
posicao_x2 = 500
posicao_y2 = 1000
velocidade2 = 9

#carro3
posicao_x3 = 200
posicao_y3 = 1000
velocidade3 = 9

#carro4
posicao_x4 = 50
posicao_y4 = 1000
velocidade4 = 6

background = pygame.image.load('pista.jpg')
carro4 = pygame.image.load('carro4.png')
carro3 = pygame.image.load('carro3.png')
carro2 = pygame.image.load('carro2.png')
carro = pygame.image.load('carro1.png')
tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')

#Mantem a tela aberta (
tela_aberta = True 
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          tela_aberta = False # )

#Movimentaçao do carro1
    movimentos = pygame.key.get_pressed()
    if movimentos[pygame.K_UP]:
     posicao_y-= velocidade
    
    if movimentos[pygame.K_DOWN]:
     posicao_y += velocidade

    if movimentos[pygame.K_LEFT]:
     posicao_x -= velocidade
    
    if movimentos[pygame.K_RIGHT]:
     posicao_x += velocidade

    #movimentação carro2 em loop
    posicao_y2 -= velocidade2
    if posicao_y2 <= -150:
      posicao_y2 = 1000


    #movimentação carro3 em loop
    posicao_y3 += velocidade3
    if posicao_y3 >= 1000:
      posicao_y3 = -150

    
    #movimentação carro4 em loop
    posicao_y4 += velocidade4
    if posicao_y4 >= 1000:
      posicao_y4 = -150


    tela.blit(background, (0,0)) #Para conseguir ver o backgorund
    tela.blit(carro4, (posicao_x4, posicao_y4)) #Para conseguir ver o carro/posiçao
    tela.blit(carro3, (posicao_x3, posicao_y3)) #Para conseguir ver o carro/posiçao
    tela.blit(carro2, (posicao_x2, posicao_y2)) #Para conseguir ver o carro/posiçao
    tela.blit(carro, (posicao_x, posicao_y)) #Para conseguir ver o carro/posiçao
    pygame.display.update()
pygame.quit()