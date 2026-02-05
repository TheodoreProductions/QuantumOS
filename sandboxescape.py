import pygame
import sys

from decode import decodeBlocks
from decode import decodeText
from decode import decodeHitboxes
from decode import decodePlayer
from decode import decodeBoxes

from getData import blockData
from getData import hitboxData
from getData import textData
from getData import stationaryTextData
from getData import stationaryBoxData

def version():
    # major.medium.minor.bugfix (Diden't add anything)
    # Can have m/m/m and bugfix at same time
    # Dont need to increment m/m/m/b when the ending number changes
    version = '0.0.0.0 000002' # +1 every git commit even when not this file is changed
    # Remember to add full version to git commit

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
                text_colors.append(c[0]) # Make a list of colors, 1 per character

        text_x = t['x']
        text_y = t['y']
        text_size = t['size']
        for i in range(len(text_string)):
            current_color = text_colors[i]

            if i != 0:
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
                if text_x == 'mid': # If either values are 'mid', calculate
                    text_x = (256 - findLengthOfText(text_string)) / 2
                if text_y == 'mid':
                    text_y = (256 - findLengthOfText(text_string)) / 2

                if text_x == '-': # Going to negetive coordinates
                    text_x = 1
                if text_y == '-':
                    text_y = 1

                if text_x == '+': # Going to positive coordinates
                    text_x = 256 - findLengthOfText(text_string)
                if text_y == '+':
                    text_y = 256 - findLengthOfText(text_string)
                
                textCode.append([text_string[i], text_x + spaceDelay, text_y + verticalDelay, current_color, text_size])

            spaceDelay += 6

    rectList = decodeText.run(textCode, p)
    rectList = turnBlocksIntoPygameRects(rectList)
    return rectList

def findLengthOfText(textList): # The 'text' attribute in getData Text files
    totalLength = 0

    for text in textList:
        for t in text:
            if t in [' ', 'i', 'j', 'l', '.', '!', '|', ':', "'"]:
                totalLength += 1
            elif t in [',', '(', ')', '[', ']', ';']:
                totalLength += 2
            elif t in ['c', 'r', 't', 'z', '{', '-', '}', '=', '+', '<', '>', '"', '1', 'f']:
                totalLength += 3
            elif t in ['b', 'd', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 's', 'u', 'y', '?', '_', '&', '/', '\\', 'q']:
                totalLength += 4
            elif t == '%':
                totalLength += 7
            else:
                totalLength += 5
            
            totalLength += 1

    return totalLength

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

    # Screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(fullName)

    # Screen num
    screenNum = 'debug'

    # debug = debug
    # A = area A

    # Start settings
    update = True
    debug = True
    printDebugText = False
    showHitboxes = False
    showPlayer = True

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        # Detect keys
        keys = pygame.key.get_pressed()
            
        if update:

            # --------------------------
            # ----- Moving objects -----
            # --------------------------

            # Blocks
            blocks = blockData.run(screenNum)
            
            blocks = decodeBlocks.run(blocks, 64, 4)
            blocks = turnBlocksIntoPygameRects(blocks)

            # Hitboxes
            hitboxes = hitboxData.run(screenNum)
            
            if showHitboxes:
                hitboxes = decodeHitboxes.run(barriers, 64, 4)
                hitboxes = turnBlocksIntoPygameRects(hitboxes)
            else:
                hitboxes = []

            # Text
            text = textData.run(screenNum)            

            text = convertStringIntoPygameRects(text, 1, 1, 4)

            # Combine them all
            movingRects = addLists([blocks, text, hitboxes])

            # ------------------------------
            # ----- Stationary objects -----
            # ------------------------------

            # Define player
            x = (width - 20) / 2
            y = (height - 60) / 2
            player = decodePlayer.run(x, y, 4)
            player = turnBlocksIntoPygameRects(player)

            # Text
            stationaryText = stationaryTextData.run(screenNum)            

            stationaryText = convertStringIntoPygameRects(stationaryText, 1, 1, 4)

            # Stationary boxes
            stationaryBoxes = stationaryBoxData.run(screenNum)
            
            stationaryBoxes = decodeBoxes.run(stationaryBoxes, 4)
            stationaryBoxes = turnBlocksIntoPygameRects(stationaryBoxes)

            # Combine them all
            stationaryRects = addLists([stationaryText])
            if showPlayer:
                stationaryRects = addLists([stationaryRects, player, stationaryBoxes])
            
            # Initialize player settings
            xVelocity = 0
            yVelocity = 0
            speed = 6
            frictionSpeed = 3

            # Update update
            update = False

        # --------------------------
        # ----- Quit Detection -----
        # --------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('\n\nThank you for using an TheodoreProductions™ project. We hope to see you again!\n\n')

        # --------------------
        # ----- Movement -----
        # --------------------

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
        limit = 1024
        nLimit = int('-' + str(limit))
        for rect in movingRects:
            actualRects += 1
            if rect[0].x < nLimit or rect[0].x > width or rect[0].y < nLimit or rect[0].y > limit:
                continue
            pygame.draw.rect(screen, rect[1], rect[0])
            drawnRects += 1
        for rect in stationaryRects:
            actualRects += 1
            if rect[0].x < nLimit or rect[0].x > limit or rect[0].y < nLimit or rect[0].y > limit:
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