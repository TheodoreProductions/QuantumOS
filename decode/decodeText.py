def run(textlist, p):
    rectlist = []
    for text in textlist:
        x = text[1] * p
        y = text[2] * p
        c = text[3]
        if text[0] == 'A':
            rectlist.append([x + 2 * p, y, p, p, c])
            rectlist.append([x + p, y + p, p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x, y + 2 * p, p, 5 * p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, 5 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
        elif text[0] == 'B':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y, 4 * p, p, c])
            rectlist.append([x, y + 3 * p, 4 * p, p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 2 * p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
        elif text[0] == 'C':
            rectlist.append([x + p, y, 4 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + p, y + 6 * p, 4 * p, p, c])
        elif text[0] == 'D':
            rectlist.append([x, y, 4 * p, p, c])
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 5 * p, c])
        elif text[0] == 'N':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + 4 * p, y, p, 7 * p, c])
            rectlist.append([x + p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 4 * p, p, p, c])
        elif text[0] == 'P':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
        elif text[0] == 'S':
            rectlist.append([x + p, y, 4 * p, p, c])
            rectlist.append([x, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
        elif text[0] == 'b':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
        elif text[0] == 's':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x, y + 3 * p, p, p, c])
            rectlist.append([x + p, y + 4 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 5 * p, p, p, c])
            rectlist.append([x, y + 6 * p, 2 * p, p, c])
        elif text[0] == '0':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + 4 * p, y + p, p, 5 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 1 * p, y + 4 * p, p, p, c])
        elif text[0] == '1':
            rectlist.append([x + p, y, 2 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x + 2 * p, y + p, p, 5 * p, c])
        elif text[0] == '2':
            rectlist.append([x, y, 3 * p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, 2 * p, c])
            rectlist.append([x + 3 * p, y + 4 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 5 * p, p, p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
        elif text[0] == '3':
            rectlist.append([x, y, 4 * p, p, c])
            rectlist.append([x, y + 3 * p, 4 * p, p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 2 * p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
        elif text[0] == '4':
            rectlist.append([x, y, p, 4 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y, p, 7 * p, c])
        elif text[0] == '5':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x, y + p, p, 2 * p, c])
            rectlist.append([x, y + 3 * p, 4 * p, p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
        elif text[0] == '6':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
        elif text[0] == '7':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 6 * p, c])
        elif text[0] == '8':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x, y + p, p, 2 * p, c])
            rectlist.append([x + 4 * p, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x, y + 4 * p, p, 2 * p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
        elif text[0] == '9':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 6 * p, c])
        else:
            rectlist.append([x, y, 3 * p, 4 * p, c])
            rectlist.append([x + 3 * p, y, 2 * p, 4 * p, (255, 0, 255)])
            rectlist.append([x, y + 4 * p, 3 * p, 3 * p, (255, 0, 255)])
            rectlist.append([x + 3 * p, y + 4 * p, 2 * p, 3 * p, c])
    return rectlist