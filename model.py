import cletca_dly_rasteniy, zomby, random, goroho_strel

x1 = 950
x2 = 950
x3 = 950
x4 = 950
x5 = 950
color_cletca_1 = 2
color_cletca_2 = 1
color_cletca_3 = 2
color_cletca_4 = 1
color_cletca_5 = 2
col_cletca_1 = 0
col_cletca_2 = 0
col_cletca_3 = 0
col_cletca_4 = 0
col_cletca_5 = 0
cletcas_1 = []
cletcas_2 = []
cletcas_3 = []
cletcas_4 = []
cletcas_5 = []
zomby_1 = zomby.vrag_zomby(1100, 90)
zomby_2 = zomby.vrag_zomby(1100, 180)
zomby_3 = zomby.vrag_zomby(1100, 270)
zomby_4 = zomby.vrag_zomby(1100, 360)
zomby_5 = zomby.vrag_zomby(1100, 450)
zomby_6 = zomby.vrag_zomby(1100, random.choice([90, 180, 270, 360, 450]))
zomby_7 = zomby.vrag_zomby(1100, 90)
zombys_1 = []
zombys_2 = []
zombys_3 = []
zombys_4 = []
zombys_5 = []
zombys_6 = []
zombys_7 = []
goroho_strel1 = None
goroho_strels = []
goroho_strel_vistrel = None
goroho_strel_vistrels = []
zombys_1.append(zomby_1)
pologenie_1 = 'dvigenie'
pologenie_2 = 'dvigenie'
pologenie_3 = 'dvigenie'
pologenie_4 = 'dvigenie'
pologenie_5 = 'dvigenie'
pologenie_6 = 'dvigenie'
pologenie_7 = 'dvigenie'


def add_cletca_1():
    global cletcas_1, color_cletca_1, x1, col_cletca_1
    if color_cletca_1 == 1 and col_cletca_1 != 10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90, [0, 200, 255])
        color_cletca_1 += 1
        x1 -= 90
        col_cletca_1 += 1
        cletcas_1.append(cletca_1)
    if color_cletca_1 == 2 and col_cletca_1 != 10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90, [0, 255, 255])
        color_cletca_1 -= 1
        x1 -= 90
        col_cletca_1 += 1
        cletcas_1.append(cletca_1)


def add_cletca_2():
    global cletcas_2, color_cletca_2, x2, col_cletca_2
    if color_cletca_2 == 1 and col_cletca_2 != 10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180, [0, 200, 255])
        color_cletca_2 += 1
        x2 -= 90
        col_cletca_2 += 1
        cletcas_2.append(cletca_2)
    if color_cletca_2 == 2 and col_cletca_2 != 10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180, [0, 255, 255])
        color_cletca_2 -= 1
        x2 -= 90
        col_cletca_2 += 1
        cletcas_2.append(cletca_2)


def add_cletca_3():
    global cletcas_3, color_cletca_3, x3, col_cletca_3
    if color_cletca_3 == 1 and col_cletca_3 != 10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270, [0, 200, 255])
        color_cletca_3 += 1
        x3 -= 90
        col_cletca_3 += 1
        cletcas_3.append(cletca_3)
    if color_cletca_3 == 2 and col_cletca_3 != 10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270, [0, 255, 255])
        color_cletca_3 -= 1
        x3 -= 90
        col_cletca_3 += 1
        cletcas_3.append(cletca_3)


def add_cletca_4():
    global cletcas_4, color_cletca_4, x4, col_cletca_4
    if color_cletca_4 == 1 and col_cletca_4 != 10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360, [0, 200, 255])
        color_cletca_4 += 1
        x4 -= 90
        col_cletca_4 += 1
        cletcas_4.append(cletca_4)
    if color_cletca_4 == 2 and col_cletca_4 != 10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360, [0, 255, 255])
        color_cletca_4 -= 1
        x4 -= 90
        col_cletca_4 += 1
        cletcas_4.append(cletca_4)


def add_cletca_5():
    global cletcas_5, color_cletca_5, x5, col_cletca_5
    if color_cletca_5 == 1 and col_cletca_5 != 10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450, [0, 200, 255])
        color_cletca_5 += 1
        x5 -= 90
        col_cletca_5 += 1
        cletcas_5.append(cletca_5)
    if color_cletca_5 == 2 and col_cletca_5 != 10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450, [0, 255, 255])
        color_cletca_5 -= 1
        x5 -= 90
        col_cletca_5 += 1
        cletcas_5.append(cletca_5)


add_cletca_1()
add_cletca_2()
add_cletca_3()
add_cletca_4()
add_cletca_5()


