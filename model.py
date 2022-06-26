import cletca_dly_rasteniy, zomby, random, goroho_strel, pygame, pocupca,folin_sun,schet,\
Happy_sun,lazer_plant

cupleniy_towar = None
x1 = 1100
x2 = 1100
x3 = 1100
x4 = 1100
x5 = 1100
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
pologenie = 'dvigenie'
x = 1200

goroho_strels = []
goroho_strel_vistrel = None
goroho_strel_vistrels = []


bananas=[]
bananas_vistrels=[]


rect_magazin = pygame.Rect([470, 0], [450, 70])

rect_towar_brocol = pygame.Rect([480, 10], [50, 50])
rect_towar_sunflover=pygame.Rect([550,10],[50,50])
rect_towar_banana = pygame.Rect([620,10],[50,50])

home = pygame.Rect(0, 90, 180, 450)

rect_sun_tovar=pygame.Rect([400, 0], [70, 90])
sun_rects=[]
sun_rect=None

schets=[]
sun_schet = schet.schet(400, 60, 100, 'sun')
schets.append(sun_schet)

sunflovers=[]
bigsuns=[]

lapata=pygame.Rect([920,0],[70,70])

vikapovatel=None




def add_cletca_1():
    global cletcas_1, color_cletca_1, x1, col_cletca_1
    if color_cletca_1 == 1 and col_cletca_1 != 10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90, [50, 255, 50])
        color_cletca_1 += 1
        x1 -= 90
        col_cletca_1 += 1
        cletcas_1.append(cletca_1)
    if color_cletca_1 == 2 and col_cletca_1 != 10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90, [70, 255, 70])
        color_cletca_1 -= 1
        x1 -= 90
        col_cletca_1 += 1
        cletcas_1.append(cletca_1)


def add_cletca_2():
    global cletcas_2, color_cletca_2, x2, col_cletca_2
    if color_cletca_2 == 1 and col_cletca_2 != 10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180, [50, 255, 50])
        color_cletca_2 += 1
        x2 -= 90
        col_cletca_2 += 1
        cletcas_2.append(cletca_2)
    if color_cletca_2 == 2 and col_cletca_2 != 10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180, [70, 255, 70])
        color_cletca_2 -= 1
        x2 -= 90
        col_cletca_2 += 1
        cletcas_2.append(cletca_2)


def add_cletca_3():
    global cletcas_3, color_cletca_3, x3, col_cletca_3
    if color_cletca_3 == 1 and col_cletca_3 != 10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270, [50, 255, 50])
        color_cletca_3 += 1
        x3 -= 90
        col_cletca_3 += 1
        cletcas_3.append(cletca_3)
    if color_cletca_3 == 2 and col_cletca_3 != 10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270, [70, 255, 70])
        color_cletca_3 -= 1
        x3 -= 90
        col_cletca_3 += 1
        cletcas_3.append(cletca_3)


def add_cletca_4():
    global cletcas_4, color_cletca_4, x4, col_cletca_4
    if color_cletca_4 == 1 and col_cletca_4 != 10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360, [50, 255, 50])
        color_cletca_4 += 1
        x4 -= 90
        col_cletca_4 += 1
        cletcas_4.append(cletca_4)
    if color_cletca_4 == 2 and col_cletca_4 != 10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360, [70, 255, 70])
        color_cletca_4 -= 1
        x4 -= 90
        col_cletca_4 += 1
        cletcas_4.append(cletca_4)


def add_cletca_5():
    global cletcas_5, color_cletca_5, x5, col_cletca_5
    if color_cletca_5 == 1 and col_cletca_5 != 10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450, [50, 255, 50])
        color_cletca_5 += 1
        x5 -= 90
        col_cletca_5 += 1
        cletcas_5.append(cletca_5)
    if color_cletca_5 == 2 and col_cletca_5 != 10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450, [70, 255, 70])
        color_cletca_5 -= 1
        x5 -= 90
        col_cletca_5 += 1
        cletcas_5.append(cletca_5)


add_cletca_1()
add_cletca_2()
add_cletca_3()
add_cletca_4()
add_cletca_5()


def funkciy_lopati(x,y):
    if lapata.collidepoint(x,y):
        add_vikapovatel(x,y)


