def run(x, y, p):
    rectlist = []
    c = (0, 0, 0)

    rectlist.append([x + p, y, 3 * p, p, c])
    rectlist.append([x, y + p, p, 3 * p, c])
    rectlist.append([x + 4 * p, y + p, p, 3 * p, c])
    rectlist.append([x + p, y + 4 * p, 3 * p, p, c])
    rectlist.append([x + 2 * p, y + 4 * p, p, 8 * p, c])
    rectlist.append([x + p, y + 8 * p, 3 * p, p, c])
    rectlist.append([x, y + 7 * p, p, p, c])
    rectlist.append([x + 4 * p, y + 7 * p, p, p, c])
    rectlist.append([x + p, y + 12 * p, p, p, c])
    rectlist.append([x, y + 13 * p, p, p, c])
    rectlist.append([x + 3 * p, y + 12 * p, p, p, c])
    rectlist.append([x + 4 * p, y + 13 * p, p, p, c])

    return rectlist