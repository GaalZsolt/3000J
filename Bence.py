from main import Tanulo


#függvények

def feladat1(lista):
    
















# program  

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split(";")
        t = Tanulo(int(s[0]), s[1], s[2], s[3], s[4], s[5], int(s[6]), int(s[7]))


for t in Tanulo.lista:
    print(t.nev)

print(len(Tanulo.lista))

print(feladat1(lista))

