def blocks(screen):
    if screen == 'debug':
        return [{
            'name': 'LOLOL',
            'x': 0,
            'y': 8
        }]
    else:
        return [{
            'name': 'error',
            'x': 0,
            'y': 0
        }]

def barriers(screen):
    if screen == 'debug':
        return []
    else:
        return [{
            'x': 0,
            'y': 0
        }]

def text(screen):
    if screen == 'debug':
        return [{
            'text': [['''A BCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789\n.,!?()[]{-}_=+@#$%^&*/\\|<>:;'"\n�\nHello, this is some test thing.\nThe quick brown fox jumps over the lazy dog.\n''', (0, 0, 0)]],
            'x': 1,
            'y': 1,
            'size': 1
        }, {
            'text': [['Text\n', (0, 0, 0)], 
                     ['redtext', (255, 0, 0)], 
                     ['\nbluetext', (0, 0, 255)]],
            'x': 1,
            'y': 77,
            'size': 1
        }]
    else:
        return [{
            'text': [['Error 0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }]
