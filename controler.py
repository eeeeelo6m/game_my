import pygame, model,random
from pygame import event


pygame.init()
TIMER_DRAW_ZOMBY = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY, 3000)

TIMER_DRAW_RASTENIA = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)
TIMER_FOLING_SUN = event.custom_type()
pygame.time.set_timer(TIMER_FOLING_SUN, 500, 1)
def control():

    e = event.get()

    for r in e:
        model.uron_rasteniy()
        if r.type == pygame.QUIT:
            exit()
        if r.type == TIMER_DRAW_ZOMBY:
            model.add_zomby()
        if r.type == TIMER_DRAW_RASTENIA:
            model.zapusk_vistrel()
            pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)
        if r.type==pygame.MOUSEBUTTONDOWN and r.button==pygame.BUTTON_LEFT:
            model.pocupka_rasteniy(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEMOTION:
            model.perenos_towar(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEBUTTONDOWN and r.button == pygame.BUTTON_LEFT:
            model.postonovka_towar(r.pos[0],r.pos[1])
        if r.type == TIMER_FOLING_SUN:
            model.add_sun()
            pygame.time.set_timer(TIMER_FOLING_SUN, random.randint(10000,15000), 1)






    model.dvigenie_vistrel()
