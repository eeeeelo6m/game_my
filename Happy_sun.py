import help,pygame,random
from pygame import draw

class happy_sun:
    def __init__(self,x=None,y=None,mogno_puscat=None):
        self.TIMER_ADD_BIGSUN=pygame.event.custom_type()
        pygame.time.set_timer(self.TIMER_ADD_BIGSUN,random.randint(12500,15000))
        self.mogno_puscat=mogno_puscat
        self.sunflover_cartinka = pygame.image.load('picture/покерфэйсмен.png')
        self.sunflover_cartinka = help.izmeni_kartinku(self.sunflover_cartinka, 90, 90, [255, 255, 255], 2)
        self.sun_cartinka = pygame.image.load('picture/солнцебест.png')
        self.sun_cartinka = help.izmeni_kartinku(self.sun_cartinka, 70, 70, [255, 255, 255], 50)
        self.x=x
        self.y=y
        self.heal=150
        self.obect_sunflover=pygame.Rect(self.x,self.y,90,90)
        self.obect_bigsun=pygame.Rect(self.x,self.y,70,70)
    def draw_sunflover(self,screen):
        # draw.rect(screen,[0,0,0],self.obect_sunflover)
        screen.blit(self.sunflover_cartinka, [self.x, self.y])
    def reg_bigsun(self):
        pygame.time.set_timer(self.TIMER_ADD_BIGSUN, 15000)
    def draw_bigsun(self,screen):
        #draw.rect(screen,[255,255,255],self.obect_bigsun)
        screen.blit(self.sun_cartinka,[self.x,self.y])