def add_vikapovatel(x,y):
    global vikapovatel
    vikapovatel = pygame.Rect([x, y], [70, 70])


def dvigenie_vikapovatel(x,y):
    global vikapovatel
    if vikapovatel is not None:
        vikapovatel = pygame.Rect([x, y], [70, 70])



def funkciy_vikapovatel(x,y):
    global vikapovatel
    for goroho_strel in goroho_strels:
        if goroho_strel.obet_rasteniy.collidepoint(x, y):
            osvobodi_cletcu(goroho_strel.obet_rasteniy)
            goroho_strels.remove(goroho_strel)
            vikapovatel = None

    for sunflover in sunflovers:
        if sunflover.obect_sunflover.collidepoint(x,y):
            osvobodi_cletcu(sunflover.obect_sunflover)
            sunflovers.remove(sunflover)
            vikapovatel = None
    for banana in bananas:
        if banana.obect_banana.collidepoint(x,y):
            osvobodi_cletcu(banana.obect_banana)
            bananas.remove(banana)
            vikapovatel = None


def add_zomby():
    global zomby_vrag
    speed = 1.5 / 10
    zomby_vrag = zomby.vrag_zomby(x, random.choice([90, 180, 270, 360, 450]), speed, 'dvigenie',6,1,'standart')
    zombys.append(zomby_vrag)


def add_fat_zomby():
    speed = 1.5/10
    zomby_vrag = zomby.vrag_zomby(x, random.choice([90, 180, 270, 360, 450]), speed, 'dvigenie',10,1,'fat')
    zombys.append(zomby_vrag)


def add_brone_zomby():
    zomby_vrag = zomby.vrag_zomby(x, random.choice([90, 180, 270, 360, 450]), 1, 'dvigenie',20,100,'brone')
    zombys.append(zomby_vrag)


def dvigenie_zomby():
    for zomby_1 in zombys:
        zomby_1.dvigenie()



def uron_rasteniy_sunflover():
    for zomby_1 in zombys:
        for sunflover in sunflovers:
            if zomby_1.vid=='brone'and\
                    sunflover.obect_sunflover.colliderect(zomby_1.obect_zomby):
                sunflover.heal -= zomby_1.damag
                zomby_1.pologenie = 'stop'
                zomby_1.damag=0
            elif sunflover.obect_sunflover.colliderect(zomby_1.obect_zomby):
                sunflover.heal -= zomby_1.damag
                zomby_1.pologenie = 'poedanie'
            if sunflover.heal<=0:
                osvobodi_cletcu(sunflover.obect_sunflover)
                sunflovers.remove(sunflover)
                izmenenie_pologeniy()


def uron_rasteniy_banana():
    for zomby_1 in zombys:
        for banana in bananas:
            if zomby_1.vid=='brone'and\
                    banana.obect_banana.colliderect(zomby_1.obect_zomby):
                banana.heal -= zomby_1.damag
                zomby_1.pologenie = 'stop'
                zomby_1.damag=0
            elif banana.obect_banana.colliderect(zomby_1.obect_zomby):
                banana.heal -= zomby_1.damag
                zomby_1.pologenie = 'poedanie'
            if banana.heal<=0:
                osvobodi_cletcu(banana.obect_banana)
                bananas.remove(banana)
                izmenenie_pologeniy()

def add_rasteniy_brocol(x, y):
    goroho_strel1 = goroho_strel.Rastenie_goroh(x, y)
    goroho_strels.append(goroho_strel1)








def dvigenie_vistrel():
    for goroho_strel_vistrel in goroho_strel_vistrels.copy():
        goroho_strel_vistrel.obect_vistrel.x += 3
        if goroho_strel_vistrel.obect_vistrel.x==1250:
            goroho_strel_vistrels.remove(goroho_strel_vistrel)




def uron_rasteniy_brocol():
    for goroho_strel in goroho_strels:
        for zomby_1 in zombys:
            if zomby_1.vid=='brone'and goroho_strel.obet_rasteniy.colliderect(zomby_1.obect_zomby):
                goroho_strel.heal -= zomby_1.damag
                zomby_1.pologenie = 'stop'
                zomby_1.damag=0
            elif goroho_strel.obet_rasteniy.colliderect(zomby_1.obect_zomby):
                goroho_strel.heal -= zomby_1.damag

                zomby_1.pologenie = 'poedanie'


