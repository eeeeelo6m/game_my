import pygame, model, veiw, random
from pygame import event

pygame.init()
TIMER_DRAW_ZOMBY = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(0, 3000))

pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(0, 3000))

pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(0, 3000))

pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(0, 3000))

pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(3000, 6000))

pygame.time.set_timer(TIMER_DRAW_ZOMBY, random.randint(3000, 6000))

TIMER_DRAW_RASTENIA = event.custom_type()
pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)
TIMER_URON_RASTENIU = event.custom_type()
pygame.time.set_timer(TIMER_URON_RASTENIU, 1000, 1)


def control():
    e = event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type == TIMER_DRAW_ZOMBY:
            model.add_zomby()

        if r.type == TIMER_DRAW_RASTENIA:
            model.groho_strel_vistrel()
            pygame.time.set_timer(TIMER_DRAW_RASTENIA, 3000, 1)

        if TIMER_URON_RASTENIU == r.type:
            model.uron_rasteniy()

    model.dvigenie_vistrel()

    model.dvigenie_zomby()
