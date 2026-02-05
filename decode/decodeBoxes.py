def run(boxList, p):
    rectList = []
    for box in boxList:
        x = box['x'] * p
        y = box['y'] * p
        c = box['color']
        w = box['width'] * p
        h = box['height'] * p
        bw = box['border'][0] * p
        bc = box['border'][1]
        t = box['textInside'][0]
        tc = box['textInside'][1]
        tp = box['textInside'][2] * p
    
        # AAAAA
        # BCCCD
        # BCCCD
        # BCCCD
        # EEEEE

        rectList.append([x, y, w, bw, bc]) # A
        rectList.append([x, y + bw, bw, h - 2 * bw, bc]) # B
        rectList.append([x + bw, y + bw, w - 2 * bw, h - 2 * bw, c]) # C
        rectList.append([x + w - bw, y + bw, bw, h - 2 * bw, bc]) # D
        rectList.append([x, y + h - bw, w, bw, bc]) # E
    
    return rectList