def del_rasteniy():
    for goroho_strel in goroho_strels:
        if goroho_strel.heal <= 0:

            osvobodi_cletcu(goroho_strel.obet_rasteniy)
            goroho_strels.remove(goroho_strel)

            izmenenie_pologeniy()


def osvobodi_cletcu(obet_rasteniy):

    if obet_rasteniy.y == 90:
        for cletcas in cletcas_1:
            if cletcas.obect_cletca.colliderect(obet_rasteniy):
                cletcas.sostoynie = 'svobodno'
    elif obet_rasteniy.y == 180:
        for cletcas in cletcas_2:
            if cletcas.obect_cletca.colliderect(obet_rasteniy):
                cletcas.sostoynie = 'svobodno'
    elif obet_rasteniy.y == 270:
        for cletcas in cletcas_3:
            if cletcas.obect_cletca.colliderect(obet_rasteniy):
                cletcas.sostoynie = 'svobodno'
    elif obet_rasteniy.y == 360:
        for cletcas in cletcas_4:
            if cletcas.obect_cletca.colliderect(obet_rasteniy):
                cletcas.sostoynie = 'svobodno'
    elif obet_rasteniy.y == 450:
        for cletcas in cletcas_5:
            if cletcas.obect_cletca.colliderect(obet_rasteniy):
                cletcas.sostoynie = 'svobodno'



def izmenenie_pologeniy():
    for zomby_1 in zombys:
        if zomby_1.vid!='brone':
            zomby_1.pologenie = 'dvigenie'


def popodaniy_vistrel_brocol():
    for goroho_strel_vistrel in goroho_strel_vistrels:
        for zomby_1 in zombys:
            if goroho_strel_vistrel.obect_vistrel.colliderect(zomby_1.obect_zomby):
                zomby_1.heal = zomby_1.heal - goroho_strel_vistrel.damag
                goroho_strel_vistrels.remove(goroho_strel_vistrel)
                break


def popadanie_vistrel_banana():
    for goroho_strel_vistrel in bananas_vistrels:
        for zomby_1 in zombys:
            if goroho_strel_vistrel.obect_lazer.colliderect(zomby_1.obect_zomby):
                zomby_1.heal = zomby_1.heal - goroho_strel_vistrel.damage
        bananas_vistrels.remove(goroho_strel_vistrel)




def del_zomby():
    for zomby_1 in zombys:
        if zomby_1.heal <= 0:
            zombys.remove(zomby_1)


def porogenie():
    for zomby_1 in zombys:
        if home.colliderect(zomby_1.obect_zomby) == True:
            exit()





def pocupka_rasteniy_brocol(x, y):
    if rect_towar_brocol.collidepoint(x, y):
        if sun_schet.number_schet>=100:
            add_rect_cupleniy_towar(x, y)


def pocupka_rasteniy_sunflover(x, y):
    if rect_towar_sunflover.collidepoint(x,y):
        if sun_schet.number_schet >= 100:
            add_rect_cupleniy_towar(x, y)


def pocupka_rasteniy_banana(x,y):
    if rect_towar_banana.collidepoint(x,y) and sun_schet.number_schet>=250:
        add_rect_cupleniy_towar(x,y)







def perenos_towar(x, y):
    global cupleniy_towar
    if cupleniy_towar is not None:
        if cupleniy_towar.sostoynie == 'perenos':
            cupleniy_towar.perenos(x, y)


