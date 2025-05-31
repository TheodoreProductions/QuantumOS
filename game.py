import pygame
import sys

from objects import rectObjects

def do_nothing():
    a = 0

def settingCustomize():
    width = input('Please enter the screen width:')
    height = input('Please enter the screen height:')
    return width, height

def turnBlocksIntoPygameRects(blocks):
    newBlocks = []
    for i in blocks:
        rect = pygame.Rect(i[0], i[1], i[2], i[3])
        newRect = [rect, i[4]]
        newBlocks.append(newRect)
    return newBlocks

def readCode(code):
    codes = []
    blocks = []
    for i in range(len(code) / 2):
        currentCode = code[(2 * i) - 1] + code[2 * i]
        codes.append(currentCode)
    for i in currentCode:
        if i == '00':
            blocks.append(['grass', ])


def addObjects(objects, blockSize):
    objectList = []
    p = 0.0625
    for obj in objects:
        if obj[0] == 'grass':
            objectList.append(rectObjects.rect(obj[1], obj[2], obj[3], obj[4], blockSize, (0, 128, 0)))
        elif obj[0] == 'path0':
            objectList.append(rectObjects.rect(obj[1], obj[2], obj[3], obj[4], blockSize, (155, 155, 115)))
        elif obj[0] == 'pathN':
            objectList.append(rectObjects.rect(obj[1], obj[2], 1, p, blockSize, (110, 75, 0)))
            objectList.append(rectObjects.rect(obj[1], obj[2] + p, 1, 1 - p, blockSize, (155, 155, 115)))
        elif obj[0] == 'pathE':
            objectList.append(rectObjects.rect(obj[1] + 1 - p, obj[2], p, 1, blockSize, (110, 75, 0)))
            objectList.append(rectObjects.rect(obj[1], obj[2], 1 - p, 1, blockSize, (155, 155, 115)))
    return objectList

def main():
    print('loading...')
    pygame.init()

    # Customize settings
    answer = input('Do you want to customize settings(y/n)?\n')
    if answer == 'y':
        width, hight = settingCustomize()
    else:
        width, height = 1000, 1000

    # Screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The game of getting destroyed")

    # Generate blocks
    blockSize = 64
    debugBlocks = [['grass', 1, 1, 1, 1], ['path0', 2, 1, 1, 1], ['pathN', 3, 1], ['pathE', 4, 1]]
    blocks = [['grass', 1, 1, 1, 1], ['path0', 2, 1, 1, 1], ['pathN', 3, 1], ['pathE', 4, 1]]
    blocks = addObjects(blocks, blockSize)
    blocks = turnBlocksIntoPygameRects(blocks)

    # Player settings
    xVelocity = 0
    yVelocity = 0
    speed = 0.3
    frictionSpeed = 0.5

    player = pygame.Rect((width / 2) - 25, (height / 2) - 25, blockSize, blockSize)

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('Thank you for using a TheodoreProductions product.')

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                xVelocity += speed
        elif keys[pygame.K_RIGHT]:
            xVelocity -= speed
        else:
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
        else:
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
        screen.fill((255, 255, 255))
        for block in blocks:
            pygame.draw.rect(screen, block[1], block[0])
        pygame.draw.rect(screen, (0, 0, 0), player)
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print('A TheodoreProductions product')
    main()