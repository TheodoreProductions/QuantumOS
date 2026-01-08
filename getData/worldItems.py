def blocks(screen):
    if screen == 'debug':
        return [{
            'text': 'grass',
            'x': 0,
            'y': 5
        }]
    else:
        return [{
            'text': 'error',
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
            'text': '''A BCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789\n.,!?()[]{-}_=+@#$%^&*/\\|<>:;'"\n�\nHello, this is some test thing.\nThe quick brown fox jumps over the lazy dog.\n''',
            'x': 1,
            'y': 1,
            'color': (0, 0, 0),
            'size': 1
        }]
    else:
        return [{
            'text': 'Error 0000: screen number wrong',
            'x': 1,
            'y': 1,
            'color': (255, 0, 255),
            'size': 1
        }]
