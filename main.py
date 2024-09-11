import pygame, time
from pygame.locals import *
from sys import exit
from random import randint

#inicializa as expecificações do quadro
PRETO = (0, 0, 0)
LARGURA = 640
ALTURA = 480
x = 250
y = 0
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
pygame.init()

#inicia imagem de fundo
imagem_fundo = pygame.image.load('BackGround.jpg')

#inicia musica
musica_de_fundo = pygame.mixer.music.load('I Know You are Out There.mp3')
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('mixkit-player-jumping-in-a-video-game-2043.wav')

fonte = pygame.font.SysFont('gabriola', 40, True, True)

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Survivor.IO')
clock = pygame.time.Clock()
distancia_do_movimento = 10

tamanho = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

while True:
    window.blit(tamanho, (0, 0))
    window.fill(PRETO)
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                x=x-distancia_do_movimento
            elif event.key ==K_d or event.key == K_RIGHT:
                x=x+distancia_do_movimento
            elif event.key == K_s or event.key == K_DOWN:
                y=y+distancia_do_movimento
            elif event.key == K_w or event.key == K_UP:
                y=y-distancia_do_movimento'''
    mensagem = f'Pontos : {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - distancia_do_movimento
    elif pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + distancia_do_movimento
    elif pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + distancia_do_movimento
    elif pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - distancia_do_movimento

    ret_rosa = pygame.draw.rect(window, (200, 80, 199), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(window, (0, 150, 255), (x_azul, y_azul, 40, 50))

    if ret_rosa.colliderect(ret_azul):  # toda vez que houver colisão, as posições do retângulo azul irão mudar
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        som_colisao.play()
    window.blit(texto_formatado, (450, 40))
    pygame.display.update()
    if y > ALTURA:
        y = 0
    elif y < 0:
        y = ALTURA
    # y=y+1
    if x > LARGURA:
        x = 0
    elif x < 0:
        x = LARGURA
