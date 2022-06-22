import pygame,help,random
from pygame import draw


class Rastenie_goroh:
    def __init__(self, x, y,mogno_strelyt_rasteniu=None):
        self.TIMER_VISTREL=pygame.event.custom_type()
        pygame.time.set_timer(self.TIMER_VISTREL,3000)
        self.brocol_cartinka = pygame.image.load('picture/броколь.png')
        self.brocol_cartinka = help.izmeni_kartinku(self.brocol_cartinka, 90, 90, [252, 252, 252], 5)
        self.damag=1
        self.heal = 300
        self.x = x
        self.y = y
        self.obet_rasteniy = pygame.Rect(self.x, self.y, 90, 90)
        self.mogno_strelyt_rasteniu=mogno_strelyt_rasteniu
        self.obect_vistrel = pygame.Rect(self.x, self.y, 10, 10)
        self.stoimost=100
    def reg_vistrel(self):
        self.mogno_strelyt_rasteniu=False
        pygame.time.set_timer(self.TIMER_VISTREL, random.randint(2000,4000))
    def draw_vistrel(self, screen):
        draw.rect(screen, [255, 0, 0], self.obect_vistrel)
    def draw_rastenie(self, screen):
        # draw.rect(screen,[0,0,0],self.obet_rasteniy)
        screen.blit(self.brocol_cartinka, [self.x, self.y])



