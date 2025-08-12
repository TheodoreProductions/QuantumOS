def run(blockList, b, p):
    rectlist = []
    for i in range(len(blockList) // 2):
        x = (i % 16) * b
        y = (i // 16) * b
        block = blockList[i * 2] + blockList[i * 2 + 1]
        if block == '00':
            a = 0
        elif block == '01':
            rectlist.append([x, y, b, b, (2, 102, 29)])
        else:
            rectlist.append([x, y, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x + b // 2, y, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x, y + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x + b // 2, y + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist