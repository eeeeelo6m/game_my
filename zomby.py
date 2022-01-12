import pygame,random
from pygame import draw
class vrag_zomby():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.obect_zomby=pygame.Rect(self.x,self.y,30,90)

    def draw_zomby(self,color,screen):
        draw.rect(screen,color,self.obect_zomby)




