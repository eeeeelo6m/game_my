import pygame
from pygame import draw

class foling_sun:
    def __init__(self,xfol):
        self.xfol=xfol
        self.yfol=-30
        self.sobrano=False
        self.obect_sun=pygame.Rect(self.xfol,self.yfol,50,50)
    def fol(self,speedx=None,speedy=None,x=None,y=None):
        if self.sobrano==False:
            self.speeedy = 7 / 10
            self.yfol += self.speeedy
            self.obect_sun.y =self.yfol
        else:
            if self.xfol<=410:
                self.xfol=410
                self.obect_sun.x = self.xfol
                speedx=0
            else:
                self.xfol -= speedx
                self.obect_sun.x=self.xfol
            if self.yfol<=10:
                self.yfol=10
                self.obect_sun.y = self.yfol
                speedy=0
            else:
                self.yfol -= speedy
                self.obect_sun.y=self.yfol




    def draw_sun(self,screen):
        #draw.rect(screen,[0,0,0],self.obect_sun)
        pass
