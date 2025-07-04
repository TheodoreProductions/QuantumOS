def run(blockList, b, p):
    rectlist = []
    for block in blockList:
        x = block[1] * b
        y = block[2] * b
        if block[0] == 'grass':
            rectlist.append([x, y, b, b, (2, 102, 29)])
        elif block[0] == 'grid':
            rectlist.append([x, y, b, p, (0, 0, 0)])
            rectlist.append([x, y, p, b, (0, 0, 0)])
            rectlist.append([x + b - p, y, p, b, (0, 0, 0)])
            rectlist.append([x , p + b - p, b, p, (0, 0, 0)])
        else:
            rectlist.append([x, y, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x + b // 2, y, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x, y + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x + b // 2, y + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist