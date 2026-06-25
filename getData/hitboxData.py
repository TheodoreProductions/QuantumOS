def run(screen, x, y):
    hitboxes = []
    hitboxCoordinates = []
    currentHitboxCoordinate = {}
    # xl, xr, yt, yb in pure pixels (block * 16) 

    if screen == 'debug':
        hitboxes = appendLists(hitboxes, [{
            'x': 0,
            'y': 7,
            'w': 1,
            'h': 1
        }, {
            'x': 5,
            'y': 7,
            'w': 2,
            'h': 3
        }])
    else:
        # hitboxes = appendLists(hitboxes, [])
        a = 0
    
    for hitbox in hitboxes:
        currentHitboxCoordinate = {
            'xl': hitbox['x'] * 16,
            'xr': (hitbox['x'] + hitbox['w']) * 16,
            'yt': hitbox['y'] * 16,
            'yb': (hitbox['y'] + hitbox['h']) * 16
        }
        hitboxCoordinates.append(currentHitboxCoordinate)

    for hitbox in hitboxes:
        hitbox['x'] += x
        hitbox['y'] += y

    return hitboxes, hitboxCoordinates

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1