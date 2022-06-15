import pygame
from pygame import draw

class foling_sun:
    def __init__(self,xfol):
        self.xfol=xfol
        self.yfol=-30
        self.sobrano=False
        self.obect_sun=pygame.Rect(self.xfol,self.yfol,50,50)
        self.speedy = 7 / 10
        self.speedx=0
    def fol(self):

        self.yfol += self.speedy
        self.obect_sun.y =self.yfol
        self.xfol += self.speedx
        self.obect_sun.x=self.xfol

    def sbor_sun(self):
        self.sobrano=True
        self.speedy=-(self.yfol-10)/50
        self.speedx=-(self.xfol-410)/50





    def draw_sun(self,screen):
        draw.rect(screen,[0,0,0],self.obect_sun)
        pass
