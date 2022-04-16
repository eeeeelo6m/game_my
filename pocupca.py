import pygame
from pygame import draw



class Pocupca_towara:
    def __init__(self,x,y,cacoe_rastenie,sostoynie):
        self.x=x
        self.y=y
        self.cacoe_rastenie=cacoe_rastenie
        self.sostoynie=sostoynie
        self.cupleniy_rect=pygame.Rect([x,y],[70,70])
    def draw_cupleniy_towar(self,screen):
        draw.rect(screen, [0, 0, 0], self.cupleniy_rect)
    def perenos(self,x,y):
        self.x=x
        self.y=y
        self.cupleniy_rect.x = self.x
        self.cupleniy_rect.y = self.y