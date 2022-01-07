import pygame
from pygame import draw
class cletca_rasteniy():
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.obect_cletca=pygame.Rect(self.x,self.y,90,90)

    def draw(self,screen,color):
        draw.rect(screen, color, self.obect_cletca)

