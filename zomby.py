import pygame,random
from pygame import draw
class vrag_zomby():
    def __init__(self,x,y,speedx,pologenie):
        self.heal=4
        self.damag=1
        self.x=x
        self.y=y
        self.pologenie=pologenie
        self.speedx=speedx
        self.obect_zomby=pygame.Rect(self.x,self.y,30,90)

    def draw_zomby(self,color,screen):
        draw.rect(screen,color,self.obect_zomby)


    def dvigenie(self):
        if self.pologenie != 'poedanie':
            self.x -= self.speedx
            self.obect_zomby.x = self.x






