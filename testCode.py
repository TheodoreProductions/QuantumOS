# run 'source pygame-env/bin/activate'

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 1024))
    pygame.display.set_caption("3d renderer")

    # Define colors
    white = (255, 255, 255)
    blue = (0, 0, 255)

    polygonList = [
        [blue, 1, 1, 2, 1, 3, 2, 2, 2]
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        for p in polygonList:
            polyCoords = [(p[1], p[2]), (p[3], p[4]), (p[5], p[6]), (p[7], p[8])]
            pygame.draw.polygon(screen, p[0], polyCoords)

        pygame.display.flip()  # update the full display

    pygame.quit()

if __name__ == "__main__":
    main()