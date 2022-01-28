from main import Tanulo

def feladat1(lista):
    print("1) Hány diák tanul az osztályban?")
    print(len(lista))
    print()

def feladat4(lista):
    print("4) Hány olyan diák van, akiknek több mint 1 testvére van!")
    mennyi = 0
    for sor in lista:
        if int(sor.testverszama) > 1:
            mennyi += 1 
    print(mennyi)        
    print()

def feladat7(lista):
    print("7) Gyűjtse ki azon diákok nevét, akiknek több mint 2 testvérük van!")
    vissza = []
    for sor in lista:
        if int(sor.testverszama) > 2:
            vissza.append(sor.nev)
            print(sor.nev)

def feladat10(lista):
    print("10) Hány diák tanul, az egyes angol csoportban?")



feladat1(Tanulo.lista)
feladat4(Tanulo.lista)
feladat7(Tanulo.lista)
feladat10(Tanulo.lista)