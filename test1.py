import pygame

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Combat with W, S, and Space")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Object positions, dimensions, and HP
objects = [
    {"rect": pygame.Rect(300, 150, 100, 100), "hp": 10, "original_hp": 10},  # Object 1 with 10 HP
    {"rect": pygame.Rect(300, 300, 100, 100), "hp": 15, "original_hp": 15},  # Object 2 with 15 HP
    {"rect": pygame.Rect(300, 450, 100, 100), "hp": 20, "original_hp": 20}   # Object 3 with 20 HP
]

# Selected object index (start with the first object)
selected_index = 0

# Character settings (position and attack power)
character = {"x": 100, "y": 100, "HP": 11}

# Load font (use a default font if custom one isn't available)
try:
    font = pygame.font.Font('fonts/Pixeltype.ttf', 36)
except FileNotFoundError:
    font = pygame.font.Font(None, 36)

# Defeat state
defeated = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # Move selection up
                selected_index = (selected_index - 1) % len(objects)
            elif event.key == pygame.K_s:  # Move selection down
                selected_index = (selected_index + 1) % len(objects)
            elif event.key == pygame.K_SPACE:  # Attack selected object
                if objects[selected_index]["hp"] > character["HP"]:
                    defeated = True  # Set defeat state
                else:
                    objects[selected_index]["hp"] -= character["HP"]

                    # Ensure HP does not go below 0
                    if objects[selected_index]["hp"] < 0:
                        objects[selected_index]["hp"] = 0

                    # If the object is defeated (HP is 0), steal its original HP as attack power
                    if objects[selected_index]["hp"] == 0:
                        character["HP"] += objects[selected_index]["original_hp"]
                        # Optionally, remove defeated object or mark as defeated
                        del objects[selected_index]

            elif event.key == pygame.K_r and defeated:  # Respawn if defeated
                defeated = False  # Reset defeat state
                character["HP"] = 11  # Reset character HP (or whatever you want)
                # Optionally, you can reset other game states here

    # Draw everything
    screen.fill(WHITE)

    if defeated:
        defeated_text = font.render('You were defeated. Press R to respawn', False, 'Red')
        screen.blit(defeated_text, (200, 200))
    else:
        # Draw objects and highlight the selected one
        for i, obj in enumerate(objects):
            color = RED if i == selected_index else BLUE  # Highlight if selected
            pygame.draw.rect(screen, color, obj["rect"])

            # Draw HP as text above each object
            hp_text = font.render(f"HP: {obj['hp']}", True, GREEN)
            screen.blit(hp_text, (obj["rect"].x, obj["rect"].y - 30))

        # Draw character (for example, as a small green square)
        pygame.draw.rect(screen, GREEN, (character["x"], character["y"], 50, 50))
        
        # Draw character HP at the top of the screen
        player_text = font.render(f"HP: {character['HP']}", True, (0, 0, 255))
        screen.blit(player_text, (100, 60))

    # Update display
    pygame.display.flip()

    # Set FPS
    pygame.time.Clock().tick(30)

pygame.quit()
