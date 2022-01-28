from main import Tanulo


def feladat2(lista):
    print('Hány fiú tanul az osztályban?')
    fiukszama = 0
    for t in Tanulo.lista:
        if t.nem == 'F':
            fiukszama+=1
    print(fiukszama)








print(len(Tanulo.lista))

feladat2(Tanulo.lista)



