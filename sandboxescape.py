import pygame
import sys

from decode import decodeBlocks
from decode import decodeText
from decode import decodeBarriers
from decode import decodePlayer

from getData import worldItems

def version():
    # maj.med.min.bug vernum
    version = '0.0.2.0 00002'
    name = 'sandbox-escape'
    return name + ' ' + version

def doNothing():
    a = 0

def addLists(listList):
    totalList = []
    for l in listList:
        for thing in l:
            totalList.append(thing)
    return totalList

def turnBlocksIntoPygameRects(blocks):
    newBlocks = []
    for i in blocks:
        rect = pygame.Rect(i[0], i[1], i[2], i[3])
        newRect = [rect, i[4]]
        newBlocks.append(newRect)
    return newBlocks

def convertStringIntoPygameRects(text, x, y, p):
    textCode = []
    rectList = []
    for t in text:
        spaceDelay = 0
        verticalDelay = 0

        text_string = ''
        colors = [] # Temperoral
        text_colors = [] # The real one
        for tt in t['text']:
            text_string += tt[0]
            colors.append([tt[1], len(tt[0])])

        for c in colors:
            for i in range(c[1]):
                text_colors.append(c[0]) # Make a list of colors , 1 per character

        text_x = t['x']
        text_y = t['y']
        text_size = t['size']
        for i in range(len(text_string)):
            current_color = text_colors[i]

            if text_string[i - 1] in [' ', 'i', 'j', 'l', '.', '!', '|', ':', "'"]:
                spaceDelay -= 4
            elif text_string[i - 1] in [',', '(', ')', '[', ']', ';']:
                spaceDelay -= 3
            elif text_string[i - 1] in ['c', 'r', 't', 'z', '{', '-', '}', '=', '+', '<', '>', '"', '1', 'f']:
                spaceDelay -= 2
            elif text_string[i - 1] in ['b', 'd', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 's', 'u', 'y', '?', '_', '&', '/', '\\', 'q']:
                spaceDelay -= 1
            elif text_string[i - 1] == '%':
                spaceDelay += 2
            
            if text_string[i] in ['\n', ' ']: # Invisible characters
                if text_string[i] == '\n':
                    verticalDelay += 11
                    spaceDelay = -6
            else:
                textCode.append([text_string[i], text_x + spaceDelay, text_y + verticalDelay, current_color, text_size])
            spaceDelay += 6
    rectList = decodeText.run(textCode, p)
    rectList = turnBlocksIntoPygameRects(rectList)
    return rectList

def main():
    fullName = version()

    pygame.init()

    print('\n\nPlease wait, ' + fullName + ' is loading...\n\n')

    # Debug
    debug = True

    # Colors
    pureWhite = (255, 255, 255)
    pureBlack = (0, 0, 0)
    pureRed = (255, 0, 0)
    pureGreen = (0, 255, 0)
    pureBlue = (0, 0, 255)

    width, height = 1024, 1024

    inc = 0

    # Screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(fullName)

    # Screen num
    screenNum = 'debug'

    # 0 = map

    # Start settings
    update = True
    debug = True
    printDebugText = False
    showBarriers = False
    showPlayer = False

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        # Detect keys
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_1]:
        #     debug = True
        #     update = True
        # if keys[pygame.K_2]:
        #     debug = False
        #     update = True
        # if keys[pygame.K_3]:
        #     showBarriers = True
        #     update = True
        # if keys[pygame.K_4]:
        #     showBarriers = False
        #     update = True
            
        if update:
            # ----------------------
            # -----Moving rects-----
            # ----------------------

            # Blocks
            if debug:
                blocks = worldItems.blocks('debug')
            else:
                blocks = worldItems.blocks(screenNum)
            
            blocks = decodeBlocks.run(blocks, 64, 4)
            blocks = turnBlocksIntoPygameRects(blocks)

            # Barriers
            if debug:
                barriers = worldItems.barriers('debug')
            else:
                barriers = worldItems.barriers(screenNum)
            
            if showBarriers:
                barriers = decodeBarriers.run(barriers, 64, 4)
                barriers = turnBlocksIntoPygameRects(barriers)
            else:
                barriers = []

            # Text
            if debug:
                text = worldItems.text('debug')
            else:
                text = worldItems.text(screenNum)
                
            text = convertStringIntoPygameRects(text, 1, 1, 4)

            # Combine them all
            movingRects = addLists([blocks, text, barriers])

            # --------------------------
            # -----Stationary rects-----
            # --------------------------

            # Define player
            x = width // 2 - 20
            y = height // 2 - 30
            player = decodePlayer.run(x, y, 4)
            player = turnBlocksIntoPygameRects(player)

            # Combine them all
            if showPlayer:
                stationaryRects = addLists([player])
            else:
                stationaryRects = []

            # Player settings
            xVelocity = 0
            yVelocity = 0
            speed = 6
            frictionSpeed = 3

            # Update update :)
            update = False

        # ------------------------
        # -----Quit Detection-----
        # ------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('\n\nThank you for using an TheodoreProductions™ project. We hope to see you again!\n\n')

        # ------------------
        # -----Movement-----
        # ------------------

        # Movement
        if keys[pygame.K_LEFT]:
            xVelocity += speed
        elif keys[pygame.K_RIGHT]:
            xVelocity -= speed
        if xVelocity > 0:
            xVelocity -= frictionSpeed
            if xVelocity < 0:  # Prevents overshooting below zero
                xVelocity = 0
        elif xVelocity < 0:
            xVelocity += frictionSpeed
            if xVelocity > 0:  # Prevents overshooting above zero
                xVelocity = 0

        if keys[pygame.K_UP]:
            yVelocity += speed
        elif keys[pygame.K_DOWN]:
            yVelocity -= speed
        if yVelocity > 0:
            yVelocity -= frictionSpeed
            if yVelocity < 0:  # Prevents overshooting below zero
                yVelocity = 0
        elif yVelocity < 0:
            yVelocity += frictionSpeed
            if yVelocity > 0:  # Prevents overshooting above zero
                yVelocity = 0

        for rect in movingRects:
            # Apply movement
            rect[0].x += xVelocity // 10
            rect[0].y += yVelocity // 10

        actualRects = 0
        drawnRects = 0

        # Drawing
        screen.fill(pureWhite)
        limit = 64
        nLimit = int('-' + str(limit))
        for rect in movingRects:
            actualRects += 1
            if rect[0].x < nLimit or rect[0].x > width + limit or rect[0].y < nLimit or rect[0].y > height + limit:
                continue
            pygame.draw.rect(screen, rect[1], rect[0])
            drawnRects += 1
        for rect in stationaryRects:
            actualRects += 1
            if rect[0].x < nLimit or rect[0].x > width + limit or rect[0].y < nLimit or rect[0].y > height + limit:
                continue
            pygame.draw.rect(screen, rect[1], rect[0])
            drawnRects += 1

        # print(actualRects, drawnRects)

        # Update display
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()

# Normal stuff
if __name__ == "__main__":
    main()