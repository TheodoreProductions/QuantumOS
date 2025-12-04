def run(textlist, p):
    rectlist = []
    index = 1
    for text in textlist:
        c = text[3]
        s = text[4]
        if index == 1:
            oldP = p
            oldS = s
            p = p * s
        if s != oldS:
            oldS = s
            p = oldP * s
        x = text[1] * p
        y = text[2] * p
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
        elif text[0] == 'E':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 3 * p, 5 * p, p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
        elif text[0] == 'F':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 3 * p, 5 * p, p, c])
        elif text[0] == 'G':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
            rectlist.append([x + 4 * p, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + 3 * p, y + 3 * p, 2 * p, p, c])
        elif text[0] == 'H':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + 4 * p, y, p, 7 * p, c])
            rectlist.append([x, y + 3 * p, 5 * p, p, c])
        elif text[0] == 'I':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x + 2 * p, y, p, 7 * p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
        elif text[0] == 'J':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x + 2 * p, y, p, 6 * p, c])
            rectlist.append([x, y + 5 * p, p, p, c])
            rectlist.append([x + p, y + 6 * p, p, p, c])
        elif text[0] == 'K':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 3 * p, 2 * p, p, c])
            rectlist.append([x + 4 * p, y, p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x + 2 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 4 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 6 * p, p, p, c])
        elif text[0] == 'L':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
        elif text[0] == 'M':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + p, y + p, p, p, c])
            rectlist.append([x + 2 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x + 4 * p, y, p, 7 * p, c])
        elif text[0] == 'N':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + 4 * p, y, p, 7 * p, c])
            rectlist.append([x + p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 4 * p, p, p, c])
        elif text[0] == 'O':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 5 * p, c])
        elif text[0] == 'P':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
        elif text[0] == 'Q':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + 4 * p, y + p, p, 4 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
            rectlist.append([x + 2 * p, y + 4 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 6 * p, p, p, c])
        elif text[0] == 'R':
            rectlist.append([x, y, 3 * p, p, c])
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 4 * p, 3 * p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 6 * p, p, p, c])
        elif text[0] == 'S':
            rectlist.append([x + p, y, 4 * p, p, c])
            rectlist.append([x, y + p, p, 2 * p, c])
            rectlist.append([x + p, y + 3 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x, y + 6 * p, 4 * p, p, c])
        elif text[0] == 'T':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x + 2 * p, y, p, 7 * p, c])
        elif text[0] == 'U':
            rectlist.append([x, y, p, 6 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x + 4 * p, y, p, 6 * p, c])
        elif text[0] == 'V':
            rectlist.append([x, y, p, 5 * p, c])
            rectlist.append([x + p, y + 5 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 6 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 4 * p, y, p, 5 * p, c])
        elif text[0] == 'W':
            rectlist.append([x, y, p, 6 * p, c])
            rectlist.append([x + p, y + 6 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + 3 * p, y + 6 * p, p, p, c])
            rectlist.append([x + 4 * p, y, p, 6 * p, c])
        elif text[0] == 'X':
            rectlist.append([x, y, p, 1.4 * p, c])
            rectlist.append([x + 4 * p, y, p, 1.4 * p, c])
            rectlist.append([x + p, y + 1.4 * p, p, 1.4 * p, c])
            rectlist.append([x + 3 * p, y + 1.4 * p, p, 1.4 * p, c])
            rectlist.append([x + 2 * p, y + 2.7 * p, p, 1.6 * p, c])
            rectlist.append([x + p, y + 4.2 * p, p, 1.4 * p, c])
            rectlist.append([x + 3 * p, y + 4.2 * p, p, 1.4 * p, c])
            rectlist.append([x, y + 5.6 * p, p, 1.4 * p, c])
            rectlist.append([x + 4 * p, y + 5.6 * p, p, 1.4 * p, c])
        elif text[0] == 'Y':
            rectlist.append([x, y, p, 2 * p, c])
            rectlist.append([x + p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 4 * p, y, p, 2 * p, c])
        elif text[0] == 'Z':
            rectlist.append([x, y, 5 * p, p, c])
            rectlist.append([x + 4 * p, y + p, p, p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + p, y + 4 * p, p, p, c])
            rectlist.append([x, y + 5 * p, p, p, c])
            rectlist.append([x, y + 6 * p, 5 * p, p, c])
        elif text[0] == 'a':
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 4 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 4 * p, c])
        elif text[0] == 'b':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 2 * p, 3 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 3 * p, c])
            rectlist.append([x, y + 6 * p, 3 * p, p, c])
        elif text[0] == 'c':
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
        elif text[0] == 'd':
            rectlist.append([x + 3 * p, y, p, 7 * p, c])
            rectlist.append([x + p, y + 2 * p, 3 * p, p, c])
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
        elif text[0] == 'e':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 2 * p, c])
            rectlist.append([x, y + 4 * p, 4 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
        elif text[0] == 'f':
            rectlist.append([x + 2 * p, y, p, p, c])
            rectlist.append([x + 3 * p, y + p, p, p, c])
            rectlist.append([x + p, y + p, p, 6 * p, c])
            rectlist.append([x, y + 3 * p, 3 * p, p, c])
        elif text[0] == 'g':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 6 * p, c])
            rectlist.append([x, y + 8 * p, p, p, c])
            rectlist.append([x + p, y + 9 * p, 2 * p, p, c])
        elif text[0] == 'h':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x, y + 2 * p, 3 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 4 * p, c])
        elif text[0] == 'i':
            rectlist.append([x, y, p, p, c])
            rectlist.append([x, y + 2 * p, p, 5 * p, c])
        elif text[0] == 'j':
            rectlist.append([x, y, p, p, c])
            rectlist.append([x, y + 2 * p, p, 7 * p, c])
            rectlist.append([x - p, y + 9 * p, p, p, c])
            rectlist.append([x - 2 * p, y + 8 * p, p, p, c])
        elif text[0] == 'k':
            rectlist.append([x, y, p, 7 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + p, y + 4 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 6 * p, p, p, c])
        elif text[0] == 'l':
            rectlist.append([x, y, p, 7 * p, c])
        elif text[0] == 'm':
            rectlist.append([x, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 3 * p, p, 4 * p, c])
        elif text[0] == 'n':
            rectlist.append([x, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 4 * p, c])
        elif text[0] == 'o':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
        elif text[0] == 'p':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, 3 * p, c])
            rectlist.append([x, y + 2 * p, p, 8 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
        elif text[0] == 'q':
            rectlist.append([x + p, y + 2 * p, 2 * p, p, c])
            rectlist.append([x, y + 3 * p, p, 3 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, 8 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
            rectlist.append([x + 3.5 * p, y + 8 * p, p, p, c])
            rectlist.append([x + 3.9 * p, y + 7 * p, p, p, c])
        elif text[0] == 'r':
            rectlist.append([x, y + 3 * p, p, 4 * p, c])
            rectlist.append([x + p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
        elif text[0] == 's':
            rectlist.append([x + p, y + 2 * p, 3 * p, p, c])
            rectlist.append([x, y + 3 * p, p, p, c])
            rectlist.append([x + p, y + 4 * p, 2 * p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x, y + 6 * p, 3 * p, p, c])
        elif text[0] == 't':
            rectlist.append([x, y + 2 * p, 3 * p, p, c])
            rectlist.append([x + p, y + p, p, 6 * p, c])
        elif text[0] == 'u':
            rectlist.append([x, y + 2 * p, p, 4 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, 4 * p, c])
            rectlist.append([x + p, y + 6 * p, 2 * p, p, c])
        elif text[0] == 'v':
            rectlist.append([x, y + 2 * p, p, 3 * p, c])
            rectlist.append([x + p, y + 5 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 6 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, 3 * p, c])
        elif text[0] == 'w':
            rectlist.append([x, y + 2 * p, p, 4 * p, c])
            rectlist.append([x + p, y + 6 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 4 * p, p, 2 * p, c])
            rectlist.append([x + 3 * p, y + 6 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, 4 * p, c])
        elif text[0] == 'x':
            rectlist.append([x, y + 2 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 2 * p, p, p, c])
            rectlist.append([x + p, y + 3 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 4 * p, p, p, c])
            rectlist.append([x + p, y + 5 * p, p, p, c])
            rectlist.append([x + 3 * p, y + 5 * p, p, p, c])
            rectlist.append([x, y + 6 * p, p, p, c])
            rectlist.append([x + 4 * p, y + 6 * p, p, p, c])
        elif text[0] == 'y':
            rectlist.append([x, y + 2 * p, p, 4 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, 7 * p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x, y + 8 * p, p, p, c])
            rectlist.append([x + p, y + 9 * p, 2 * p, p, c])
        elif text[0] == 'z':
            rectlist.append([x, y + 2 * p, 3 * p, p, c])
            rectlist.append([x + 2 * p, y + 2 * p, p, 2 * p, c])
            rectlist.append([x + p, y + 4 * p, p, p, c])
            rectlist.append([x, y + 5 * p, p, 2 * p, c])
            rectlist.append([x, y + 6 * p, 3 * p, p, c])
        elif text[0] == '0':
            rectlist.append([x + p, y, 3 * p, p, c])
            rectlist.append([x + p, y + 6 * p, 3 * p, p, c])
            rectlist.append([x, y + p, p, 5 * p, c])
            rectlist.append([x + 4 * p, y + p, p, 5 * p, c])
            rectlist.append([x + 3 * p, y + 2 * p, p, p, c])
            rectlist.append([x + 2 * p, y + 3 * p, p, p, c])
            rectlist.append([x + 1 * p, y + 4 * p, p, p, c])
        elif text[0] == '1':
            rectlist.append([x, y, 2 * p, p, c])
            rectlist.append([x, y + 6 * p, 3 * p, p, c])
            rectlist.append([x + p, y + p, p, 5 * p, c])
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
        elif text[0] == '.':
            rectlist.append([x, y + 6 * p, p, p, c])
        elif text[0] == ',':
            rectlist.append([x + p, y + 6 * p, p, 2 * p, c])
            rectlist.append([x, y + 7 * p, 2 * p, p, c])
        else:
            rectlist.append([x, y, 3 * p, 4 * p, c])
            rectlist.append([x + 3 * p, y, 2 * p, 4 * p, (255, 0, 255)])
            rectlist.append([x, y + 4 * p, 3 * p, 3 * p, (255, 0, 255)])
            rectlist.append([x + 3 * p, y + 4 * p, 2 * p, 3 * p, c])

        index += 1
    return rectlist