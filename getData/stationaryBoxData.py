def run(screen):
    boxes = []

    boxes = appendLists(boxes, [{
            'x': 'r', # 'r' for right anchor
            'y': 0,
            'border': [1, (100, 100, 100)], # Border width (0 = no border), color
            'color': (0, 0, 0),
            'height': 't',
            'width': 't', # 't' stands for text, overrite
            'textInside': ['Area ' + str(screen), (255, 255, 255), 1] # Text, color, padding (length text to border)
        }])

    if screen == 'debug':
        # boxes = appendLists(boxes, [])
        a = 0
    
    return boxes

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1