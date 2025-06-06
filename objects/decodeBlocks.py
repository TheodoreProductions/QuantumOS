def decodeBlocks(blockList, b, p):
    rectlist = []
    for block in blockList:
        x = block[1]
        y = block[2]
        if block[0] == 'grass':
            rectlist.append([x * b, y * b, b, b, (2, 102, 29)])
        else:
            rectlist.append([x * b, y * b, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x * b + b // 2, y * b, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x * b, y * b + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x * b + b // 2, y * b + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist

def decodeText(textlist, p, c):
    rectlist = []
    for text in textlist:
        x = text[1]
        y = text[2]
        if text[0] == 'A':
            rectlist.append([x * p + 2 * p, y * p, p, p, c])
            rectlist.append([x * p + p, y * p + p, p, p, c])
            rectlist.append([x * p + 3 * p, y * p + p, p, p, c])
            rectlist.append([x * p, y * p + 2 * p, p, 5 * p, c])
            rectlist.append([x * p + 4 * p, y * p + 2 * p, p, 5 * p, c])
            rectlist.append([x * p + p, y * p + 3 * p, 3 * p, p, c])
        elif text[0] == 'B':
            rectlist.append([x * p, y * p, p, 7 * p, c])
            rectlist.append([x * p, y * p, 4 * p, p, c])
            rectlist.append([x * p, y * p + 3 * p, 4 * p, p, c])
            rectlist.append([x * p, y * p + 6 * p, 4 * p, p, c])
            rectlist.append([x * p + 4 * p, y * p + p, p, 2 * p, c])
            rectlist.append([x * p + 4 * p, y * p + 4 * p, p, 2 * p, c])
        elif text[0] == '0':
            rectlist.append([x * p + p, y * p, 3 * p, p, c])
            rectlist.append([x * p + p, y * p + 6 * p, 3 * p, p, c])
            rectlist.append([x * p, y * p + p, p, 5 * p, c])
            rectlist.append([x * p + 4 * p, y * p + p, p, 5 * p, c])
            rectlist.append([x * p + 3 * p, y * p + 2 * p, p, p, c])
            rectlist.append([x * p + 2 * p, y * p + 3 * p, p, p, c])
            rectlist.append([x * p + 1 * p, y * p + 4 * p, p, p, c])
        elif text[0] == '1':
            rectlist.append([x * p + p, y * p, 2 * p, p, c])
            rectlist.append([x * p + p, y * p + 6 * p, 3 * p, p, c])
            rectlist.append([x * p + 2 * p, y * p + p, p, 5 * p, c])
        elif text[0] == '2':
            rectlist.append([x * p, y * p, 3 * p, p, c])
            rectlist.append([x * p + 3 * p, y * p + p, p, p, c])
            rectlist.append([x * p + 4 * p, y * p + 2 * p, p, 2 * p, c])
            rectlist.append([x * p + 3 * p, y * p + 4 * p, p, p, c])
            rectlist.append([x * p + 2 * p, y * p + 5 * p, p, p, c])
            rectlist.append([x * p, y * p + 6 * p, 5 * p, p, c])
        elif text[0] == '3':
            rectlist.append([x * p, y * p, 4 * p, p, c])
            rectlist.append([x * p, y * p + 3 * p, 4 * p, p, c])
            rectlist.append([x * p, y * p + 6 * p, 4 * p, p, c])
            rectlist.append([x * p + 4 * p, y * p + p, p, 2 * p, c])
            rectlist.append([x * p + 4 * p, y * p + 4 * p, p, 2 * p, c])
        elif text[0] == '4':
            rectlist.append([x * p, y * p, p, 4 * p, c])
            rectlist.append([x * p + p, y * p + 3 * p, 3 * p, p, c])
            rectlist.append([x * p + 4 * p, y * p, p, 7 * p, c])
        else:
            rectlist.append([x * p, y * p, 3 * p, 4 * p, (0, 0, 0)])
            rectlist.append([x * p + 3 * p, y * p, 2 * p, 4 * p, (255, 0, 255)])
            rectlist.append([x * p, y * p + 4 * p, 3 * p, 3 * p, (255, 0, 255)])
            rectlist.append([x * p + 3 * p, y * p + 4 * p, 2 * p, 3 * p, (0, 0, 0)])
    return rectlist