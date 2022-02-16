def contaTamanhoRio(x, y, mapa, listaTamanhoRios):
    if y != len(mapa[x]) - 1 and mapa[x][y+1]==1:
        mapa[x][y+1] = -1
        listaTamanhoRios[-1] += 1
        contaTamanhoRio(x, y+1, mapa, listaTamanhoRios)
    if y!=0 and mapa[x][y-1]==1:
        mapa[x][y-1] = -1
        listaTamanhoRios[-1] += 1
        contaTamanhoRio(x, y-1, mapa, listaTamanhoRios)
    if x>0 and mapa[x-1][y]==1:
        mapa[x-1][y] = -1
        listaTamanhoRios[-1] += 1
        contaTamanhoRio(x-1, y, mapa, listaTamanhoRios)
    if x<len(mapa)-1 and mapa[x+1][y]==1:
        mapa[x+1][y] = -1
        listaTamanhoRios[-1] += 1
        contaTamanhoRio(x+1, y, mapa, listaTamanhoRios)
  
def achaRio(mapa):
    listaTamanhoRios = []

    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            if mapa[x][y]==1:
                mapa[x][y] = -1
                listaTamanhoRios.append(1)
                contaTamanhoRio(x, y, mapa, listaTamanhoRios)
    return listaTamanhoRios

mapa = [
[1, 0, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 0]
]

achaRio(mapa)