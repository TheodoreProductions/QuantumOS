def run(screen, health):
    unallowedScreens = []

    if health < 101:
        normalHealth = health
        shieldHealth = 0
        extraShieldHealth = 0
    elif health < 201:
        normalHealth = 100
        shieldHealth = health - 100
        extraShieldHealth = 0
    else:
        normalHealth = 100
        shieldHealth = 100
        extraShieldHealth = health - 200

    extraShieldHealthMain = extraShieldHealth // 8
    extraShieldHealthExtra = extraShieldHealth % 8

    if health == 0:
        healthBorder = 0
    else:
        healthBorder = 1
    if shieldHealth == 0:
        shieldBorder = 0
    else:
        shieldBorder = 1
    if extraShieldHealthMain == 0:
        extraShieldHealthMainBorder = 0
    else:
        extraShieldHealthMainBorder = 1
    if extraShieldHealthExtra == 0:
        extraShieldHealthExtraBorder = 0
    else:
        extraShieldHealthExtraBorder = 1

    if screen in unallowedScreens:
        return []
    else:
        return [{
            'x': 0,
            'y': 0,
            'border': [healthBorder, (185, 0, 0)],
            'color': (235, 0, 0),
            'height': 't',
            'width': normalHealth,
            'textInside': ['Health: ' + str(health), (0, 0, 0), 1]
        }, {
            'x': 100,
            'y': 0,
            'border': [shieldBorder, (205, 205, 0)],
            'color': (235, 235, 0),
            'height': 't',
            'width': shieldHealth,
            'textInside': ['', (0, 0, 0), 1]
        }, {
            'x': 0,
            'y': 14,
            'border': [extraShieldHealthMainBorder, (0, 0, 185)],
            'color': (0, 0, 235),
            'height': 8,
            'width': extraShieldHealthMain,
            'textInside': ['', (0, 0, 0), 1]
        }, {
            'x': extraShieldHealthMain,
            'y': 14,
            'border': [extraShieldHealthExtraBorder, (0, 0, 235)],
            'color': (0, 0, 235),
            'height': extraShieldHealthExtra,
            'width': 1,
            'textInside': ['', (0, 0, 0), 0]
        }] # Use the stationary box decode for this