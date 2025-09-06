# run 'source pygame-env/bin/activate'

import pygame
import sys

from decode import decodeBlocks
from decode import decodeText
from decode import decodeBarriers
from decode import decodePlayer

from getData import debugWorldItems

def version():
    version = 'develepmont (00000)'
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
        for i in range(len(t[0])):
            if t[0][i] == ' ':
                spaceDelay -= 4
            elif t[0][i] == '\n':
                verticalDelay += 8
                spaceDelay = -6
            else:
                textCode.append([t[0][i], t[1] + spaceDelay, t[2] + verticalDelay, t[3], t[4]])
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
    screenNum = 0

    # 0 = map

    # Start settings
    update = True
    debug = False
    printDebugText = False
    showBarriers = False

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        # Detect keys
        keys = pygame.key.get_pressed()

        # Detect updates
        if keys[pygame.K_1]:
            debug = True
            update = True
        if keys[pygame.K_2]:
            debug = False
            update = True
        if keys[pygame.K_3]:
            showBarriers = True
            update = True
        if keys[pygame.K_4]:
            showBarriers = False
            update = True
            
        if update:
            # ----------------------
            # -----Moving rects-----
            # ----------------------

            # Blocks
            if debug:
                blocks = debugWorldItems.blocks()
            else:
                if screenNum == 0:
                    blocks = []
                else:
                    blocks = []
            blocks = decodeBlocks.run(blocks, 64, 4)
            blocks = turnBlocksIntoPygameRects(blocks)

            # Barriers
            if debug:
                barriers = debugWorldItems.barriers()
            else:
                if screenNum == 0:
                    barriers = []
                    barrierPositions = barriers
                else:
                    barriers = []
            if showBarriers:
                barriers = decodeBarriers.run(barriers, 64, 4)
                barriers = turnBlocksIntoPygameRects(barriers)
            else:
                barriers = []

            # Text
            if debug:
                text = debugWorldItems.text()
            else:
                if screenNum == 0:
                    text = []
                else:
                    text = []
            text = convertStringIntoPygameRects(text, 1, 1, 4)

            # Combine them all
            movingRects = addLists([blocks, text, barriers])

            # --------------------------
            # -----Stationary rects-----
            # --------------------------

            # Define player
            x = 0
            y = 0
            player = decodePlayer.run(x, y, 4)
            player = turnBlocksIntoPygameRects(player)

            # Combine them all
            stationaryRects = addLists([player])

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

        print(actualRects, drawnRects)

        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()