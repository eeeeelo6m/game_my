import pygame

class foling_sun:
    def __init__(self,xfol,):
        self.xfol=xfol
        self.yfol=700
        self.sun_speed=5
        self.obect_sun=pygame.Rect(self.xfol,self.yfol,30,30)