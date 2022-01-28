from zsolt import feladat3,feladat6,feladat9,feladat12,feladat15,feladat18,feladat21,feladat24,feladat27,feladat30
from Bence import feladat2,feladat5,feladat8,feladat11,feladat14,feladat17,feladat20,feladat23,feladat26,feladat29


class Tanulo:
    lista = []
    def __init__(self, tanulokod, nev, micsop, acsop, mnyelv, nem, egyuttlakok, testverszam):
        self.tanulokod = tanulokod
        self.nev = nev
        self.micsop = micsop
        self.acsop = acsop
        self.mnyelv = mnyelv
        self.nem = nem
        self.egyuttlakok = egyuttlakok
        self.testverszama = testverszam
        Tanulo.lista.append(self)

with open("input.txt", "r", encoding="utf8") as f:

    for sor in f:
        s = sor.strip().split(";")
        t = Tanulo(int(s[0]), s[1], s[2], s[3], s[4], s[5], int(s[6]), int(s[7]))


feladat2(Tanulo.lista)
feladat3(Tanulo.lista)
feladat5(Tanulo.lista)
feladat6(Tanulo.lista)
feladat8(Tanulo.lista)
feladat9(Tanulo.lista)
feladat11(Tanulo.lista)
feladat12(Tanulo.lista)
feladat14(Tanulo.lista)
feladat15(Tanulo.lista)
feladat17(Tanulo.lista)
feladat18(Tanulo.lista)
feladat20(Tanulo.lista)
feladat21(Tanulo.lista)
feladat23(Tanulo.lista)
feladat24(Tanulo.lista)
feladat26(Tanulo.lista)
feladat27(Tanulo.lista)
feladat30(Tanulo.lista)









