# 3-mal osztva 0 maradékot adó feladatok

def feladat3(lista):
    print("3) Hány lány tanul az osztályban?")
    result = 0
    for i in lista:
        if i.nem == 'L':
            result+=1
    print(result)

def feladat6(lista):
    print("6) Hány olyan diák van, akiknek több mint 2 testvére van?")
    result = 0
    for i in lista:
        if i.testverszama > 2:
            result+=1
    print(result)

def feladat9(lista):
    print("9) Gyűjtse ki azon fiú diákok nevét, akik a 2. idegen nyelvként a németet tanulják!")
    for i in lista:
        if i.nem == 'F' and i.mnyelv == 'német':
            print(i.nev)
    
def feladat12(lista):
    print("12) Hány diák tanul, az alfa matematika csoportban?")
    result = 0
    for i in lista:
        if i.micsop == 'alfa':
            result+=1
    print(result)

def feladat15(lista):
    print("15) Hány lány diák tanul, a beta matematika csoportban?")
    result = 0
    for i in lista:
        if i.micsop == 'beta' and i.nem == 'L':
            result+=1
    print(result)

def feladat18(lista):
    print("18) Van-e olyan diák, aki a 2. idegen nyelvként oroszt tanul?")
    result = False
    for i in lista:
        if i.mnyelv == 'orosz':
            result = True
            break
    print(result)

def feladat21(lista):
    print("21) Mekkora a legnagyobb család az osztályban?")
    result = lista[0].egyuttlakok
    for i in lista:
        if result < i.egyuttlakok:
            result = i.egyuttlakok
    print(result)

def feladat24(lista):
    print("24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak és 0 vagy 2 testvérük van!")
    for i in lista:
        if i.nem == 'F' and (i.acsop[0] == '3' or i.acsop[0] == '4') and (i.testverszama == 0 or i.testverszama == 2):
            print(i.nev)

def feladat27(lista):
    print("27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
    result = ""
    for i in lista:
        if i.nev == 'Avon Mór':
            result = i.acsop[0]
            break

    for i in lista:
        if i.acsop[0] == result and i.nev != 'Avon Mór':
            print(i.nev)

def feladat30(lista):
    print("30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
    result = ""
    for i in lista:
        if i.nev == 'Hát Izsák':
            result = i.acsop[0]
            break

    for i in lista:
        if i.acsop[0] == result and i.nev != 'Hát Izsák':
            print(i.nev)