def postonovka_towar(x, y):
    global cupleniy_towar,sun_schet,mogno_puscat
    if cupleniy_towar is not None and cupleniy_towar.sostoynie == 'perenos' \
            and cupleniy_towar.cacoe_rastenie=='brocol':
        for cletca1 in cletcas_1:
            if cletca1.obect_cletca.collidepoint(x, y) == True and cletca1.sostoynie == 'svobodno':
                add_rasteniy_brocol(cletca1.x, cletca1.y)
                cupleniy_towar = None
                cletca1.sostoynie = 'zanyto'
                sun_schet.number_schet-=100
        for cletca2 in cletcas_2:
            if cletca2.obect_cletca.collidepoint(x, y) == True and cletca2.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca2.sostoynie = 'zanyto'
                add_rasteniy_brocol(cletca2.x, cletca2.y)
                sun_schet.number_schet -= 100
        for cletca3 in cletcas_3:
            if cletca3.obect_cletca.collidepoint(x, y) == True and cletca3.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca3.sostoynie = 'zanyto'
                add_rasteniy_brocol(cletca3.x, cletca3.y)
                sun_schet.number_schet -= 100
        for cletca4 in cletcas_4:
            if cletca4.obect_cletca.collidepoint(x, y) == True and cletca4.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca4.sostoynie = 'zanyto'
                add_rasteniy_brocol(cletca4.x, cletca4.y)
                sun_schet.number_schet -= 100
        for cletca5 in cletcas_5:
            if cletca5.obect_cletca.collidepoint(x, y) and cletca5.sostoynie == 'svobodno':
                cupleniy_towar = None
                add_rasteniy_brocol(cletca5.x, cletca5.y)
                cletca5.sostoynie = 'zanyto'
                sun_schet.number_schet -= 100

    elif cupleniy_towar is not None and cupleniy_towar.sostoynie == 'perenos' \
             and cupleniy_towar.cacoe_rastenie == 'sunflover':
        for cletca1 in cletcas_1:
            if cletca1.obect_cletca.collidepoint(x, y) == True and cletca1.sostoynie == 'svobodno':
                add_rasteniy_sunflover(cletca1.x, True, cletca1.y)
                cupleniy_towar = None
                cletca1.sostoynie = 'zanyto'
                sun_schet.number_schet -= 100
                mogno_puscat = True
        for cletca2 in cletcas_2:
            if cletca2.obect_cletca.collidepoint(x, y) == True and cletca2.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca2.sostoynie = 'zanyto'
                add_rasteniy_sunflover(cletca2.x, True, cletca2.y)
                sun_schet.number_schet -= 100
                mogno_puscat = True
        for cletca3 in cletcas_3:
            if cletca3.obect_cletca.collidepoint(x, y) == True and cletca3.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca3.sostoynie = 'zanyto'
                add_rasteniy_sunflover(cletca3.x, True, cletca3.y)
                sun_schet.number_schet -= 100
                mogno_puscat = True
        for cletca4 in cletcas_4:
            if cletca4.obect_cletca.collidepoint(x, y) == True and cletca4.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca4.sostoynie = 'zanyto'
                add_rasteniy_sunflover(cletca4.x, True, cletca4.y)
                sun_schet.number_schet -= 100

        for cletca5 in cletcas_5:
            if cletca5.obect_cletca.collidepoint(x, y) and cletca5.sostoynie == 'svobodno':
                cupleniy_towar = None
                add_rasteniy_sunflover(cletca5.x, True, cletca5.y)
                cletca5.sostoynie = 'zanyto'
                sun_schet.number_schet -= 100



    elif cupleniy_towar is not None and cupleniy_towar.sostoynie == 'perenos' \
            and cupleniy_towar.cacoe_rastenie=='banana':
        for cletca1 in cletcas_1:
            if cletca1.obect_cletca.collidepoint(x, y) == True and cletca1.sostoynie == 'svobodno':
                add_rastenie_banana(cletca1.x,cletca1.y)
                cupleniy_towar = None
                cletca1.sostoynie = 'zanyto'
                sun_schet.number_schet-=250
        for cletca2 in cletcas_2:
            if cletca2.obect_cletca.collidepoint(x, y) == True and cletca2.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca2.sostoynie = 'zanyto'
                add_rastenie_banana(cletca2.x,cletca2.y)
                sun_schet.number_schet -= 250
        for cletca3 in cletcas_3:
            if cletca3.obect_cletca.collidepoint(x, y) == True and cletca3.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca3.sostoynie = 'zanyto'
                add_rastenie_banana(cletca3.x, cletca3.y)
                sun_schet.number_schet -= 250
                mogno_puscat = True
        for cletca4 in cletcas_4:
            if cletca4.obect_cletca.collidepoint(x, y) == True and cletca4.sostoynie == 'svobodno':
                cupleniy_towar = None
                cletca4.sostoynie = 'zanyto'
                add_rastenie_banana(cletca4.x, cletca4.y)
                sun_schet.number_schet -= 250

        for cletca5 in cletcas_5:
            if cletca5.obect_cletca.collidepoint(x, y) and cletca5.sostoynie == 'svobodno':
                cupleniy_towar = None
                add_rastenie_banana(cletca5.x,cletca5.y)
                cletca5.sostoynie = 'zanyto'
                sun_schet.number_schet -= 250



