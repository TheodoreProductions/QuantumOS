def run(barrierList, b, p):
    rectlist = []
    for barrier in barrierList:
        x = barrier[0] * b
        y = barrier[1] * b
        rectlist.append(x, y, )
    return 'sdf'