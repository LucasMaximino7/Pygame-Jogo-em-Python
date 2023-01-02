import pygame
import random


def jogo_2d():
    pygame.init()

    #Variaveis globais
    x = 900
    y = 600
    timer1 = 120
    def respawn():
        x = random.randint(1200, 1550)
        y = random.randint(210, 364)
        return[x,y]
    def respawn2():
        x1 = random.randint(1200, 2700)
        y1 = random.randint(210, 364)
        return[x1,y1]

    vida = 3
    pontos = 0

    coracao_x = 8000
    coracao_y = 360

    espinho_x = 1500
    espinho_y = 372

    def respawn_coracao():
        coracao_x = random.randint(5500,8600)
        coracao_y = random.randint(210, 364)
        return [coracao_x,coracao_y]

    def respawn_espinhos():
        x = random.randint(2000, 5600)
        y = random.randint(372, 374)
        return[x,y]

    font = pygame.font.SysFont('arial black',30)

    chao = pygame.image.load('Chao.png')
    chao = pygame.transform.scale(chao,(900,600))

    chao2 = pygame.image.load('Chao2.png')
    chao2 = pygame.transform.scale(chao2,(900,600))

    chao3 = pygame.image.load('Chao3.png')
    chao3 = pygame.transform.scale(chao3,(900,600))

    chao4 = pygame.image.load('Chao4.png')
    chao4 = pygame.transform.scale(chao4,(900,600))

    hadogen = pygame.image.load("tiro.png")
    hadogen = pygame.transform.scale(hadogen,(50,50))

    hadogen2 = pygame.image.load("tiro2.png")
    hadogen2 = pygame.transform.scale(hadogen2,(50,50))

    espinho = pygame.image.load("Espinhos.png")
    espinho = pygame.transform.scale(espinho,(65,65))

    velocidade_missil = 10
    pos_x_missil = 450
    pos_y_missil = 375

    atirar_direita = False
    atirar_esquerda = False
    triggered = False
    timer2 = 0

    pode = True
    gameover = pygame.image.load("gameover.png")
    tentarnovamente = pygame.image.load("tentarnovamente.png")

    coracao = pygame.image.load("coracao.png")
    coracao = pygame.transform.scale(coracao,(38,38))

    coracao_rect = coracao.get_rect()

    personagem = pygame.image.load("parado.png")
    personagem = pygame.transform.scale(personagem,(56,75))

    personagem_direita = pygame.image.load("direita.png")
    personagem_direita = pygame.transform.scale(personagem_direita,(53,75))

    personagem_esquerda = pygame.image.load("esquerda.png")
    personagem_esquerda = pygame.transform.scale(personagem_esquerda,(53,75))

    alien = pygame.image.load("alien.png")
    alien = pygame.transform.scale(alien,(64,65))

    alien2 = pygame.image.load("alien.png")
    alien2 = pygame.transform.scale(alien2,(64,65))

    hadogen_rect = hadogen.get_rect()
    personagem_rect = personagem.get_rect()
    alien_rect = alien.get_rect()
    alien2_rect = alien.get_rect()
    espinho_rect = espinho.get_rect()

    vel_alien = 4.5

    pos_x_alien = 1250
    pos_y_alien = 360

    pos_x_alien2 = 1600
    pos_y_alien2 = 360

    pos_x_personagem = 400
    pos_y_personagem = 360
    delay = 14
    velocidade = 4
    janela = pygame.display.set_mode((x,y))
    pygame.display.set_caption("Jogo")

    pygame.time.delay(delay)

    janela_aberta = True
    while janela_aberta :
        teclas = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        if teclas[pygame.K_ESCAPE]:
            break
        if vel_alien < 9:
            vel_alien += 0.0015
            velocidade += 0.0004
        elif vel_alien < 11 and vel_alien >= 9:
            vel_alien += 0.0007
            velocidade += 0.00020
        elif vel_alien < 13 and vel_alien >= 11:
            vel_alien += 0.0003
            velocidade += 0.00008
        elif vel_alien >= 15:
            vel_alien += 0.00017
            velocidade += 0.00004

        if pontos < 10:
            rel_x = x % chao.get_rect().width
            janela.blit(chao,(rel_x - chao.get_rect().width,0))
            if rel_x < 920:
                janela.blit(chao,(rel_x,0))

        elif pontos >= 10 and pontos < 20:
            rel_x = x % chao2.get_rect().width
            janela.blit(chao2,(rel_x - chao2.get_rect().width,0))
            if rel_x < 920:
                janela.blit(chao2,(rel_x,0))

            janela.blit(alien2,(pos_x_alien2,pos_y_alien2))

            pos_x_alien2 -= vel_alien

        elif pontos >= 20 and pontos < 30:
            rel_x = x % chao3.get_rect().width
            janela.blit(chao3,(rel_x - chao3.get_rect().width,0))
            if rel_x < 920:
                janela.blit(chao3,(rel_x,0))

            janela.blit(alien2,(pos_x_alien2,pos_y_alien2))

            pos_x_alien2 -= vel_alien
        elif pontos >= 30:
            rel_x = x % chao4.get_rect().width
            janela.blit(chao4,(rel_x - chao4.get_rect().width,0))
            if rel_x < 920:
                janela.blit(chao4,(rel_x,0))

            janela.blit(alien2,(pos_x_alien2,pos_y_alien2))

            pos_x_alien2 -= vel_alien

        if pontos > 5:
            if personagem_rect.colliderect(alien2_rect) or pos_x_alien2 < -25:
                print("Colision")
                vida -= 1
                pos_x_alien2 = respawn2()[0]
                pos_y_alien2 = respawn2()[1]
            elif hadogen_rect.colliderect(alien2_rect) and not hadogen_rect.colliderect(personagem_rect):
                print("Colision")
                pos_x_alien2 = respawn2()[0]
                pos_y_alien2 = respawn2()[1]
                pontos += 1


        x -= velocidade

        print(f"{espinho_x}")

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a] and pos_x_personagem > -30:
            pos_x_personagem -= 7
            if not triggered:
                pos_x_missil -= 7
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d] and pos_x_personagem < 823:
            pos_x_personagem +=7
            if not triggered:
                pos_x_missil += 7
        if teclas[pygame.K_UP] or teclas[pygame.K_w] and pos_y_personagem > 210:
            pos_y_personagem -= 7
            if not triggered:
                pos_y_missil -= 7
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s] and pos_y_personagem < 360:
            pos_y_personagem += 6
            if not triggered:
                pos_y_missil += 6

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a] and pos_x_personagem > -30:
            janela.blit(personagem_esquerda,(pos_x_personagem,pos_y_personagem))
            if pode == True:
                if teclas[pygame.K_q]:
                    atirar_esquerda = True
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d] and pos_x_personagem < 823:
            janela.blit(personagem_direita,(pos_x_personagem,pos_y_personagem))
            if pode == True:
                if teclas[pygame.K_q]:
                    atirar_direita = True
        elif teclas[pygame.K_UP] or teclas[pygame.K_w] and pos_y_personagem > 260:
            janela.blit(personagem,(pos_x_personagem,pos_y_personagem))
        elif teclas[pygame.K_DOWN] or teclas[pygame.K_s] and pos_y_personagem < 360:
            janela.blit(personagem,(pos_x_personagem,pos_y_personagem))
        else:
            janela.blit(personagem,(pos_x_personagem,pos_y_personagem))
            if pode == True:
                if teclas[pygame.K_q]:
                    atirar_direita = True
        
        pos_x_alien -= vel_alien
        coracao_x -= 6

        janela.blit(coracao,(coracao_x,coracao_y))

        if coracao_x < 10:
            coracao_x = respawn_coracao()[0]
            coracao_y = respawn_coracao()[1]


        #SKILLS
        if atirar_direita == True:
            hadogen = pygame.transform.scale(hadogen,(50,50))
            ataque2 = font.render(f"Skill Ataque Recarregando ", True,(0,0,0))
            janela.blit(ataque2,(10,7))
            pode = False
            triggered = True
            
            if triggered == True:
                janela.blit(hadogen,(pos_x_missil,pos_y_missil))

            if pos_x_missil > 930 or hadogen_rect.colliderect(alien_rect) or hadogen_rect.colliderect(alien2_rect):
                triggered = False
                pos_x_missil = pos_x_personagem
                pos_y_missil = pos_y_personagem
                atirar_direita = False
                pode = True

            pos_x_missil += velocidade_missil + 1

        elif atirar_esquerda == True:
            ataque2 = font.render(f"Skill Ataque Recarregando ", True,(0,0,0))
            janela.blit(ataque2,(10,7))
            pode = False
            triggered = True

            if triggered == True:
                janela.blit(hadogen2,(pos_x_missil,pos_y_missil))

            if pos_x_missil < 0 or hadogen_rect.colliderect(alien_rect) or hadogen_rect.colliderect(alien2_rect):
                triggered = False
                pos_x_missil = pos_x_personagem
                pos_y_missil = pos_y_personagem
                atirar_esquerda = False
                pode = True

            pos_x_missil -= velocidade_missil + 3
        else:
            ataque = font.render(f"Skill Ataque pronto: Q ", True,(0,0,0))
            janela.blit(ataque,(10,7))

        timer1 += 1
        
        if timer1 >= 120:
            dash = font.render(f"Skill Dash pronto: E", True,(0,0,0))
            janela.blit(dash,(10,42))
            if teclas[pygame.K_RIGHT]:
                if teclas[pygame.K_e]:
                    pos_x_personagem += 265
                    pos_x_missil += 265
                    timer1 = 0
            if teclas[pygame.K_LEFT]:
                if teclas[pygame.K_e]:
                    pos_x_personagem -= 265
                    pos_x_missil -= 265
                    timer1 = 0
        else:
            dashRecarga = font.render(f"Dash Recarregando ", True,(0,0,0))
            janela.blit(dashRecarga,(10,42))

        if pos_x_personagem < -31:
            pos_x_personagem = -32
        if pos_x_personagem > 822:
            pos_x_personagem = 821
        
        janela.blit(alien,(pos_x_alien,pos_y_alien))
        delay = 25

        if vida >= 3:
            janela.blit(coracao,(700,10))
            janela.blit(coracao,(750,10))
            janela.blit(coracao,(800,10))
        elif vida == 2:
            janela.blit(coracao,(700,10))
            janela.blit(coracao,(750,10))
        elif vida == 1:
            janela.blit(coracao,(700,10))

        personagem_rect.x = pos_x_personagem
        personagem_rect.y = pos_y_personagem

        alien2_rect.x = pos_x_alien2
        alien2_rect.y = pos_y_alien2

        hadogen_rect.x = pos_x_missil
        hadogen_rect.y = pos_y_missil

        coracao_rect.x = coracao_x
        coracao_rect.y = coracao_y

        alien_rect.x = pos_x_alien
        alien_rect.y= pos_y_alien

        espinho_rect.x = espinho_x
        espinho_rect.y = espinho_y

        score = font.render(f"Vida: {vida}", True,(0,0,0))
        janela.blit(score,(10,80))

        Points = font.render(f"Pontos: {pontos}", True,(0,0,0))
        janela.blit(Points,(10,115))
        

        #COLISoes
        if personagem_rect.colliderect(alien_rect) or pos_x_alien < -15:
            print("Colision")
            vida -= 1
            pos_x_alien = respawn()[0]
            pos_y_alien = respawn()[1]
        elif hadogen_rect.colliderect(alien_rect) and not hadogen_rect.colliderect(personagem_rect):
            print("Colision")
            pos_x_alien = respawn()[0]
            pos_y_alien = respawn()[1]
            pontos += 1
        

        if coracao_rect.colliderect(personagem_rect):
            coracao_x = respawn_coracao()[0]
            coracao_y = respawn_coracao()[1]
            vida += 1

        if pontos >= 0:
            janela.blit(espinho,(espinho_x,espinho_y))
            if personagem_rect.colliderect(espinho_rect):
                print("Colision")
                vida -= 1
                espinho_x = respawn_espinhos()[0]
                espinho_y = respawn_espinhos()[1]
            
            elif espinho_x < -25:
                espinho_x = respawn_espinhos()[0]
                espinho_y = respawn_espinhos()[1]

            elif personagem_rect.colliderect(espinho_rect) and not hadogen_rect.colliderect(personagem_rect):
                print("Colision")
                espinho_x = respawn_espinhos()[0]
                espinho_y = respawn_espinhos()[1]
        
        espinho_x -= 4
        
        #SE A VIDA ABAIXAR DE 0
        if vida <= 0:
            pygame.init()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break

                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_ESCAPE]:
                    break
                
                pygame.time.delay(25)
                janela = pygame.display.set_mode((900,600))
                pygame.display.set_caption("GAME OVER")
                timer2 += 1

                if timer2 < 30:
                    janela.blit(gameover,(0,0))
                elif timer2 > 30:
                    janela.blit(tentarnovamente,(0,0))
                    if teclas[pygame.KSCAN_KP_ENTER] or teclas[pygame.K_SPACE] or teclas[pygame.K_KP_ENTER]:
                        jogo_2d()
                pygame.display.update()

            pygame.quit()
                    
        
        pygame.display.update()

    pygame.quit()

jogo_2d()