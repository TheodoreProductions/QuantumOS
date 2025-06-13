# source pygame-env/bin/activate
# -m venv pyinstaller-env
# source pyinstaller-env/bin/activate
# pip install pyinstaller
# pyinstaller --onefile --name "Game" game.py
# and then zip it

import pygame
import sys

from objects import decodeObjects

def do_nothing():
    a = 0

def turnBlocksIntoPygameRects(blocks):
    newBlocks = []
    for i in blocks:
        rect = pygame.Rect(i[0], i[1], i[2], i[3])
        newRect = [rect, i[4]]
        newBlocks.append(newRect)
    return newBlocks

def convertStringIntoPygameRects(text, x, y, p, c):
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
                textCode.append([t[0][i], t[1] + spaceDelay, t[2] + verticalDelay])
            spaceDelay += 6
    rectList = decodeObjects.decodeText(textCode, p, c)
    rectList = turnBlocksIntoPygameRects(rectList)
    return rectList

def main():
    pygame.init()

    # Debug
    debug = True

    # Colors
    pureWhite = (255, 255, 255)
    pureBlack = (0, 0, 0)
    pureRed = (255, 0, 0)
    pureGreen = (0, 255, 0)
    pureBlue = (0, 0, 255)

    width, height = 1000, 1000

    # Screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The blank window... or is it?")

    # Generate blocks
    blockSize = 64
    pixelSize = 4

    # Blocks
    debugBlocks = [['grass', 0, 3], ['replacement texture', 1, 3]]
    if debug:
        blocks = debugBlocks
    else:
        blocks = []
    blocks = decodeObjects.decodeBlocks(blocks, blockSize, pixelSize)
    blocks = turnBlocksIntoPygameRects(blocks)

    # Borders
    debugBorders = [['n', 0, 4], ['e', 1, 4], ['s', 2, 4], ['w', 3, 4], ['1', 4, 4], ['2', 5, 4], ['3', 6, 4], 
                    ['4', 7, 4]]
    if debug:
        borders = debugBorders
    else:
        borders = []
    borders = decodeObjects.decodeBorders(borders, blockSize, pixelSize)
    borders = turnBlocksIntoPygameRects(borders)

    # Text
    debugText = [['''A BCDEFGHIJKLMNOPQRSTUVWXYZ\na bcdefghijklmnopqrstuvwxyz\n0 123456789\n. ,!?()[]{-}_=+@#$%^&*/\\|<>\n�''', 1, 1]]
    if debug:
        text = debugText
    else:
        text = ''
    text = convertStringIntoPygameRects(text, 1, 1, pixelSize, (0, 0, 0))
    for t in text:
        blocks.append(t)
    for border in borders:
        blocks.append(border)

    # Player settings
    xVelocity = 0
    yVelocity = 0
    speed = 0.6
    frictionSpeed = 0.3

    player = pygame.Rect((width / 2) - 25, (height / 2) - 25, blockSize, blockSize)

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
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

        # ---------------------------------------------------------------------------------

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

        for block in blocks:
            # Apply movement
            block[0].x += xVelocity
            block[0].y += yVelocity

        # Drawing
        screen.fill(pureWhite)
        for block in blocks:
            pygame.draw.rect(screen, block[1], block[0])
        for t in text:
            pygame.draw.rect(screen, t[1], t[0])
        pygame.draw.rect(screen, pureBlack, player)
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()