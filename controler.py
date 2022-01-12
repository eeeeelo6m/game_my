import pygame,model,veiw
from pygame import event
pygame.init()
TIMER_DRAW_ZOMBY2=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY2,1000)
def control():
    e = event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type==TIMER_DRAW_ZOMBY2:
            veiw.draw_zomby_2()

    model.dvigenie_zomby()























