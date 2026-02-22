def run(screen):
    if screen == 'debug':
        return [{
            'text': [['This is some stationary text.', (0, 155, 0)]],
            'x': 1,
            'y': 89,
            'size': 1
        }, {
            'text': [['C- (XY)', (0, 155, 0)]],
            'x': 'mid', 
            'y': '-', 
            'size': 1
        }, {
            'text': [['-C', (0, 155, 0)]], 
            'x': '-', 
            'y': 'mid', 
            'size': 1
        }, {
            'text': [['CC', (0, 155, 0)]], 
            'x': 'mid', 
            'y': 'mid', 
            'size': 1
        }, {
            'text': [['C+', (0, 155, 0)]], 
            'x': 'mid', 
            'y': '+', 
            'size': 1
        }, {
            'text': [['+C', (0, 155, 0)]], 
            'x': '+', 
            'y': 'mid',
            'size': 1
        }, {
            'text': [['--', (0, 155, 0)]], 
            'x': '-', 
            'y': '-',
            'size': 1
        }, {
            'text': [['-+', (0, 155, 0)]], 
            'x': '-', 
            'y': '+',
            'size': 1
        }, {
            'text': [['+-', (0, 155, 0)]], 
            'x': '+', 
            'y': '-',
            'size': 1
        }, {
            'text': [['++', (0, 155, 0)]], 
            'x': '+', 
            'y': '+',
            'size': 1
        }]
    else:
        return [{
            'text': [['E0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }]