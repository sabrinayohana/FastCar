import pygame

pygame.init()

# carro1
posicao_x = 360
posicao_y = 850
velocidade = 10

# carro2
posicao_x2 = 500
posicao_y2 = 1000
velocidade2 = 9

# carro3
posicao_x3 = 200
posicao_y3 = 1000
velocidade3 = 9

# carro4
posicao_x4 = 50
posicao_y4 = 1000
velocidade4 = 6

# carro5
posicao_x5 = 200
posicao_y5 = 700
velocidade5 = 7

# Fontw tempo
fontTimer = pygame.font.SysFont('Arial black', 20)
textoTempo = fontTimer.render("Tempo: ", True, (255, 255, 255,), (0, 0, 0))
text_pos = textoTempo.get_rect()
text_pos.center = (50, 50)

timer = 0
sec = 0

# menu fonte e posiçao
status = "menu"
fontMenu = pygame.font.SysFont('Arial black', 40)
textoMenu = fontMenu.render("Pressione [S] para iniciar", True, (255, 255, 255,), (0, 0, 0))
menu_pos = textoMenu.get_rect()
menu_pos.center = (300, 500)

# GAME OVEEER
fontGameOver = pygame.font.SysFont('Arial black', 40)
textoGameOver = fontGameOver.render("GAME OVER", True, (255, 255, 255), (0, 0, 0))
gameOver_pos = textoGameOver.get_rect()
gameOver_pos.center = (300, 500)


background = pygame.image.load('pista.jpg')
carro5 = pygame.image.load('carro5.png')
carro4 = pygame.image.load('carro4.png')
carro3 = pygame.image.load('carro3.png')
carro2 = pygame.image.load('carro2.png')
carro = pygame.image.load('carro1.png')
tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')

# Mantém a tela aberta
tela_aberta = True
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_aberta = False

    movimentos = pygame.key.get_pressed()

    if status == "menu":
        tela.fill((0, 0, 0))
        tela.blit(textoMenu, menu_pos)
        pygame.display.update()

        if movimentos[pygame.K_s]:
            status = "jogando"
            sec = 0
            timer = 0

    elif status == "jogando":

        # Movimentação do carro1
        if movimentos[pygame.K_UP] and posicao_y >= 30:  # o and limita o movimento
            posicao_y -= velocidade

        if movimentos[pygame.K_DOWN] and posicao_y <= 820:
            posicao_y += velocidade

        if movimentos[pygame.K_LEFT] and posicao_x >= 50:
            posicao_x -= velocidade

        if movimentos[pygame.K_RIGHT] and posicao_x <= 500:
            posicao_x += velocidade

        # movimentação carro2 em loop
        posicao_y2 -= velocidade2
        if posicao_y2 <= -150:
            posicao_y2 = 1000

        # movimentação carro3 em loop
        posicao_y3 += velocidade3
        if posicao_y3 >= 1000:
            posicao_y3 = -150

        # movimentação carro4 em loop
        posicao_y4 += velocidade4
        if posicao_y4 >= 1000:
            posicao_y4 = -150

        # movimentação carro5 em loop
        posicao_y5 += velocidade5
        if posicao_y5 >= 1000:
            posicao_y5 = -150

        # colisão e game over
        jogador_rect = pygame.Rect(posicao_x, posicao_y, carro.get_width(), carro.get_height())
        carro2_rect = pygame.Rect(posicao_x2, posicao_y2, carro2.get_width(), carro2.get_height())
        carro3_rect = pygame.Rect(posicao_x3, posicao_y3, carro3.get_width(), carro3.get_height())
        carro4_rect = pygame.Rect(posicao_x4, posicao_y4, carro4.get_width(), carro4.get_height())
        carro5_rect = pygame.Rect(posicao_x5, posicao_y5, carro5.get_width(), carro5.get_height())

        if (jogador_rect.colliderect(carro2_rect) or
            jogador_rect.colliderect(carro3_rect) or
            jogador_rect.colliderect(carro4_rect) or
            jogador_rect.colliderect(carro5_rect)):

            posicao_x = 360
            posicao_y = 850
            status = "game_over"

        # temporizador
        if (timer < 20):
            timer += 1
        else:
            sec += 1
            textoTempo = fontTimer.render("Tempo: " + str(sec), True, (255, 255, 255,), (0, 0, 0))  # Corrigido para fontTimer
            timer = 0
        
        if status == "game_over":
          tela.fill((0, 0, 0))
          tela.blit(textoGameOver, gameOver_pos)
          pygame.display.update()
          pygame.time.delay(3000) #3 segundos
          tela_aberta = False


        tela.blit(background, (0, 0))  # Para conseguir ver o background
        tela.blit(textoTempo, text_pos)
        tela.blit(carro5, (posicao_x5, posicao_y5))  # Para conseguir ver o carro/posição
        tela.blit(carro4, (posicao_x4, posicao_y4))  # Para conseguir ver o carro/posição
        tela.blit(carro3, (posicao_x3, posicao_y3))  # Para conseguir ver o carro/posição
        tela.blit(carro2, (posicao_x2, posicao_y2))  # Para conseguir ver o carro/posição
        tela.blit(carro, (posicao_x, posicao_y))  # Para conseguir ver o carro/posição
        pygame.display.update()

pygame.quit()
