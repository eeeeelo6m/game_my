import pygame
from pygame import draw

class Rastenie_goroh:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.obet_rasteniy=pygame.Rect(self.x,self.y,30,30)
        self.obect_vistrel=pygame.Rect(self.x,self.y,10,10)


    def draw_rastenie(self,screen):
        draw.rect(screen,[0,0,0],self.obet_rasteniy)

