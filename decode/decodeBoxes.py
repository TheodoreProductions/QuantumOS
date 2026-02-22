def run(boxList, p):
    rectList = []
    textData = []

    for box in boxList:
        x = box['x']
        y = box['y'] * p

        c = box['color']

        w = box['width']
        h = box['height']

        bw = box['border'][0] * p
        bc = box['border'][1]

        t = box['textInside'][0]
        tc = box['textInside'][1]
        rtp = box['textInside'][2] # Raw text padding, don't multiply by p
        tp = box['textInside'][2] * p

        if w == 't':
            w = findLengthOfText(t) * p + 2 * tp + p
            # You have to add 1 once because findLengthOfText adds 1 once already
        else:
            w = w * p
        if h == 't':
            h = findHeightOfText(t) * p + 2 * tp + p
        else:
            h = h * p

        if x == 'r': # Right anchor
            x = 1024 - w
        else:
            x = x * p

        textData.append({
            'text': [[t, tc]],
            'x': x + rtp + 1,
            'y': y + rtp + 1,
            'size': 1
        })

        print(x)

        # AAAAA
        # BCCCD
        # BCCCD
        # BCCCD
        # EEEEE

        rectList.append([x, y, w, bw, bc]) # A
        rectList.append([x, y, bw, h, bc]) # B
        rectList.append([x + bw, y + bw, w - 2 * bw, h - 2 * bw, c]) # C
        rectList.append([x + w - bw, y, bw, h, bc]) # D
        rectList.append([x, y + h - bw, w, bw, bc]) # E
    
    return rectList, textData

def findLengthOfText(text):
    totalLength = 0

    for t in text:
        if t in [' ', 'i', 'j', 'l', '.', '!', '|', ':', "'"]:
            totalLength += 1
        elif t in [',', '(', ')', '[', ']', ';']:
            totalLength += 2
        elif t in ['c', 'r', 't', 'z', '{', '-', '}', '=', '+', '<', '>', '"', '1', 'f']:
            totalLength += 3
        elif t in ['b', 'd', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 's', 'u', 'y', '?', '_', '&', '/', '\\', 'q']:
            totalLength += 4
        elif t == '%':
            totalLength += 7
        else:
            totalLength += 5
        
        totalLength += 1

    return totalLength

def findHeightOfText(text):
    totalHeight = 11

    for t in text:
        if t in ['\n']:
            totalHeight += 11
    
    return totalHeight