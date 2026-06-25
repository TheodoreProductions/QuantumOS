def run(screen, xl, yt, xr, yb):
    text = []

    if screen == 'debug':
        text = appendLists(text, [{
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
            'text': [['+-', (0, 155, 0)]], 
            'x': '+', 
            'y': '-',
            'size': 1
        }])
    else:
        text = appendLists(text, [{
            'text': [['E0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }])
    
    text = appendLists(text, [{
        'text': [['XL: ' + str(xl) + ', YT: ' + str(yt) + ', XR: ' + str(xr) + ', YB: ' + str(yb), (0, 0, 0)]],
        'x': 1,
        'y': '+',
        'size': 1
    }])
    
    return text

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1