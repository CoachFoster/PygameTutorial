import pygame

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

width, height = 800,  580

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Template')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # find the center
    pygame.draw.circle(screen, GREEN, [10, 10], 10)

    # draw rectangles
    pygame.draw.rect(screen, RED, [100, 200, 50, 80], 0)
    pygame.draw.rect(screen, RED, [200, 200, 50, 80], 2)

    # draw a house
    pygame.draw.rect(screen, WHITE, [500, 325, 200, 250], 5)
    # roof
    pygame.draw.polygon(screen, GREEN, [[450, 327], [600, 200], [750, 327]], 0)
    # window
    pygame.draw.rect(screen, YELLOW, [525, 350, 60, 60], 0)
    # window frame, horiz
    pygame.draw.line(screen, BLACK, [525, 380], [585, 380], 4)
    # window frame, vert
    pygame.draw.line(screen, BLACK, [555, 350], [555, 410], 4)
    # door
    pygame.draw.rect(screen, BLUE, [562, 460, 80, 110], 0)
    # door knob
    pygame.draw.circle(screen, RED, [582, 510], 8)

    pygame.display.update()

pygame.quit()