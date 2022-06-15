import help,pygame
from pygame import draw

class happy_sun:
    def __init__(self,x,y):
        self.sunflover_cartinka = pygame.image.load('picture/покерфэйсмен.png')
        self.sunflover_cartinka = help.izmeni_kartinku(self.sunflover_cartinka, 90, 90, [255, 255, 255], 2)
        self.x=x
        self.y=y
        self.obect_sunflover=pygame.Rect(self.x,self.y,[90,90])
        self.obect_bigsun=pygame.Rect(self.x+10,self.y,[70,70])
    def draw_sunflover(self,screen):
        draw.rect(screen,[0,0,0],self.obect_sunflover)
        screen.blit(self.sunflover_cartinka, [self.x, self.y])
    def draw_bigsun(self,screen):
        draw.rect(screen,[255,255,255],self.obect_bigsun)
