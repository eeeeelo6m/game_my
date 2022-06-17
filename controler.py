import pygame, model,random
from pygame import event


pygame.init()
TIMER_DRAW_ZOMBY = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY,30000,1)

TIMER_DRAW_RASTENIA = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)
TIMER_FOLING_SUN = event.custom_type()
pygame.time.set_timer(TIMER_FOLING_SUN, 10000, 1)
TIMER_ADD_BIGSUN=event.custom_type()
def control():

    e = event.get()

    for r in e:
        model.uron_rasteniy_brocol()
        if r.type == pygame.QUIT:
            exit()
        if r.type == TIMER_DRAW_ZOMBY:
            model.add_zomby()
            pygame.time.set_timer(TIMER_DRAW_ZOMBY,random.randint(5000,10000),1)
        if r.type == TIMER_DRAW_RASTENIA:
            model.zapusk_vistrel()
            pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)
        if r.type==pygame.MOUSEBUTTONDOWN and r.button==pygame.BUTTON_LEFT:
            model.pocupka_rasteniy_brocol(r.pos[0],r.pos[1])
            model.pocupka_rasteniy_sunflover(r.pos[0],r.pos[1])
            model.sbor_bigsuns(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEMOTION:
            model.perenos_towar(r.pos[0],r.pos[1])
        if r.type == pygame.MOUSEBUTTONDOWN and r.button == pygame.BUTTON_LEFT:
            model.postonovka_towar(r.pos[0],r.pos[1])
        if model.mogno_puscat==True:
            pygame.time.set_timer(TIMER_ADD_BIGSUN,random.randint(17500,20000))
            model.mogno_puscat=False
        if r.type==TIMER_ADD_BIGSUN:
            model.add_bigsun()

        if r.type == TIMER_FOLING_SUN:
            model.add_sun()
            pygame.time.set_timer(TIMER_FOLING_SUN, random.randint(10000,15000), 1)
        if r.type==pygame.MOUSEBUTTONDOWN and r.button==pygame.BUTTON_LEFT:
            model.sbor_sun(r.pos[0],r.pos[1])





    model.dvigenie_vistrel()
