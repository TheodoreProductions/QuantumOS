def blocks(screen):
    if screen == 'debug':
        return [['grass', 0, 5]]
    else:
        return [['error', 0, 0]]

def barriers(screen):
    if screen == 'debug':
        return []
    else:
        return [0, 0]

def text(screen):
    # Text, x, y, color, size
    if screen == 'debug':
        return [['''A BCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789\n.,!?()[]{-}_=+@#$%^&*/\\|<>:;'"\n�\nHello, this is some test thing.\nThe quick brown fox jumps over the lazy dog.\n''', 1, 1, (0, 0, 0), 1]]
    else:
        return [['Error 0000: screen number wrong', 1, 1, (255, 0, 255), 1]]