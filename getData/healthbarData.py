def run(screen):
    unallowedScreens = []

    if screen in unallowedScreens:
        return []
    else:
        return [{
            'x': 0,
            'y': 0,
            'border': [1, (185, 0, 0)],
            'color': (235, 0, 0),
            'height': 0.8,
            'width': 64,
            'textInside': ['', (0, 0, 0), 0]
        }] # Use the stationary box decode for this