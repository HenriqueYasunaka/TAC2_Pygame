import pygame
from pygame.locals import *
from sys import exit
from Const  import *
from J import *
from I import * 

class Jogo:
    def __init__(self):
        pygame.init()

        
        self.window = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Survivor.IO')

        
        self.musica_de_fundo = pygame.mixer.music.load(MUSICA_DE_FUNDO)
        pygame.mixer.music.play(-1)
        self.som_colisao = pygame.mixer.Sound(SOM_COLISAO)
      
        self.fonte = pygame.font.SysFont(FONTE, TAMANHO_FONTE, NEGRITO, ITALICO)
        self.pontos = 0
        
        self.imagem_fundo = pygame.image.load(IMAGEM_FUNDO)
        self.tamanho = pygame.transform.scale(self.imagem_fundo, (LARGURA, ALTURA))
    
        self.jogador = Jogador(LARGURA, ALTURA)
        self.inimigo = Inimigo(LARGURA, ALTURA)
      
        self.clock = pygame.time.Clock()

    def rodar(self):
        while True:
            self.window.fill(PRETO)
            self.window.blit(self.tamanho, (0,0))
            self.clock.tick(40)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

           
            self.jogador.mover(self.window)
            self.ret_jogador = self.jogador.desenhar(self.window)
            
            self.ret_inimigo = self.inimigo.desenhar(self.window)

            if self.ret_jogador.colliderect(self.ret_inimigo):
                self.inimigo.resetar_posicao()
                self.pontos += 1
                self.som_colisao.play()

            
            mensagem = f'Pontos : {self.pontos}'
            texto_formatado = self.fonte.render(mensagem, True, BRANCO)
            self.window.blit(texto_formatado, (450, 40))

            
            pygame.display.update()

