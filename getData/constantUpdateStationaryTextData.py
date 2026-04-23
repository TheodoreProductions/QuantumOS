def run(screen, x, y):
    text = []

    text = appendLists(text, [{
        'text': [['X: ' + str(x) + ', Y: ' + str(y), (0, 0, 0)]],
        'x': 1,
        'y': '+',
        'size': 1
    }])
    
    return text

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1