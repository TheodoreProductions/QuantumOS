def run(boxList, p):
    rectList = []
    textData = []

    for box in boxList:
        x = box['x'] * p
        y = box['y'] * p

        c = box['color']

        w = box['width']
        h = box['height']

        bw = box['border'][0] * p
        bc = box['border'][1]

        t = box['textInside'][0]
        tc = box['textInside'][1]
        tp = box['textInside'][2] * p

        if w == 't':
            w = findLengthOfText(t) * p
        else:
            w = w * p
        if h == 't':
            h = findLengthOfText(t) * p
        else:
            h = h * p
        
        print(w, h)
    
        textData.append({
            'text': [[t, tc]],
            'x': x + tp,
            'y': y + tp,
            'size': 1
        })

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