def dvigenie_zomby():
    global zomby_1, zomby_2
    if zomby_1 is not None and pologenie_1 != 'poedanie':
        zomby_1.obect_zomby.x -= 1
    if zomby_2 is not None and pologenie_2 == 'dvigenie':
        zomby_2.obect_zomby.x -= 1
    if zomby_3 is not None and pologenie_3 == 'dvigenie':
        zomby_3.obect_zomby.x -= 1
    if zomby_4 is not None and pologenie_4 == 'dvigenie':
        zomby_4.obect_zomby.x -= 1
    if zomby_5 is not None and pologenie_5 == 'dvigenie':
        zomby_5.obect_zomby.x -= 1
    if zomby_6 is not None and pologenie_6 == 'dvigenie':
        zomby_6.obect_zomby.x -= 1
    if zomby_7 is not None and pologenie_7 == 'dvigenie':
        zomby_7.obect_zomby.x -= 1


def add_zombi_2():
    global zomby_2, zombys_2
    zomby_2 = zomby.vrag_zomby(1100, 180)
    zombys_2.append(zomby_2)


def add_zombi_3():
    global zomby_3, zombys_3
    zomby_3 = zomby.vrag_zomby(1100, 270)
    zombys_3.append(zomby_3)


def add_zombi_4():
    global zomby_4, zombys_4
    zomby_4 = zomby.vrag_zomby(1100, 360)
    zombys_4.append(zomby_4)


def add_zombi_5():
    global zomby_5, zombys_5
    zomby_5 = zomby.vrag_zomby(1100, 450)
    zombys_5.append(zomby_5)


def add_zombi_6():
    global zomby_6, zombys_6
    zomby_6 = zomby.vrag_zomby(1100, random.choice([90, 180, 270, 360, 450]))
    zombys_6.append(zomby_6)


def add_zombi_7():
    global zomby_7, zombys_7
    zomby_7 = zomby.vrag_zomby(1100, random.choice([90, 180, 270, 360, 450]))
    zombys_7.append(zomby_7)


def add_rasteniy_1():
    global goroho_strel1, goroho_strels
    goroho_strel1 = goroho_strel.Rastenie_goroh(170, 120)
    goroho_strels.append(goroho_strel1)
    goroho_strel1 = goroho_strel.Rastenie_goroh(170, 210)
    goroho_strels.append(goroho_strel1)
    goroho_strel1 = goroho_strel.Rastenie_goroh(170, 300)
    goroho_strels.append(goroho_strel1)
    goroho_strel1 = goroho_strel.Rastenie_goroh(170, 390)
    goroho_strels.append(goroho_strel1)
    goroho_strel1 = goroho_strel.Rastenie_goroh(170, 480)
    goroho_strels.append(goroho_strel1)


add_rasteniy_1()


def groho_strel_vistrel():
    global goroho_strel_vistrel, goroho_strel_vistrels
    for goroho_strel1 in goroho_strels:
        goroho_strel_vistrel = goroho_strel.Rastenie_goroh(goroho_strel1.x, goroho_strel1.y)
        goroho_strel_vistrels.append(goroho_strel_vistrel)


def dvigenie_vistrel():
    global goroho_strel_vistrels
    vistrel = len(goroho_strel_vistrels)
    if vistrel >= 1:
        for goroho_strel_vistrel in goroho_strel_vistrels:
            goroho_strel_vistrel.obect_vistrel.x += 3


def popodaniy_vistrel():
    a = len(goroho_strel_vistrels)
    if a >= 1:
        for goroho_strel_vistrel in goroho_strel_vistrels:
            if zomby_1 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_1.obect_zomby):
                    zomby_1.heal = zomby_1.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)

            if zomby_2 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_2.obect_zomby):
                    zomby_2.heal = zomby_2.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)
            if zomby_3 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_3.obect_zomby):
                    zomby_3.heal = zomby_3.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)

            if zomby_4 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_4.obect_zomby):
                    zomby_4.heal = zomby_4.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)
            if zomby_5 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_5.obect_zomby):
                    zomby_5.heal = zomby_5.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)

            if zomby_6 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_6.obect_zomby):
                    zomby_6.heal -= goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)

            if zomby_7 is not None:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_7.obect_zomby):
                    zomby_7.heal -= goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)






def uron_rasteniu():

    for goroho_strel in goroho_strels:
        if goroho_strel.colliderect(zomby_1.obect_zomby):
            goroho_strel1.heal-=zomby_1.damag




def del_zomby():
    global zomby_1, zomby_2, zomby_3, zomby_4, zomby_5, zomby_6, zomby_7
    if zomby_1 is not None:
        if zomby_1.heal <= 0:
            zomby_1 = None
    if zomby_2 is not None:
        if zomby_2.heal <= 0:
            zomby_2 = None
    if zomby_3 is not None:
        if zomby_3.heal <= 0:
            zomby_3 = None
    if zomby_4 is not None:
        if zomby_4.heal <= 0:
            zomby_4 = None
    if zomby_5 is not None:
        if zomby_5.heal <= 0:
            zomby_5 = None
    if zomby_6 is not None:
        if zomby_6.heal <= 0:
            zomby_6 = None
    if zomby_7 is not None:
        if zomby_7.heal <= 0:
            zomby_7 = None


def step():
    popodaniy_vistrel()

    del_zomby()
