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
zomby_vrag = None

zombys = []
goroho_strel1 = None
goroho_strels = []
goroho_strel_vistrel = None
goroho_strel_vistrels = []

pologenie = 'dvigenie'

x=1050





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


def add_zomby():
    global zomby_vrag
    zomby_vrag=zomby.vrag_zomby(1050,random.choice([90,180,270,360,450]))
    zombys.append(zomby_vrag)

def dvigenie_zomby():
    global zomby_vrag,x
    if zomby_vrag is not None and pologenie != 'poedanie':
        x-=0.3
        for zomby_1 in zombys:
            zomby_1.obect_zomby.x = x







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


def uron_rasteniy():
    global pologenie_1
    for goroho_strel in goroho_strels:
        for zomby_1 in zombys:
            if goroho_strel.obet_rasteniy.colliderect(zomby_vrag.obect_1):
                goroho_strel.heal-=zomby_1.damag
                print(goroho_strel.heal)
                pologenie_1 = 'poedanie'


def popodaniy_vistrel():
    a = len(goroho_strel_vistrels)
    if a >= 1:
        for goroho_strel_vistrel in goroho_strel_vistrels:
            for zomby_1 in zombys:
                if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_1.obect_zomby):
                    zomby_1.heal = zomby_1.heal - goroho_strel_vistrel.damag
                    goroho_strel_vistrels.remove(goroho_strel_vistrel)

def del_zomby():
    for zomby_1 in zombys:
        if zomby_1.heal <= 0:
            zombys.remove(zomby_1)




def step():
    popodaniy_vistrel()

    del_zomby()
