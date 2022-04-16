import model, help,pygame,pocupca
from pygame import draw, display

screen = display.set_mode([1200, 650])
home_cartinca = pygame.image.load('picture/Без имени.png')
home_cartinca = help.izmeni_kartinku(home_cartinca, 180, 450, [255, 255, 255], 1)
brocol_cartinka = pygame.image.load('picture/броколь.png')
brocol_cartinka=help.izmeni_kartinku(brocol_cartinka,90,90,[252,252,252],5)
brocol_cartinka_towar = pygame.image.load('picture/броколь.png')
brocol_cartinka_towar=help.izmeni_kartinku(brocol_cartinka_towar,50,50,[252,252,252],5)
brocol_cartinka_towar_perenos = pygame.image.load('picture/броколь.png')
brocol_cartinka_towar_perenos=help.izmeni_kartinku(brocol_cartinka_towar,70,70,[252,252,252],5)
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

    for zomby_1 in model.zombys:
        if model.zomby_vrag is not None:
            zomby_1.draw_zomby([255, 10, 10], screen)



    for goroho_strels in model.goroho_strels:
        goroho_strels.draw_rastenie(screen)
        screen.blit(brocol_cartinka,[goroho_strels.x,goroho_strels.y])
    for goroho_strel_vistrel in model.goroho_strel_vistrels:
        goroho_strel_vistrel.draw_vistrel(screen)

    pygame.draw.rect(screen,[133,45,27],model.rect_magazin)
    #pygame.draw.rect(screen,[0,0,0],model.rect_towar)
    screen.blit(brocol_cartinka_towar, [model.rect_towar.x, model.rect_towar.y])

    #draw.rect(screen,[0,0,0],model.home)
    screen.blit(home_cartinca, [0, 90])
    if model.cupleniy_towar!=None:
        #model.cupleniy_towar.draw_cupleniy_towar(screen)
        screen.blit(brocol_cartinka_towar_perenos, [model.cupleniy_towar.x, model.cupleniy_towar.y])

    display.flip()
