import pygame

pygame.init()

posicao_x = 340
posicao_y = 850
velocidade = 10

background = pygame.image.load('pista.jpg')
carro = pygame.image.load('carro150.png')
tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')

#Mantem a tela aberta (
tela_aberta = True 
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          tela_aberta = False # )

#Movimentaçao do carro
    movimentos = pygame.key.get_pressed()
    if movimentos[pygame.K_UP]:
     posicao_y-= velocidade
    
    if movimentos[pygame.K_DOWN]:
     posicao_y += velocidade

    if movimentos[pygame.K_LEFT]:
     posicao_x -= velocidade
    
    if movimentos[pygame.K_RIGHT]:
     posicao_x += velocidade

    tela.blit(background, (0,0)) #Para conseguir ver o backgorund
    tela.blit(carro, (posicao_x, posicao_y)) #Para conseguir ver o carro/posiçao
    pygame.display.update()
pygame.quit()