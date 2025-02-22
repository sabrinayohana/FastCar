import pygame

pygame.init()
pygame.mixer.init()

soundtrack = pygame.mixer.music.load('soundtrack2.ogg')
som_gameOver = pygame.mixer.music.load('you-lose.ogg')
som_vitoria = pygame.mixer.music.load('you-win.ogg')

# carro princpal
posicao_x = 360; posicao_y = 850; velocidade = 10; velocidade1 = 1

# carro2 azul
posicao_x2 = 500; posicao_y2 = 1000; velocidade2 = 10

# carro3 roxo
posicao_x3 = 200; posicao_y3 = 1000; velocidade3 = 9

# carro4 verde
posicao_x4 = 50; posicao_y4 = 1000; velocidade4 = 5

# carro5 vermelho
posicao_x5 = 360; posicao_y5 = 1000; velocidade5 = 6

velocidade_pista = 30
pos_pista1 = 0; pos_pista2= 0
pos_pista3 = 400; pos_pista4= 400
pos_pista5 = 800; pos_pista6 = 800
pos_pista7 = -200; pos_pista8 = -200
pos_pista9 = -500; pos_pista10 = -500
pos_pista11 = -900; pos_pista12 = -900


fontTimer = pygame.font.SysFont('Arial black', 20)
textoTempo = fontTimer.render("Tempo: ", True, (0, 0, 0,), (255, 217, 95))  
text_pos = textoTempo.get_rect()
text_pos.center = (50, 50)

timer = 0
sec = 0

status = "menu"

# >>>>>>>>>>>>>>>>>>>> FOTOS <<<<<<<<<<<<<<<<<<<<<<<<<<<
backgroundMenu = pygame.image.load('start.png')
backgroundGameOver = pygame.image.load('lose.png')
backgroundVitoria = pygame.image.load('win.png')
background = pygame.image.load('pista.jpg')
background1 = pygame.image.load('pista1.png')
background2 = pygame.image.load('pista2.png')
background3 = pygame.image.load('pista3.png')
background4 = pygame.image.load('pista4.png')
background5 = pygame.image.load('pista5.png')
background6 = pygame.image.load('pista6.png')
background7 = pygame.image.load('pista7.png')
background8 = pygame.image.load('pista8.png')
background9 = pygame.image.load('pista9.png')
background10 = pygame.image.load('pista10.png')
background11 = pygame.image.load('pista11.png')
background12 = pygame.image.load('pista12.png')
carro5 = pygame.image.load('carro5.png')
carro4 = pygame.image.load('carro4.png')
carro3 = pygame.image.load('carro3.png')
carro2 = pygame.image.load('carro2.png')
carro = pygame.image.load('carro1.png')
tela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('FastCar')


