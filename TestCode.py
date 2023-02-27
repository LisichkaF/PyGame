import sys
import pygame

pygame.init()

def main():
    screen = pygame.display.set_mode((400, 400))
    font = pygame.font.SysFont('Arial', 200, False, False)

    lives = "Hi"

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            lives = "Goodbye"

        screen.fill((255, 255, 255))
        text = font.render(str(lives), True, (0,0,0))

        screen.blit(text, (25, 25))
        pygame.display.flip()

main()