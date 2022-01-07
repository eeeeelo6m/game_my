import model
from pygame import draw,display
screen=display.set_mode([1050,650])
def veiw():

    model.cletca_1.draw(screen,[0,255,255])

    model.cletca_2.draw(screen,[0,0,255])
    model.cletca_3.draw(screen,[0,255,255])
    model.cletca_4.draw(screen,[0,0,255])
    model.cletca_5.draw(screen,[0,255,255])
    display.flip()