# TELA
tela_aberta = True
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_aberta = False

    teclas = pygame.key.get_pressed()

    if status == "menu":
        tela.fill((0, 0, 0))
        tela.blit(backgroundMenu, (0, 0))
        pygame.display.update()

        if teclas[pygame.K_s]:
            status = "jogando"
            sec = 0
            timer = 0

        elif teclas[pygame.K_e]:
            tela_aberta = False

    elif status == "jogando":
        if teclas[pygame.K_UP] and posicao_y >= 30:  
            posicao_y -= velocidade1

        if teclas[pygame.K_DOWN] and posicao_y <= 820:
            posicao_y += velocidade1

        if teclas[pygame.K_LEFT] and posicao_x >= 50:
            posicao_x -= velocidade

        if teclas[pygame.K_RIGHT] and posicao_x <= 500:
            posicao_x += velocidade

        # >>>>>>>>> MOVIMENTO DOS CARROS SECUNDARIOS <<<<<<<
        posicao_y2 += velocidade2
        if posicao_y2 >= 1000:
            posicao_y2 = -150

        posicao_y3 += velocidade3
        if posicao_y3 >= 1000:
            posicao_y3 = -150

        posicao_y4 += velocidade4
        if posicao_y4 >= 1000:
            posicao_y4 = -150

        posicao_y5 += velocidade5
        if posicao_y5 >= 1000:
            posicao_y5 = -150

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

        if (timer < 20):
            timer += 1
        else:
            sec += 1
            textoTempo = fontTimer.render("Tempo: " + str(sec), True, (0, 0, 0,), (255, 217, 95))  
            timer = 0

        if sec >= 15:
            status = "vitoria"

   # >>>>>>>>> MOVIMENTOS DAS PISTAS <<<<<<<
        pos_pista1 += velocidade_pista
        pos_pista2+= velocidade_pista
        pos_pista3 += velocidade_pista
        pos_pista4+= velocidade_pista
        pos_pista5 += velocidade_pista
        pos_pista6 += velocidade_pista
        pos_pista7 += velocidade_pista
        pos_pista8 += velocidade_pista
        pos_pista9 += velocidade_pista
        pos_pista10 += velocidade_pista
        pos_pista11 += velocidade_pista
        pos_pista12 += velocidade_pista

        # LOOP PISTAs
        if pos_pista1 >= 1000:
            pos_pista1 = -1000  

        if pos_pista2>= 1000:
            pos_pista2= -1000  
        
        if pos_pista3 >= 1000:
            pos_pista3 = -1000  

        if pos_pista4>= 1000:
            pos_pista4= -1000 
        
        if pos_pista5 >= 1000:
            pos_pista5 = -1000        
            
        if pos_pista6 >= 1000:
            pos_pista6 = -1000 

        if pos_pista7 >= 1000:
            pos_pista7 = -1000  

        if pos_pista8 >= 1000:
            pos_pista8 = -1000 
        
        if pos_pista9 >= 1000:
            pos_pista9 = -1000        
            
        if pos_pista10 >= 1000:
            pos_pista10 = -1000 

        if pos_pista11 >= 1000:
            pos_pista11 = -1000        
            
        if pos_pista12 >= 1000:
            pos_pista12 = -1000 

        # >>>>>>>>>>>>>> DESENHOSSS <<<<<<<<<<<<<<<<<<<<<<<
        tela.blit(background, (0, 0))  
        tela.blit(background1, (450, pos_pista1)) 
        tela.blit(background2, (145, pos_pista2)) 
        tela.blit(background3, (450, pos_pista3)) 
        tela.blit(background4, (145, pos_pista4))  
        tela.blit(background5, (450, pos_pista5)) 
        tela.blit(background6, (145, pos_pista6))
        tela.blit(background7, (450, pos_pista7)) 
        tela.blit(background8, (145, pos_pista8))  
        tela.blit(background9, (450, pos_pista9)) 
        tela.blit(background10, (145, pos_pista10))   
        tela.blit(background11, (450, pos_pista11)) 
        tela.blit(background12, (145, pos_pista12))  
        tela.blit(textoTempo, text_pos)
        tela.blit(carro5, (posicao_x5, posicao_y5))  
        tela.blit(carro4, (posicao_x4, posicao_y4))  
        tela.blit(carro3, (posicao_x3, posicao_y3))  
        tela.blit(carro2, (posicao_x2, posicao_y2))  
        tela.blit(carro, (posicao_x, posicao_y))  
        pygame.display.update()

    if status == "vitoria":
        tela.fill((0, 0, 0))
        tela.blit(backgroundVitoria, (0, 0))
        pygame.display.update()

        if teclas[pygame.K_a]:
            status = "jogando"

        elif teclas[pygame.K_e]:
            tela_aberta = False

    elif status == "game_over":
        tela.fill((0, 0, 0))
        tela.blit(backgroundGameOver, (0, 0))
        pygame.display.update()
   
        if teclas[pygame.K_a]:
            status = "jogando"

        elif teclas[pygame.K_e]:
            tela_aberta = False

pygame.quit()