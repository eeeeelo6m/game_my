import pygame

class lazer_rastenie:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.heal=500
        self.damage=0.50
        self.obect_lazer=pygame.Rect(self.x,self.y,90,90)
        self.obect_lazer=pygame.Rect(self.x-90,self.y-10,1200-self.x,5)
    def draw_lazer_plant(self):
        pass
    def draw_lazer(self):
        pass