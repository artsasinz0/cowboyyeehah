import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Tower Wars")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Character classes
class Character:
    def __init__(self, name, health, attack, x, y):
        self.name = name
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 100, 100))
        name_text = font.render(self.name, True, WHITE)
        health_text = font.render(f"Health: {self.health}", True, WHITE)
        attack_text = font.render(f"Attack: {self.attack}", True, WHITE)
        screen.blit(name_text, (self.x + 10, self.y + 10))
        screen.blit(health_text, (self.x + 10, self.y + 40))
        screen.blit(attack_text, (self.x + 10, self.y + 70))

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        enemy.health -= self.attack

# Create characters
hero = Character("Hero", 10, 10, 150, 250)
enemy1 = Character("Goblin", 15, 5, 550, 300)
enemy2 = Character("Dragon", 24, 15, 550, 100)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if enemy1.is_alive():
                    hero.attack_enemy(enemy1)
                elif enemy2.is_alive():
                    hero.attack_enemy(enemy2)

    # Draw characters
    hero.draw(screen)
    if enemy1.is_alive():
        enemy1.draw(screen)
    if enemy2.is_alive():
        enemy2.draw(screen)

    # Check for game end conditions
    if not hero.is_alive():
        game_over_text = font.render("Game Over! The enemies have won.", True, BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    elif not enemy1.is_alive() and not enemy2.is_alive():
        victory_text = font.render("Victory! The hero has won.", True, BLACK)
        screen.blit(victory_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()