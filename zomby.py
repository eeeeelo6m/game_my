import pygame,random
from pygame import draw,font
pygame.init()
f=font.SysFont('arial',20)
class vrag_zomby():
    def __init__(self,x,y,speedx,pologenie,heal,damage,vid):
        self.heal=heal
        self.damag=damage
        self.x=x
        self.y=y
        self.pologenie=pologenie
        self.speedx=speedx
        self.obect_zomby=pygame.Rect(self.x,self.y,30,90)
        self.vid=vid
    def draw_zomby(self,color,screen:pygame.Surface):
        draw.rect(screen,color,self.obect_zomby)
        t=f.render(str(self.heal),True,[0,0,0])
        screen.blit(t,self.obect_zomby)



    def dvigenie(self):
        if self.pologenie == 'dvigenie':
            self.x -= self.speedx
            self.obect_zomby.x = self.x






