import pygame
from random import randint

class Jogador:
    def __init__(self, largura, altura):
        self.x = 250
        self.y = 0
        self.largura = largura
        self.altura = altura
        self.distancia_do_movimento = 10
        self.cor = (255, 0, 0, 0)
        self.ninjaParado = pygame.image.load('Imagens/NinjaParado-removebg-preview.png').convert_alpha()
        self.ninjaParado = pygame.transform.scale(self.ninjaParado, (50,70))
        
        self.sprites_direita = [pygame.image.load(f'Imagens/Ninja{i}-removebg-preview.png').convert_alpha() for i in range(1, 15)]
        self.sprites_direita = [pygame.transform.scale(image, (50,70)) for image in self.sprites_direita]
        self.sprite_direita_quadro = 0
        
        self.sprite_esquerda = [pygame.transform.flip(image, True, False) for image in self.sprites_direita]
        self.sprite_esquerda_quadro= 0

    def mover(self, window):
        teclas = pygame.key.get_pressed()
        if not(teclas[pygame.K_a] or teclas[pygame.K_LEFT] or teclas[pygame.K_d] or teclas[pygame.K_RIGHT]):
            window.blit(self.ninjaParado, (self.x, self.y))
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            window.blit(self.sprite_esquerda[self.sprite_esquerda_quadro] , (self.x, self.y))
            self.x -= self.distancia_do_movimento
            self.desenharEsquerda(window)
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            window.blit(self.sprites_direita[self.sprite_direita_quadro] , (self.x, self.y))
            self.x += self.distancia_do_movimento
            self.desenharDireita(window)
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.distancia_do_movimento
        elif teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.distancia_do_movimento

        # Movimentação no eixo vertical e horizontal
        if self.y > self.altura:
            self.y = 0
        elif self.y < 0:
            self.y = self.altura

        if self.x > self.largura:
            self.x = 0
        elif self.x < 0:
            self.x = self.largura
            
    def desenharDireita(self, window):
        self.sprite_direita_quadro+=1
        if self.sprite_direita_quadro >= len(self.sprites_direita):
            self.sprite_direita_quadro=0
            
    def desenharEsquerda(self, window):
        self.sprite_esquerda_quadro+=1
        if self.sprite_esquerda_quadro >= len(self.sprite_esquerda):
            self.sprite_esquerda_quadro=0
        #self.sprite_esquerda = 
    def desenhar(self, window):
        surface = pygame.Surface((800, 600), pygame.SRCALPHA)
        ret_rosa = pygame.draw.rect(surface, self.cor, (self.x, self.y, 40, 50))
        return ret_rosa
        
            