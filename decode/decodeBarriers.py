def run(barrierList, b, p):
    rectlist = []
    for i in range(len(barrierList)):
        x = (i % 16) * b
        y = (i // 16) * b

        r = (255, 0, 0)

        if barrierList[i] == '1':
            rectlist.append([x + 3 * p, y + p, 10 * p, 2 * p, r])
            rectlist.append([x + 2 * p, y + 2 * p, p, 12 * p, r])
            rectlist.append([x + 13 * p, y + 2 * p, p, 12 * p, r])
            rectlist.append([x + p, y + 3 * p, p, 10 * p, r])
            rectlist.append([x + 3 * p, y + 3 * p, p, p, r])
            rectlist.append([x + 11 * p, y + 3 * p, 2 * p, 2 * p, r])
            rectlist.append([x + 14 * p, y + 3 * p, p, 10 * p, r])
            rectlist.append([x + 10 * p, y + 4 * p, p, p, r])
            rectlist.append([x + 9 * p, y + 5 * p, 2 * p, 2 * p, r])
            rectlist.append([x + 11 * p, y + 5 * p, p, p, r])
            rectlist.append([x + 8 * p, y + 6 * p, p, p, r])
            rectlist.append([x + 7 * p, y + 7 * p, 2 * p, 2 * p, r])
            rectlist.append([x + 9 * p, y + 7 * p, p, p, r])
            rectlist.append([x + 6 * p, y + 8 * p, p, p, r])
            rectlist.append([x + 5 * p, y + 9 * p, 2 * p, 2 * p, r])
            rectlist.append([x + 7 * p, y + 9 * p, p, p, r])
            rectlist.append([x + 4 * p, y + 10 * p, p, p, r])
            rectlist.append([x + 3 * p, y + 11 * p, 3 * p, p, r])
            rectlist.append([x + 3 * p, y + 12 * p, 2 * p, p, r])
            rectlist.append([x + 12 * p, y + 12 * p, p, p, r])
            rectlist.append([x + 3 * p, y + 13 * p, 10 * p, 2 * p, r])
    return rectlist