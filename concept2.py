import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hero Tower Wars")

background_image = pygame.image.load("test1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

cat_image = pygame.image.load("test2.png")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

while True:
    screen.blit(background_image, (0, 0))
    
    screen.blit(cat_image, (960,540))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")

    pygame.display.flip()


pygame.quit()