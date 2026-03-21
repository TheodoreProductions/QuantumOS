def run(screen):
    if screen == 'debug':
        return [{
            'x': 'r', # 'r' for right anchor
            'y': 0,
            'border': [1, (100, 100, 100)], # Border width (0 = no border), color
            'color': (0, 0, 0),
            'height': 't',
            'width': 't', # 't' stands for text, overrite
            'textInside': ['Area ' + str(screen), (255, 255, 255), 1] # Text, color, padding (length text to border)
        }, {
            'x': 'c', # 'r' for right anchor
            'y': 'c',
            'border': [1, (100, 100, 100)], # Border width (0 = no border), color
            'color': (0, 0, 0),
            'height': 't',
            'width': 't', # 't' stands for text, overrite
            'textInside': ['test cdnterers', (255, 255, 255), 1] # Text, color, padding (length text to border)
        }]