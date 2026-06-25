import pygame
import sys

from decode import decodeBlocks
from decode import decodeText
from decode import decodeHitboxes
from decode import decodePlayer
from decode import decodeBoxes

# Moving
from getData import blockData
from getData import hitboxData
from getData import textData

# Stationary
from getData import stationaryTextData
from getData import stationaryBoxData
from getData import healthbarData

def version():
    # major.medium.minor.bugfix (Diden't add anything)
    # Can have m/m/m and bugfix at same time
    # Dont need to increment m/m/m/b when the ending number changes
    version = '0.0.0.0 000005' # +1 every git commit even when not this file is changed

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

def turnRectlistsIntoPygameRects(blocks):
    newBlocks = []
    for i in blocks:
        rect = pygame.Rect(i[0], i[1], i[2], i[3])
        newRect = [rect, i[4]]
        newBlocks.append(newRect)
    return newBlocks

def convertStringIntoPygameRectlists(text, p):
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
        textSize = t['size']
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
                    text_x = (256 - findLengthOfText(text_string, textSize)) / 2
                if text_y == 'mid':
                    text_y = (256 - findHeightOfText(text_string, textSize)) / 2

                if text_x == '-': # Going to negetive coordinates
                    text_x = 1
                if text_y == '-':
                    text_y = 1

                if text_x == '+': # Going to positive coordinates
                    text_x = 256 - findLengthOfText(text_string, textSize)
                if text_y == '+':
                    text_y = 256 - findHeightOfText(text_string, textSize)
                
                textCode.append([text_string[i], text_x + spaceDelay, text_y + verticalDelay, current_color, textSize])

            spaceDelay += 6

    rectList = decodeText.run(textCode, p)
    return rectList

def findLengthOfText(textList, textSize):
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
    
    totalLength *= textSize
    return totalLength

def findHeightOfText(textList, textSize):
    totalHeight = 1

    for text in textList:
        for t in text:
            if t == '\n':
                totalHeight += 1
    
    totalHeight *= 9
    totalHeight *= textSize
    return totalHeight

def main():
    fullName = version()

    pygame.init()

    print('\n\nPlease wait, ' + fullName + ' is loading...\n\n')

    # Debug
    debug = True

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
    showHitboxes = True
    showPlayer = True
    
    # Initialize player settings
    xVelocity = 0
    yVelocity = 0
    speed = 3
    frictionSpeed = 1
    health = 100
    x = (width - 20) / 2
    y = (height - 60) / 2
    rx = 0
    ry = 0

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        # Detect keys
        keys = pygame.key.get_pressed()
                
        # ---------------------------
        # ----- Constant update -----
        # ---------------------------

        # ------------------------------
        # ----- Stationary objects -----
        # ------------------------------

        # Healthbar
        healthbar = healthbarData.run(screenNum, health)
        healthbar, healthbarText = decodeBoxes.run(healthbar, 4)
        # healthbar = turnRectlistsIntoPygameRects(healthbar)
        healthbarText = convertStringIntoPygameRectlists(healthbarText, 4) 

        # Define player
        playerx = (width - 20) / 2
        playery = (height - 60) / 2
        player = decodePlayer.run(playerx, playery, 4)
        # player = turnRectlistsIntoPygameRects(player)

        # Text
        stationaryText = stationaryTextData.run(screenNum, x, y)            

        stationaryText = convertStringIntoPygameRectlists(stationaryText, 4)

        # Stationary boxes
        stationaryBoxes = stationaryBoxData.run(screenNum)
        
        stationaryBoxes, stationaryBoxText = decodeBoxes.run(stationaryBoxes, 4)
        # stationaryBoxes = turnRectlistsIntoPygameRects(stationaryBoxes)
        stationaryBoxText = convertStringIntoPygameRectlists(stationaryBoxText, 4)

        # Combine them all
        stationaryRectlists = addLists([stationaryText, stationaryBoxes, stationaryBoxText])
        if showPlayer:
            stationaryRectlists = addLists([stationaryRectlists, player, healthbar, healthbarText])
        
        # --------------------------
        # ----- Moving objects -----
        # --------------------------

        # Blocks
        blocks = blockData.run(screenNum, rx / 16, ry / 16)
        
        blocks = decodeBlocks.run(blocks, 64, 4)
        # blocks = turnRectlistsIntoPygameRects(blocks)

        # Hitboxes
        hitboxes = hitboxData.run(screenNum, rx / 16, ry / 16)
        
        if showHitboxes:
            hitboxes = decodeHitboxes.run(hitboxes, 64, 4)
            # hitboxes = turnRectlistsIntoPygameRects(hitboxes)
        else:
            hitboxes = []

        # Text
        text = textData.run(screenNum, rx, ry)            

        text = convertStringIntoPygameRectlists(text, 4)

        # Combine them all
        movingRectlists = addLists([blocks, text, hitboxes])

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
        
        rx += xVelocity / 10
        ry += yVelocity / 10

        x = rx + (width - 20) / 2
        if x % 1 < 0.5:
            x = x // 1
        else:
            x += 0.5
            x = x // 1
        
        y = ry + (width - 60) / 2
        if y % 1 < 0.5:
            y = y // 1
        else:
            y += 0.5
            y = y // 1

        actualRects = 0
        drawnRects = 0

        # Drawing
        screen.fill((255, 255, 255))
        limit = 1024
        nLimit = int('-' + str(limit))
        for rect in movingRectlists:
            actualRects += 1
            if rect[0] < nLimit or rect[0] > width or rect[0] < nLimit or rect[0] > limit:
                continue
            drawnRects += 1
        for rect in stationaryRectlists:
            actualRects += 1
            if rect[0] < nLimit or rect[0] > limit or rect[0] < nLimit or rect[0] > limit:
                continue
            drawnRects += 1

        for rect in movingRectlists:
            pygameRect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
            pygame.draw.rect(screen, rect[4], pygameRect)
        for rect in stationaryRectlists:
            pygameRect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
            pygame.draw.rect(screen, rect[4], pygameRect)

        # print(actualRects, drawnRects)

        # Update display
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()

# Normal stuff
if __name__ == "__main__":
    main()