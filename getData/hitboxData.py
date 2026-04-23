def run(screen):
    hitboxes = []

    if screen == 'debug':
        hitboxes = appendLists(hitboxes, [{
            'x': 0,
            'y': 7,
            'w': 1,
            'h': 1
        }])
    else:
        # hitboxes = appendLists(hitboxes, [])
        a = 0

    return hitboxes

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1