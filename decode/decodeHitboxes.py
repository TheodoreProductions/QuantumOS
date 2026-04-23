def run(barrierList, b, p):
    rectlist = []
    for barrier in barrierList:
        x = barrier['x'] * b
        y = barrier['y'] * b
        xp = barrier['w'] * p
        yp = barrier['h'] * p
        w = barrier['w']
        h = barrier['h']

        print(x, w * b, h)

        r = (255, 0, 0)

        rectlist.append([x + 3 * xp, y + yp, 10 * xp, 2 * yp, r])
        rectlist.append([x + 2 * xp, y + 2 * yp, xp, 12 * yp, r])
        rectlist.append([x + 13 * xp, y + 2 * yp, xp, 12 * yp, r])
        rectlist.append([x + xp, y + 3 * yp, xp, 10 * yp, r])
        rectlist.append([x + 3 * xp, y + 3 * yp, xp, yp, r])
        rectlist.append([x + 11 * xp, y + 3 * yp, 2 * xp, 2 * yp, r])
        rectlist.append([x + 14 * xp, y + 3 * yp, xp, 10 * yp, r])
        rectlist.append([x + 10 * xp, y + 4 * yp, xp, yp, r])
        rectlist.append([x + 9 * xp, y + 5 * yp, 2 * xp, 2 * yp, r])
        rectlist.append([x + 11 * xp, y + 5 * yp, xp, yp, r])
        rectlist.append([x + 8 * xp, y + 6 * yp, xp, yp, r])
        rectlist.append([x + 7 * xp, y + 7 * yp, 2 * xp, 2 * yp, r])
        rectlist.append([x + 9 * xp, y + 7 * yp, xp, yp, r])
        rectlist.append([x + 6 * xp, y + 8 * yp, xp, yp, r])
        rectlist.append([x + 5 * xp, y + 9 * yp, 2 * xp, 2 * yp, r])
        rectlist.append([x + 7 * xp, y + 9 * yp, xp, yp, r])
        rectlist.append([x + 4 * xp, y + 10 * yp, xp, yp, r])
        rectlist.append([x + 3 * xp, y + 11 * yp, 3 * xp, yp, r])
        rectlist.append([x + 3 * xp, y + 12 * yp, 2 * xp, yp, r])
        rectlist.append([x + 12 * xp, y + 12 * yp, xp, yp, r])
        rectlist.append([x + 3 * xp, y + 13 * yp, 10 * xp, 2 * yp, r])

        bh = 0.5 * p * h
        bw = 0.5 * p * w
        
        rectlist.append([x, y, w * b, bh, r])
        rectlist.append([x + w * b - bw, y, bw, h * b, r])
        rectlist.append([x, y + h * b - bh, w * b, bh, r])
        rectlist.append([x, y, bw, h * b, r])

    return rectlist