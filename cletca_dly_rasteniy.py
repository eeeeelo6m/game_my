import pygame
from pygame import draw
class cletca_rasteniy():
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.obect_cletca=pygame.Rect(self.x,self.y,90,90)
        self.sostoynie='svobodno'

    def draw(self,screen,):
        draw.rect(screen, self.color, self.obect_cletca)

