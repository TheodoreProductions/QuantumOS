def run(screen, x, y):
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
    
    for hitbox in hitboxes:
        hitbox['x'] += x
        hitbox['y'] += y

    return hitboxes

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1