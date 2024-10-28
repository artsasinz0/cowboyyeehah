import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920 , 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
BACKGROUND_COLOR = (30, 30, 60)  # Dark blue
BUTTON_COLOR = (100, 100, 250)  # Light blue
HIGHLIGHT_COLOR = (150, 150, 255)  # Lighter blue for hover effect
TEXT_COLOR = (255, 255, 255)  # White

# Fonts
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 36)

background_image = pygame.image.load("test1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

cat_image = pygame.image.load("test2.png") 

# Button properties
button_texts = ["Start Game", "Options", "Quit"]
buttons = []
for i, text in enumerate(button_texts):
    button_rect = pygame.Rect(WIDTH // 2 - 100, 200 + i * 80, 200, 50)
    buttons.append((button_rect, text))

def draw_background():
    screen.blit(background_image, (0, 0))
    
    screen.blit(cat_image, (960,540))
    
    # Draw a title
    title_text = font.render("Game Menu", True, TEXT_COLOR)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    # Draw buttons
    for button_rect, text in buttons:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
        button_text = button_font.render(text, True, TEXT_COLOR)
        screen.blit(button_text, (button_rect.x + button_rect.width // 2 - button_text.get_width() // 2,
                                  button_rect.y + button_rect.height // 2 - button_text.get_height() // 2))

def main():
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button is clicked
                mouse_pos = pygame.mouse.get_pos()
                for button_rect, text in buttons:
                    if button_rect.collidepoint(mouse_pos):
                        if text == "Start Game":
                            subprocess.Popen(["python", "concept2.py"])
                        elif text == "Options":
                            print("Options button clicked!")
                        elif text == "Quit":
                            pygame.quit()
                            sys.exit()

        # Draw background and buttons
        draw_background()

        # Update display
        pygame.display.flip()

# Run the main loop
main()
