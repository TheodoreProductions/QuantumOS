def run(blockList, b, p):
    rectlist = []
    for block in blockList:
        x = block['x'] * b
        y = block['y'] * b
        text_string = block['text']
        if 1==2:
            a=23241312
        else:
            rectlist.append([x, y, b // 2, b // 2, (0, 0, 0)])
            rectlist.append([x + b // 2, y, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x, y + b // 2, b // 2, b // 2, (255, 0, 255)])
            rectlist.append([x + b // 2, y + b // 2, b // 2, b // 2, (0, 0, 0)])
    return rectlist
