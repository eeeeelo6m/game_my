import model, zomby
from pygame import draw, display

screen = display.set_mode([1050, 650])


def veiw():
    screen.fill([20, 255, 20])
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
    for goroho_strel_vistrel in model.goroho_strel_vistrels:
        goroho_strel_vistrel.draw_vistrel(screen)



    display.flip()
