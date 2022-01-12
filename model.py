import cletca_dly_rasteniy,zomby,random


x1=950
x2=950
x3=950
x4=950
x5=950
color_cletca_1=2
color_cletca_2=1
color_cletca_3=2
color_cletca_4=1
color_cletca_5=2
col_cletca_1=0
col_cletca_2=0
col_cletca_3=0
col_cletca_4=0
col_cletca_5=0
cletcas_1=[]
cletcas_2=[]
cletcas_3=[]
cletcas_4=[]
cletcas_5=[]
zomby_1 = zomby.vrag_zomby(1100,random.choice([90,180,270,360,450]))
zomby_2 = zomby.vrag_zomby(1100,random.choice([90,180,270,360,450]))
zombys_1 = []
zombys_2 = []



def add_cletca_1():
    global cletcas_1,color_cletca_1,x1,col_cletca_1
    if color_cletca_1==1 and col_cletca_1!=10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90,[0,200,255])
        color_cletca_1+=1
        x1-=90
        col_cletca_1+=1
        cletcas_1.append(cletca_1)
    if color_cletca_1==2 and col_cletca_1!=10:
        cletca_1 = cletca_dly_rasteniy.cletca_rasteniy(x1, 90,[0,255,255])
        color_cletca_1-=1
        x1-=90
        col_cletca_1 += 1
        cletcas_1.append(cletca_1)


def add_cletca_2():
    global cletcas_2,color_cletca_2,x2,col_cletca_2
    if color_cletca_2==1 and col_cletca_2!=10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180,[0,200,255])
        color_cletca_2+=1
        x2-=90
        col_cletca_2+=1
        cletcas_2.append(cletca_2)
    if color_cletca_2==2 and col_cletca_2!=10:
        cletca_2 = cletca_dly_rasteniy.cletca_rasteniy(x2, 180,[0,255,255])
        color_cletca_2-=1
        x2-=90
        col_cletca_2 += 1
        cletcas_2.append(cletca_2)


def add_cletca_3():
    global cletcas_3,color_cletca_3,x3,col_cletca_3
    if color_cletca_3==1 and col_cletca_3!=10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270,[0,200,255])
        color_cletca_3+=1
        x3-=90
        col_cletca_3+=1
        cletcas_3.append(cletca_3)
    if color_cletca_3==2 and col_cletca_3!=10:
        cletca_3 = cletca_dly_rasteniy.cletca_rasteniy(x3, 270,[0,255,255])
        color_cletca_3-=1
        x3-=90
        col_cletca_3 += 1
        cletcas_3.append(cletca_3)


def add_cletca_4():
    global cletcas_4,color_cletca_4,x4,col_cletca_4
    if color_cletca_4==1 and col_cletca_4!=10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360,[0,200,255])
        color_cletca_4+=1
        x4-=90
        col_cletca_4+=1
        cletcas_4.append(cletca_4)
    if color_cletca_4==2 and col_cletca_4!=10:
        cletca_4 = cletca_dly_rasteniy.cletca_rasteniy(x4, 360,[0,255,255])
        color_cletca_4-=1
        x4-=90
        col_cletca_4 += 1
        cletcas_4.append(cletca_4)


def add_cletca_5():
    global cletcas_5,color_cletca_5,x5,col_cletca_5
    if color_cletca_5==1 and col_cletca_5!=10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450,[0,200,255])
        color_cletca_5+=1
        x5-=90
        col_cletca_5+=1
        cletcas_5.append(cletca_5)
    if color_cletca_5==2 and col_cletca_5!=10:
        cletca_5 = cletca_dly_rasteniy.cletca_rasteniy(x5, 450,[0,255,255])
        color_cletca_5-=1
        x5-=90
        col_cletca_5 += 1
        cletcas_5.append(cletca_5)
add_cletca_1()
add_cletca_2()
add_cletca_3()
add_cletca_4()
add_cletca_5()

def dvigenie_zomby():
    global zomby_1,zomby_2
    zomby_1.obect_zomby.x-=1
    zomby_2.obect_zomby.x-=1



def step():
    global zombys_1,zombys_2,zomby_1,zomby_2
    zombys_1.append(zomby_1)
    zombys_2.append(zomby_2)



