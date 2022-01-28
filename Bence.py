# 3-mal osztva 2 maradékot adó feladatok

def feladat2(lista):
    print('2) Hány fiú tanul az osztályban?')
    fiukszama = 0
    for t in lista:
        if t.nem == 'F':
            fiukszama+=1
    print(fiukszama)
    print()

def feladat5(lista):
    print('5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!')
    for t in lista:
        if t.testverszama > 1:
            print(t.nev)
    print()

def feladat8(lista):
    print('8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!')
    nemetesekszama = 0
    for t in lista:
        if t.mnyelv == 'német':
            nemetesekszama+=1
    print(nemetesekszama)
    print()

def feladat11(lista):
    print('11) Hány diák tanul, a kettes angol csoportban?')
    kettesangol = 0
    for t in lista:
        if t.acsop == '2. Bán':
            kettesangol+=1
    print(kettesangol)
    print()

def feladat14(lista):
    print('14) Hány lány diák tanul, az alfa matematika csoportban?')
    lanyokszama = 0
    for t in lista:
        if t.nem == 'L' and t.micsop == 'alfa':
            lanyokszama+=1
    print(lanyokszama)
    print()

def feladat17(lista):
    print('17) Hány fiú diák tanul, a beta matematika csoportban?')
    fiukszama = 0
    for t in lista:
        if t.nem == 'F' and t.micsop == 'beta':
            fiukszama+=1
    print(fiukszama)
    print()

def feladat20(lista):
    print('20) Van-e olyan diák, aki a 2. idegen nyelvként spanyolt tanul?')
    vane = False
    i = 0
    while not vane  and i < len(lista):
        if lista[i].mnyelv == 'spanyol':
            vane = True
        i+=1
    print(vane)
    print() 

def feladat23(lista):
    print('23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!')
    for t in lista:
        if t.acsop == '2. Bán' or t.acsop == '1. Sió':
            print(t.nev)
    print()


def feladat26(lista):
    print('26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.')
    for ta in lista:
        if ta.nev == 'Dári Dóra':
            for tb in lista:
                if  tb.acsop == ta.acsop and tb.nev != 'Dári Dóra':
                    print(tb.nev)
    print()

def feladat29(lista):
    print('29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ')
    for t in lista:
        pass
