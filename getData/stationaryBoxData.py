def run(screen):
    if screen == 'debug':
        return [{
            'x': 'r', # 'r' for right anchor
            'y': 0,
            'border': [1, (255, 0, 255)], # Border width (0 = no border), color
            'color': (0, 0, 0),
            'height': 't',
            'width': 't', # 't' stands for text, overrite
            'textInside': ['Tabcdefghijklmnopqrstuvwxyz', (255, 255, 255), 1] # Text, color, padding (length text to border)
        }]