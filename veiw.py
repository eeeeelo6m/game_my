import model, help, pygame, folin_sun
from pygame import draw, display

screen = display.set_mode([1200, 650])
home_cartinca = pygame.image.load('picture/Без имени.png')
home_cartinca = help.izmeni_kartinku(home_cartinca, 180, 450, [255, 255, 255], 1)

brocol_cartinka_towar = pygame.image.load('picture/броколь.png')
brocol_cartinka_towar = help.izmeni_kartinku(brocol_cartinka_towar, 50, 50, [252, 252, 252], 5)
brocol_cartinka_towar_perenos = pygame.image.load('picture/броколь.png')
brocol_cartinka_towar_perenos = help.izmeni_kartinku(brocol_cartinka_towar, 70, 70, [252, 252, 252], 5)
sun_towar_cartinka = pygame.image.load('picture/солнцебест.png')
sun_towar_cartinka = help.izmeni_kartinku(sun_towar_cartinka, 70, 70, [255, 255, 255], 100)
sunflover_towar_cartinka = pygame.image.load('picture/покерфэйсмен.png')
sunflover_towar_cartinka = help.izmeni_kartinku(sunflover_towar_cartinka, 50, 50, [255, 255, 255], 1)
sunflover_cartinka_towar_perenos=pygame.image.load('picture/покерфэйсмен.png')
sunflover_cartinka_towar_perenos = help.izmeni_kartinku(sunflover_cartinka_towar_perenos, 70, 70, [255, 255, 255], 1)



def veiw():
    screen.fill([110, 255, 110])
    for cletcas_1 in model.cletcas_1:
        cletcas_1.draw(screen)
        model.add_cletca_1()

    for cletcas_2 in model.cletcas_2:
        cletcas_2.draw(screen)
        model.add_cletca_2()

    for cletcas_3 in model.cletcas_3:
        cletcas_3.draw(screen)
        model.add_cletca_3()

    for cletcas_4 in model.cletcas_4:
        cletcas_4.draw(screen)
        model.add_cletca_4()

    for cletcas_5 in model.cletcas_5:
        cletcas_5.draw(screen)
        model.add_cletca_5()

    for goroho_strels in model.goroho_strels:
        goroho_strels.draw_rastenie(screen)
    for goroho_strel_vistrel in model.goroho_strel_vistrels:
        goroho_strel_vistrel.draw_vistrel(screen)
    for sunflovers in model.sunflovers:
        sunflovers.draw_sunflover(screen)
    pygame.draw.rect(screen, [133, 45, 27], model.rect_magazin)

    # pygame.draw.rect(screen,[0,0,0],model.rect_towar_brocol)
    screen.blit(brocol_cartinka_towar, [model.rect_towar_brocol.x, model.rect_towar_brocol.y])

    # pygame.draw.rect(screen,[0,0,0],model.rect_towar_sunflover)
    screen.blit(sunflover_towar_cartinka,[model.rect_towar_sunflover.x,model.rect_towar_sunflover.y])


    # draw.rect(screen,[0,0,0],model.home)
    screen.blit(home_cartinca, [0, 90])

    draw.rect(screen, [100, 200, 100], model.rect_sun_tovar)
    screen.blit(sun_towar_cartinka, [model.rect_sun_tovar.x, model.rect_sun_tovar.y])


    for schet in model.schets:
        schet.draw_schet(screen)



    if model.cupleniy_towar != None and model.cupleniy_towar.cacoe_rastenie=='brocol':
        # model.cupleniy_towar.draw_cupleniy_towar(screen)
        screen.blit(brocol_cartinka_towar_perenos, [model.cupleniy_towar.x, model.cupleniy_towar.y])
    elif model.cupleniy_towar != None and model.cupleniy_towar.cacoe_rastenie=='sunflover':
        # model.cupleniy_towar.draw_cupleniy_towar(screen)
        screen.blit(sunflover_cartinka_towar_perenos,[model.cupleniy_towar.x, model.cupleniy_towar.y])


    for zomby_1 in model.zombys:
        if model.zomby_vrag is not None:
            zomby_1.draw_zomby([255, 10, 10], screen)


    for sun_rect in model.sun_rects:
        if model.sun_rect is not None:
            sun_rect.draw_sun(screen)



    display.flip()