def mogno_strelyt_brocol():

    for zomby in zombys:
        for goroho_strel1 in goroho_strels:
            if goroho_strel1.y == zomby.y and zomby.x<=1170:
                goroho_strel1.mogno_strelyt_rasteniu = True


def mogno_strelyt_banana():
    for zomby in zombys:
        for banana in bananas:
            if banana.y == zomby.y and zomby.x<=1170:
                banana.mogu_strelyt = True






def zapusk_vistrel_brocol(TIMER):
    for goroho_strel1 in goroho_strels:
        if goroho_strel1.mogno_strelyt_rasteniu == True and goroho_strel1.TIMER_VISTREL==TIMER:
            goroho_strel1.reg_vistrel()
            goroho_strel_vistrel = goroho_strel.Rastenie_goroh(goroho_strel1.x, goroho_strel1.y + 30)
            goroho_strel_vistrels.append(goroho_strel_vistrel)
    pygame.display.set_caption(str(len(goroho_strel_vistrels)) + ' ' + str(len(goroho_strels)))


def zapusk_vistrel_banana(TIMER):
    for banana in bananas:
        if banana.mogu_strelyt == True and banana.TIMER_VISTREL==TIMER:
            banana.reg_vistrel()
            goroho_strel_vistrel = lazer_plant.lazer_rastenie(banana.x, banana.y + 10)
            bananas_vistrels.append(goroho_strel_vistrel)

def add_sun():
    global sun_rect

    sun_rect=folin_sun.foling_sun(random.randint(300,1160) )
    sun_rects.append(sun_rect)


def dvigenie_sun():

    for sun_rect in sun_rects:
        sun_rect.fol()

        if rect_sun_tovar.contains(sun_rect.obect_sun) and sun_rect.sobrano==True:
            del_sun(sun_rect)






def sbor_sun(x=0,y=0):

    for sun_rect in sun_rects:
        if sun_rect.obect_sun.collidepoint(x,y):
            sun_rect.sbor_sun()




def del_sun(sun_rect):
    sun_rects.remove(sun_rect)
    sun_schet.number_schet+=25

def add_rect_cupleniy_towar(x, y):
    global cupleniy_towar
    if rect_towar_brocol.collidepoint(x, y):
        cupleniy_towar = pocupca.Pocupca_towara(x, y, 'brocol', 'perenos')
    if rect_towar_sunflover.collidepoint(x,y):
        cupleniy_towar = pocupca.Pocupca_towara(x, y, 'sunflover', 'perenos')
    if rect_towar_banana.collidepoint(x,y):
        cupleniy_towar = pocupca.Pocupca_towara(x,y,'banana','perenos')

def add_rasteniy_sunflover(x,a,y):
    sunflover1=Happy_sun.happy_sun(x,y,a)
    sunflovers.append(sunflover1)





def add_bigsun(TIMER):
    for sunflover in sunflovers:
        if sunflover.TIMER_ADD_BIGSUN==TIMER and sunflover.mogno_puscat==True:
            sunflover.reg_bigsun()
            bigsun=Happy_sun.happy_sun(sunflover.obect_sunflover.x+10,sunflover.obect_sunflover.y-70)
            bigsuns.append(bigsun)
            sunflover.smogno_puscat = False



def sbor_bigsuns(x,y):
    for bigsun in bigsuns:
        if bigsun.obect_bigsun.collidepoint(x,y):
            sun_schet.number_schet+=50
            bigsuns.remove(bigsun)


def add_rastenie_banana(x,y):
    banana=lazer_plant.lazer_rastenie(x,y)
    bananas.append(banana)



def step():
    popodaniy_vistrel_brocol()
    popadanie_vistrel_banana()
    uron_rasteniy_brocol()
    uron_rasteniy_sunflover()
    dvigenie_zomby()
    del_rasteniy()
    porogenie()
    mogno_strelyt_brocol()
    uron_rasteniy_banana()
    mogno_strelyt_banana()
    del_zomby()
    dvigenie_sun()
    sbor_sun()

