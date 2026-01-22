def run(screen):
    if screen == 'debug':
        return [{
            'text': [['This is some stationary text.', (0, 155, 0)]],
            'x': 1,
            'y': 88,
            'size': 1
        }, {
            'text': [['Some X centered text', (0, 155, 0)]],
            'x': 'mid', 
            'y': 1, 
            'size': 1
        }]
    else:
        return [{
            'text': [['E0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }]