import pygame,help

class lazer_rastenie:
    def __init__(self,x,y):
        self.TIMER_VISTREL=pygame.event.custom_type()
        pygame.time.set_timer(self.TIMER_VISTREL,6000)
        self.x=x
        self.y=y
        self.heal=500
        self.damage=1
        self.obect_banana=pygame.Rect(self.x,self.y,90,90)
        self.obect_lazer=pygame.Rect(self.x+90,self.y-10,1110-self.x,5)
        self.banana_cartinka = pygame.image.load('picture/банана.png')
        self.banana_cartinka = help.izmeni_kartinku(self.banana_cartinka, 90, 90, [255, 255, 255], 10)
        self.mogu_strelyt=False
    def draw_banan(self,screen):
        # pygame.draw.rect(screen,[0,0,0],self.obect_banana)
        screen.blit(self.banana_cartinka,[self.x,self.y])

    def draw_lazer(self,screen):
        pygame.draw.rect(screen,[20,20,255],self.obect_lazer)

    def reg_vistrel(self):
        self.mogu_strelyt=False
        pygame.time.set_timer(self.TIMER_VISTREL,6000)


