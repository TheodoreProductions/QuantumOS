def run(borderList, b, p):
    rectlist = []
    for border in borderList:
        x = border[1] * b
        y = border[2] * b
        c = border[3]
        if border[0] == 'n':
            rectlist.append([x, y, b, p, c])
        elif border[0] == 'e':
            rectlist.append([x + b - p, y, p, b, c])
        elif border[0] == 's':
            rectlist.append([x, y + b - p, b, p, c])
        elif border[0] == 'w':
            rectlist.append([x, y, p, b, c])
        elif border[0] == '1':
            rectlist.append([x, y, p, p, c])
        elif border[0] == '2':
            rectlist.append([x + b - p, y, p, p, c])
        elif border[0] == '3':
            rectlist.append([x, y + b - p, p, p, c])
        elif border[0] == '4':
            rectlist.append([x + b - p, y + b - p, p, p, c])
        else:
            rectlist.append([x, y, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x + b // 2, y, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x, y + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x + b // 2, y + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist