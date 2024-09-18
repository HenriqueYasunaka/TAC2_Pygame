from random import randint
import pygame



class Inimigo:
    def __init__(self, largura, altura):
        self.x = randint(40, 600)
        self.y = randint(50, 430)
        self.cor = (0, 150, 255)
        self.largura = largura
        self.altura = altura

    def desenhar(self, window):
        surface = pygame.Surface((800, 600), pygame.SRCALPHA)
        image = pygame.image.load("imagens/ZumbiAndando1-removebg-preview.png")
        image = pygame.transform.scale(image, (60, 70))
        ret_azul = pygame.draw.rect(surface, self.cor, (self.x, self.y, 40, 50))
        window.blit(image, ret_azul)
        return ret_azul

    def resetar_posicao(self):
        self.x = randint(40, 600)
        self.y = randint(50, 430)
