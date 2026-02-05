def run(screen):
    if screen == 'debug':
        return [{
            'x': 0,
            'y': 0,
            'border': [1, (255, 0, 255)], # Border width (0 = no border), color
            'color': (0, 0, 0),
            'height': 42,
            'width': 96, # 't' stands for text, overrite
            'textInside': ['', (0, 0, 0), 0] # Text, color, padding (length text to border)
        }]