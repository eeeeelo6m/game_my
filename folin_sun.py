import pygame
from pygame import draw

class foling_sun:
    def __init__(self,xfol):
        self.xfol=xfol
        self.yfol=-30

        self.obect_sun=pygame.Rect(self.xfol,self.yfol,50,50)
    def fol(self):
        self.speedy = 7 / 10
        self.yfol += self.speedy
        self.obect_sun.y =self.yfol



    def draw_sun(self,screen):
        # draw.rect(screen,[0,0,0],self.obect_sun)
        pass
