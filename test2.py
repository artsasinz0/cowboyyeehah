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

# Tower positions, dimensions, and HP
towers = [
    [  # Tower 1
        {"rect": pygame.Rect(300, 150, 100, 100), "hp": 10, "original_hp": 10},  # Part 1
        {"rect": pygame.Rect(300, 300, 100, 100), "hp": 15, "original_hp": 15},  # Part 2
        {"rect": pygame.Rect(300, 450, 100, 100), "hp": 20, "original_hp": 20}   # Part 3
    ],
    [  # Tower 2
        {"rect": pygame.Rect(500, 150, 100, 100), "hp": 12, "original_hp": 12},
        {"rect": pygame.Rect(500, 300, 100, 100), "hp": 18, "original_hp": 18},
        {"rect": pygame.Rect(500, 450, 100, 100), "hp": 25, "original_hp": 25}
    ],
    [  # Tower 3
        {"rect": pygame.Rect(700, 150, 100, 100), "hp": 15, "original_hp": 15},
        {"rect": pygame.Rect(700, 300, 100, 100), "hp": 20, "original_hp": 20},
        {"rect": pygame.Rect(700, 450, 100, 100), "hp": 30, "original_hp": 30}
    ]
]

# Selected tower and part index (start with the first tower and its first part)
selected_tower_index = 0
selected_part_index = 0

# Character settings (position and attack power)
character = {"x": 100, "y": 100, "HP": 11}
original_character_hp = character["HP"]  # Store the original HP for respawn

# Load font (use a default font if custom one isn't available)
try:
    font = pygame.font.Font('fonts/Pixeltype.ttf', 36)
except FileNotFoundError:
    font = pygame.font.Font(None, 36)

# Main loop
running = True
defeated = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # Move selection up
                selected_part_index = (selected_part_index - 1) % len(towers[selected_tower_index])
            elif event.key == pygame.K_s:  # Move selection down
                selected_part_index = (selected_part_index + 1) % len(towers[selected_tower_index])
            elif event.key == pygame.K_a:  # Move to the previous tower
                selected_tower_index = (selected_tower_index - 1) % len(towers)
                selected_part_index = 0  # Reset part index when switching towers
            elif event.key == pygame.K_d:  # Move to the next tower
                selected_tower_index = (selected_tower_index + 1) % len(towers)
                selected_part_index = 0  # Reset part index when switching towers
            elif event.key == pygame.K_SPACE and not defeated:  # Attack selected tower part only if not defeated
                # Check if the leftmost tower (Tower 1) is still standing
                if selected_tower_index > 0:  # If not the first tower
                    if any(part["hp"] > 0 for part in towers[0]):
                        # Cannot attack, show a message
                        continue
                
                current_part = towers[selected_tower_index][selected_part_index]
                if current_part["hp"] > character["HP"]:
                    defeated = True  # Set defeated flag
                else:
                    current_part["hp"] -= character["HP"]

                    # Ensure HP does not go below 0
                    if current_part["hp"] < 0:
                        current_part["hp"] = 0

                    # If the part is defeated (HP is 0), steal its original HP as attack power
                    if current_part["hp"] == 0:
                        character["HP"] += current_part["original_hp"]
                        # Optionally, remove defeated object or mark as defeated
                        current_part["original_hp"] = 0  # Mark as looted

            elif event.key == pygame.K_r and defeated:  # Respawn
                character["HP"] = original_character_hp  # Reset character HP
                defeated = False  # Reset defeated flag

    # Draw everything
    screen.fill(WHITE)

    # Draw towers and highlight the selected one
    for tower_index, tower in enumerate(towers):
        for part_index, obj in enumerate(tower):
            color = RED if (tower_index == selected_tower_index and part_index == selected_part_index) else BLUE  # Highlight if selected
            pygame.draw.rect(screen, color, obj["rect"])

            # Draw HP as text above each part
            hp_text = font.render(f"HP: {obj['hp']}", True, GREEN)
            screen.blit(hp_text, (obj["rect"].x, obj["rect"].y - 30))

    # Draw character (for example, as a small green square)
    pygame.draw.rect(screen, GREEN, (character["x"], character["y"], 50, 50))
    
    # Draw character HP and attack power at the top of the screen
    player_text = font.render(f"HP: {character['HP']}", True, (0, 0, 255))
    screen.blit(player_text, (100, 60))

    # Display defeat message if defeated
    if defeated:
        defeated_text = font.render('You were defeated. Press R to respawn.', True, RED)
        screen.blit(defeated_text, (200, 200))

    # Update display
    pygame.display.flip()

    # Set FPS
    pygame.time.Clock().tick(30)

pygame.quit()
