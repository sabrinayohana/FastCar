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

#carro5
posicao_x5 = 200
posicao_y5 = 700
velocidade5 = 7

#tempo
font = pygame.font.SysFont('Arial black', 20)
textoTempo = font.render("Tempo: ", True, (255,255,255,), (0,0,0))
text_pos = textoTempo.get_rect()
text_pos.center = (50,50)

timer = 0
sec = 0


background = pygame.image.load('pista.jpg')
carro5 = pygame.image.load('carro5.png')
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
    if movimentos[pygame.K_UP] and posicao_y >= 30: # o and limita o movimento 
     posicao_y-= velocidade
    
    if movimentos[pygame.K_DOWN] and posicao_y <= 820:
     posicao_y += velocidade

    if movimentos[pygame.K_LEFT] and posicao_x >= 50: 
     posicao_x -= velocidade
    
    if movimentos[pygame.K_RIGHT] and posicao_x <= 500:
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

    #movimentação carro4 em loop
    posicao_y5 += velocidade5
    if posicao_y5 >= 1000:
      posicao_y5 = -150


#temporizadpr
    if (timer <20):
      timer +=1
    else:
      sec +=1
      textoTempo = font.render("Tempo: "+ str(sec), True, (255,255,255,), (0,0,0))
      timer = 0
  


    tela.blit(background, (0,0)) #Para conseguir ver o backgorund
    tela.blit(textoTempo, text_pos)
    tela.blit(carro5, (posicao_x5, posicao_y5)) #Para conseguir ver o carro/posiçao
    tela.blit(carro4, (posicao_x4, posicao_y4)) #Para conseguir ver o carro/posiçao
    tela.blit(carro3, (posicao_x3, posicao_y3)) #Para conseguir ver o carro/posiçao
    tela.blit(carro2, (posicao_x2, posicao_y2)) #Para conseguir ver o carro/posiçao
    tela.blit(carro, (posicao_x, posicao_y)) #Para conseguir ver o carro/posiçao
    pygame.display.update()
pygame.quit()