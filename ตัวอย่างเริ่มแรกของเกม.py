import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Addition Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 50)

# Fixed values for each level
levels = {
    1: (3, 2, 11),   # Level 1: (B, C, D)
    2: (16, 19, 51), # Level 2: (B, C, D)
    3: (86, 99, 200)  # Level 3: (B, C, D)
}

# Function to reset the game
def reset_game(level):
    global option_b, option_c, option_d, game_over, message, selected_options
    option_b, option_c, option_d = levels[level]  # Get values from levels dictionary
    game_over = False
    message = ""
    selected_options = []  # Track selected options

# Initial game setup
number_a = 10  # Set starting value of A to 10
level = 1
reset_game(level)
next_level = False  # Track if the player is ready for the next level
next_count = 0  # Count how many times the player has reached the next level
running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for mouse click on options
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Option B
            if 'B' not in selected_options and option_b_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_b:  # Check if A is greater or equal
                    selected_options.append('B')
                    number_a += option_b  # Add value to number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # End the game

            # Option C
            elif 'C' not in selected_options and option_c_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_c:  # Check if A is greater or equal
                    selected_options.append('C')
                    number_a += option_c  # Add value to number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # End the game

            # Option D
            elif 'D' not in selected_options and option_d_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_d:  # Check if A is greater or equal
                    selected_options.append('D')
                    number_a += option_d  # Add value to number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # End the game

            # Check for win condition
            if len(selected_options) == 3 and not game_over:
                next_count += 1  # Increment next level counter
                if next_count == 3:  # Win after 3 levels
                    message = "Win! Press R to Restart."
                    game_over = True  # End the game
                else:
                    message = "Next! Click to proceed to the next level."
                    next_level = True  # Set to True when the player can go to the next level

        # Check for next level click
        if next_level and event.type == pygame.MOUSEBUTTONDOWN:
            level += 1  # Increase level for new fixed numbers
            if level <= len(levels):
                reset_game(level)  # Generate new numbers for the next level
            next_level = False  # Reset next level flag

        # Check for restart key press
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Check if R is pressed
                number_a = 5  # Reset A to 5
                level = 1  # Reset level to 1
                reset_game(level)  # Reset the game
                next_count = 0  # Reset next count
                message = ""  # Clear message
                game_over = False  # Reset game over flag

    # Display the numbers and options
    number_a_text = font.render(f"A: {number_a}", True, BLACK)
    message_text = font.render(message, True, RED if game_over else BLACK)

    screen.blit(number_a_text, (50, HEIGHT // 4))  # Move A to the left side

    # Display all options, hiding selected ones
    if 'B' not in selected_options:
        option_b_text = font.render(f"B: {option_b}", True, GREEN)
        option_b_rect = screen.blit(option_b_text, (WIDTH // 4, HEIGHT // 2))
    
    if 'C' not in selected_options:
        option_c_text = font.render(f"C: {option_c}", True, GREEN)
        option_c_rect = screen.blit(option_c_text, (WIDTH // 2 - 50, HEIGHT // 2))
    
    if 'D' not in selected_options:
        option_d_text = font.render(f"D: {option_d}", True, GREEN)
        option_d_rect = screen.blit(option_d_text, (3 * WIDTH // 4 - 50, HEIGHT // 2))

    # Display the message for proceeding to the next level or restarting
    if next_level or game_over:
        screen.blit(message_text, (WIDTH // 2 - 250, 3 * HEIGHT // 4))
    else:
        screen.blit(message_text, (WIDTH // 2 - 150, 3 * HEIGHT // 4))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
