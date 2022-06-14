import pygame
from pygame import draw

print(pygame.font.get_fonts())
shrift = pygame.font.SysFont('comicsansms', 25)

class schet():
    def __init__(self,x,y,number_schet,name):
        self.x=x
        self.y=y
        self.number_schet=number_schet
        self.name=name
        self.schet_cartinka = shrift.render(str(self.number_schet),True,[0,0,0])
    def draw_schet(self,screen):
        self.schet_cartinka = shrift.render(str(self.number_schet), True, [0, 0, 0])
        screen.blit(self.schet_cartinka, [self.x,self.y])










# cartinca_goals_left = shrift.render(str(goal_igroc_left), True, [123, 1, 255])