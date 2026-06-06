def run(screen, x, y):
    blocks = []

    if screen == 'debug':
        blocks = appendLists(blocks, [{
            'name': 'missingBlock',
            'x': 0,
            'y': 8
        }])
    else:
        blocks = appendLists(blocks, [{
            'name': 'error',
            'x': 0,
            'y': 0
        }])
    
    for block in blocks:
        block['x'] += x
        block['y'] += y
    
    return blocks

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1