import pygame
from pygame import event
pygame.init()

def control():
    e = event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()