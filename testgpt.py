import pygame
from sys import exit
from Player_file import Player
from Item_file import Item
from Enemy_file import Enemy,Enemy01
from Tower_file import Tower

# Game Settings
pygame.init()
pygame.display.set_caption('Tower Progression Game')
clock = pygame.time.Clock()
FPS = 50

# Screen Settings
WIDTH, HEIGHT = 1440, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Fonts
fonts = pygame.font.Font('fonts/Pixeltype.ttf', 30)

# Background
background_image = pygame.image.load("img_graphic/map1.png")

def draw_background():
    screen.blit(background_image, (0, 0))

# Player
player = Player(x=110, y=550, hp=12)

# Create Towers
towers1 = [
    Tower(1, enemies=
            [Enemy(x=510, y=555, hp=10)]),
    Tower(2, enemies=
            [Enemy(x=720, y=445, hp=10)], 
            items=
            [Item("Potion I", 720, 570, value=2, effect_type="multi")]),
    Tower(3, enemies=
            [Enemy(x=930, y=555, hp=10), 
            Enemy(x=930, y=330, hp=10)], 
            items=
            [Item("Potion II", 929, 460, value=2, effect_type="div")]),
]

towers2 = [
    Tower(1, enemies=
          [Enemy(x=350, y=555, hp=10),
           Enemy(x=350, y=328, hp=10),
           Enemy(x=350, y=218, hp=10),
           Enemy(x=350, y=108, hp=10)], 
          items=
          [Item("Potion V", 350, 460, 1.5, effect_type="multi")]),
    Tower(2, enemies=
          [Enemy(x=560, y=555, hp=60), 
           Enemy(x=560, y=328, hp=40)], 
          items=[Item("Potion VI", 560, 235, 2, effect_type="multi")]),
    Tower(3, enemies=
          [Enemy(x=770, y=218, hp=70), 
           Enemy(x=770, y=108, hp=50)], 
          items=[Item("Potion VII", 768, 345, 1.2, effect_type="multi")]),
    Tower(4, enemies=
          [Enemy(x=975, y=555, hp=80), 
           Enemy(x=975, y=440, hp=60)], 
          items=[Item("Potion VIII", 975, 345, 1.3, effect_type="multi")]),
]

text_showed = False

current_tower_index = 0  # Start with Tower 1
selected_enemy_index = 0  # Enemy selection in the current tower
current_level = 1
if current_level == 1:
    towers = towers1
elif current_level == 2:
    towers = towers2

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Enemy and Item Selection Logic
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and len(towers[current_tower_index].get_all_objects()) > 0:  # Select previous object
                selected_enemy_index = (selected_enemy_index - 1) % len(towers[current_tower_index].get_all_objects())
            elif event.key == pygame.K_s and len(towers[current_tower_index].get_all_objects()) > 0:  # Select next object
                selected_enemy_index = (selected_enemy_index + 1) % len(towers[current_tower_index].get_all_objects())
            elif event.key == pygame.K_f and len(towers[current_tower_index].get_all_objects()) > 0:  # Interact with selected object
                all_objects = towers[current_tower_index].get_all_objects()

                # Ensure selected_enemy_index is within bounds
                if selected_enemy_index >= len(all_objects):
                    selected_enemy_index = 0  # Reset to the first object if index is out of range

                if selected_enemy_index < len(all_objects):
                    selected_object = all_objects[selected_enemy_index]

                    if isinstance(selected_object, (Enemy, Enemy01)):
                        player.attack() 
                        if selected_object.e_health_point.hp <= player.health_point.hp:
                            original_enemy_hp = selected_object.e_health_point.hp
                            selected_object.take_dmg(player.health_point.hp)
                            if not selected_object.e_health_point.still_alive():
                                print("Enemy defeated!")
                                player.health_point.hp += original_enemy_hp
                                towers[current_tower_index].enemies.remove(selected_object)
                               
                        elif selected_object.e_health_point.hp > player.health_point.hp:
                            player.gameover(screen)

                    elif isinstance(selected_object, Item):
                        player.item_applied()
                        selected_object.apply_item(player)
                        towers[current_tower_index].items.remove(selected_object)  # Remove item after use

                    # After using the item, check if there are still objects left and update selection
                    if len(towers[current_tower_index].get_all_objects()) > 0:
                        selected_enemy_index = 0  # Reset to the first available object
                    else:
                        selected_enemy_index = -1  # No valid selection if no objects left
                        
        if towers[current_tower_index].is_cleared() and len(towers[current_tower_index].get_all_objects()) == 0:
            if current_tower_index < len(towers) - 1:
                current_tower_index += 1
            else:
                text_showed = True
                if player.rect.x >= 1350:  # Move player until they reach the screen's edge
                    if current_level == 1:
                        current_level += 1
                        towers = towers2
                        current_tower_index = 0
                        selected_enemy_index = 0
                        # player.rect.x = 100
                        player.x = 110
                        text_showed = False
                        background_image = pygame.image.load("img_graphic/map2.png")
                    else:
                        print("You completed all levels! Congratulations!")
    
    keys = pygame.key.get_pressed()
    player.left_pressed = keys[pygame.K_a]
    player.right_pressed = keys[pygame.K_d]
                     
    # Drawing
    draw_background()
    for tower in towers:
        tower.draw(screen)

    all_objects = towers[current_tower_index].get_all_objects()

    if len(all_objects) > 0:
        selected_object = all_objects[selected_enemy_index]

        if isinstance(selected_object, (Enemy,Enemy01)):
            pygame.draw.rect(screen, (255, 0, 0), selected_object.rect.inflate(10, 10), 2)
        elif isinstance(selected_object, Item):  # Highlight the selected item
            pygame.draw.rect(screen, (0, 255, 0), selected_object.rect.inflate(10, 10), 2)  # Green border for selected item

    # Draw items and enemies normally
    for item in towers[current_tower_index].items:  # Draw items in the current tower
        item.draw(screen)
    for enemy in towers[current_tower_index].enemies:  # Loop through enemies in the current tower
        enemy.draw(screen)
        enemy.draw_hp(screen)
        enemy.update()
        
    player.update(screen)
    player.draw(screen)
    player.draw_hp(screen)
    
    text0 = fonts.render('Press | F | to attack.', False, 'Red')
    screen.blit(text0, (WIDTH-1400, HEIGHT-650))
    
    if text_showed:
        font0 = pygame.font.Font('fonts/Pixeltype.ttf',35)
        text1 = font0.render('Go to Right to Next Level.', False, 'Red')
        screen.blit(text1, (WIDTH-285, HEIGHT-650))
    
    pygame.display.update()
    clock.tick(FPS)
