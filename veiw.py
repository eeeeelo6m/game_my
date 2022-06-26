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
banana_towar_cartinka=pygame.image.load('picture/банана.png')
banana_towar_cartinka= help.izmeni_kartinku(banana_towar_cartinka,50,50,[255,255,255],10)
banana_perenos_cartinka=pygame.image.load('picture/банана.png')
banana_perenos_cartinka= help.izmeni_kartinku(banana_towar_cartinka,70,70,[255,255,255],10)
lopata_cartinka=pygame.image.load('picture/лопата.png')
lopata_cartinka= help.izmeni_kartinku(lopata_cartinka,70,70,[255,255,255],10)




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
    for banana in model.bananas:
        banana.draw_banan(screen)
    for vistrel in model.bananas_vistrels:
        vistrel.draw_lazer(screen)
    pygame.draw.rect(screen, [133, 45, 27], model.rect_magazin)

    # pygame.draw.rect(screen,[0,0,0],model.rect_towar_brocol)
    screen.blit(brocol_cartinka_towar, [model.rect_towar_brocol.x, model.rect_towar_brocol.y])

    # pygame.draw.rect(screen,[0,0,0],model.rect_towar_sunflover)
    screen.blit(sunflover_towar_cartinka,[model.rect_towar_sunflover.x,model.rect_towar_sunflover.y])

    # pygame.draw.rect(screen,[0,0,0],model.rect_towar_banana)
    screen.blit(banana_towar_cartinka,[model.rect_towar_banana.x,model.rect_towar_banana.y])


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
    elif model.cupleniy_towar !=None and model.cupleniy_towar.cacoe_rastenie=='banana':
        # model.cupleniy_towar.draw_cupleniy_towar(screen)
        screen.blit(banana_perenos_cartinka,[model.cupleniy_towar.x,model.cupleniy_towar.y])
    if len(model.bigsuns)>=1:
        for bigsuns in model.bigsuns:
            bigsuns.draw_bigsun(screen)
    if model.vikapovatel is not None:
        # pygame.draw.rect(screen,[0,0,0],model.vikapovatel)
        screen.blit(lopata_cartinka,[model.vikapovatel.x,model.vikapovatel.y])
    # pygame.draw.rect(screen,[0,0,0],model.lapata)
    screen.blit(lopata_cartinka, [model.lapata.x, model.lapata.y])





    for zomby_1 in model.zombys:
        if zomby_1.vid=='standart':
            zomby_1.draw_zomby([255, 10, 10], screen)
    for zomby_1 in model.zombys:
        if zomby_1.vid=='fat':
            zomby_1.draw_zomby([84,154,53], screen)
    for zomby_1 in model.zombys:
        if zomby_1.vid=='brone':
            zomby_1.draw_zomby([91,70,89], screen)


    for sun_rect in model.sun_rects:
        if model.sun_rect is not None:
            sun_rect.draw_sun(screen)



    display.flip()
