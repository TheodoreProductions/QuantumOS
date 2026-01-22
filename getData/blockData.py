def run(screen):
    if screen == 'debug':
        return [{
            'name': 'missingBlock',
            'x': 0,
            'y': 8
        }]
    else:
        return [{
            'name': 'error',
            'x': 0,
            'y': 0
        }]