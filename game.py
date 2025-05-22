import pygame
import sys

def do_nothing():
    a = 0

def settingCustomize():
    width = input('Please enter the screen width:')
    height = input('Please enter the screen height:')
    return width, height

def generateBlock(x, y, size):
    blocks = pygame.Rect(x * size, y * size, size, size)
    return blocks

def generateBlocks(blocks, size):
    blocksList = []
    for block in blocks:
        blocksList.append(generateBlock(block[0], block[1], size))
    return blocksList

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
    pygame.display.set_caption("The adventure")

    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)

    # Generate blocks
    blocksXY = [[2, 2], [3, 2]]
    blockSize = 64
    blocks = generateBlocks(blocksXY, blockSize)

    # Player settings
    xVelocity = 0
    yVelocity = 0
    speed = 0.1
    frictionSpeed = 0.1

    player = pygame.Rect((width / 2) - 25, (height / 2) - 25, blockSize, blockSize)

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('Thank you for using a TheodorePriductions product.')

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
        # ---------------------
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
            block.x += xVelocity
            block.y += yVelocity

        for block in blocks:
            if player.colliderect(block):
                print('coll')

        # Drawing
        screen.fill(white)
        for block in blocks:
            pygame.draw.rect(screen, green, block)
        pygame.draw.rect(screen, black, player)
        pygame.display.flip()

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print('A TheodoreProductions product')
    main()