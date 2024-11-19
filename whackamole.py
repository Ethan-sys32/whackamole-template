import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        WIDTH, HEIGHT, SIZE = 20, 16, 32
        mole_x, mole_y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (mole_x * SIZE <= mouse_x < (mole_x + 1) * SIZE
                            and mole_y * SIZE <= mouse_y < (mole_y + 1) * SIZE):
                        mole_x = random.randint(0, WIDTH - 1)
                        mole_y = random.randint(0, HEIGHT - 1)
            screen.fill("light green")
            for x in range(0, 640, SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, SIZE):
                pygame.draw.line(screen, "black", (0, y), (640, y))
            screen.blit(mole_image, (mole_x * SIZE, mole_y * SIZE))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
