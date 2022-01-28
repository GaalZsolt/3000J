from main import Tanulo

#minden harmadik feladatot oldak meg a 2.-tól kezdve
def feladat2(lista):
    print('2) Hány fiú tanul az osztályban?')
    fiukszama = 0
    for t in Tanulo.lista:
        if t.nem == 'F':
            fiukszama+=1
    print(fiukszama)

def feladat5(lista):
    print('5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!')
    for t in Tanulo.lista:
        if t.testverszama > 1:
            print(t.nev)

def feladat8(lista):
    print('8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!')
    nemetesekszama = 0
    for t in Tanulo.lista:
        if t.mnyelv == 'német':
            nemetesekszama+=1
    print(nemetesekszama)

def feladat11(lista):
    print('11) Hány diák tanul, a kettes angol csoportban?')
    kettesangol = 0
    for t in Tanulo.lista:
        if t.acsop == '2. Bán':
            kettesangol+=1
    print(kettesangol)

def feladat14(lista):
    print('14) Hány lány diák tanul, az alfa matematika csoportban?')
    lanyokszama = 0
    for t in Tanulo.lista:
        if t.nem == 'L' and t.micsop == 'alfa':
            lanyokszama+=1
    print(lanyokszama)

def feladat17(lista):
    print('17) Hány fiú diák tanul, a beta matematika csoportban?')
    fiukszama = 0
    for t in Tanulo.lista:
        if t.nem == 'F' and t.micsop == 'beta':
            fiukszama+=1
    print(fiukszama)


feladat2(Tanulo.lista)

feladat5(Tanulo.lista)

feladat8(Tanulo.lista)

feladat11(Tanulo.lista)

feladat14(Tanulo.lista)

feladat17(Tanulo.lista)







