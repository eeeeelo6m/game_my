import pygame,model,veiw,random
from pygame import event
pygame.init()
TIMER_DRAW_ZOMBY2=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY2,random.randint(0,2000),1)
TIMER_DRAW_ZOMBY3=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY3,random.randint(0,2000),1)
TIMER_DRAW_ZOMBY4=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY4,random.randint(0,2000),1)
TIMER_DRAW_ZOMBY5=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY5,random.randint(0,2000),1)
TIMER_DRAW_ZOMBY6=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY6,random.randint(2000,5000),1)
TIMER_DRAW_ZOMBY7=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY7,random.randint(2000,5000),1)
TIMER_DRAW_RASTENIA=event.custom_type()
pygame.time.set_timer(TIMER_DRAW_RASTENIA,2000,1)
def control():
    e = event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type==TIMER_DRAW_ZOMBY2:
            model.add_zombi_2()
        if r.type==TIMER_DRAW_ZOMBY3:
            model.add_zombi_3()
        if r.type==TIMER_DRAW_ZOMBY4:
            model.add_zombi_4()
        if r.type==TIMER_DRAW_ZOMBY5:
            model.add_zombi_5()
        if r.type==TIMER_DRAW_ZOMBY6:
            model.add_zombi_6()
        if r.type==TIMER_DRAW_ZOMBY7:
            model.add_zombi_7()
        if r.type==TIMER_DRAW_RASTENIA:
            model.groho_strel_vistrel()
            pygame.time.set_timer(TIMER_DRAW_RASTENIA, 2000, 1)



    model.dvigenie_vistrel()

    model.dvigenie_zomby()























