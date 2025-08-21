def run(blockList, b, p):
    rectlist = []
    for block in blockList:
        x = block[1] * b
        y = block[2] * b
        name = block[0]
        if name == 'grass':
            rectlist.append([x, y, b, b, (2, 102, 29)])
        else:
            rectlist.append([x, y, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x + b // 2, y, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x, y + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x + b // 2, y + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist