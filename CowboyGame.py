import pygame
from sys import exit
from Player_file import Player
from Enemy_file import Enemy
# from Item_file import Item

#game_setting
pygame.init()
pygame.display.set_caption('Jack The Cowboy from Downtown')
clock = pygame.time.Clock()

#screen_setting
WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#fonts
fonts = pygame.font.Font('fonts/Pixeltype.ttf',90)
text_showed = fonts.render('Jack the Cowboy',False,'Red')
text_showed_rect = text_showed.get_rect(center=(WIDTH//2,60)) 

#img
cat_img = pygame.image.load("img_graphic/test2.png")

#Player_file
player = Player(x=WIDTH//4, y=500, hp=12)
attack_status = False

#Emeny_file
enemy_group = pygame.sprite.Group()
enemies = [
    Enemy(x=600,y=100,hp=62), 
    Enemy(x=600,y=200,hp=161),
    Enemy(x=600,y=300,hp=40),
    Enemy(x=600,y=400,hp=22),
    Enemy(x=600,y=500,hp=11) 
]
for enemy in enemies:
    enemy_group.add(enemy)

# Item initialization
# item_group = pygame.sprite.Group()
# items = [
#     Item(name="Health Potion", x=400, y=300, value=10),  # Example item
#     Item(name="Power Potion", x=500, y=200, value=5)
# ]
# for item in items:
#     item_group.add(item)
    
#select_the_enemy
selected_enemy_index = 0

def get_background():
    background_image = pygame.image.load("img_graphic/test1.png")
    background_image = pygame.transform.scale(background_image,(1080,720))
    screen.blit(background_image,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        #selected the enemy
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and len(enemy_group) > 0:
                selected_enemy_index = (selected_enemy_index-1) % len(enemy_group)
            elif event.key == pygame.K_s and len(enemy_group) > 0:
                selected_enemy_index = (selected_enemy_index+1) % len(enemy_group)
            elif event.key == pygame.K_f and len(enemy_group) > 0:
                attack_status = True
                          
    #player_movement
    keys = pygame.key.get_pressed()
    player.left_pressed = keys[pygame.K_a]
    player.right_pressed = keys[pygame.K_d]
    player.space_pressed = keys[pygame.K_SPACE]
        
    #player_attack
    if attack_status and len(enemy_group) > 0:
        selected_enemy = enemy_group.sprites()[selected_enemy_index]  # Get the highlighted enemy
        if player.health_point.hp < selected_enemy.e_health_point.hp:
            print("Game over")
            player.gameover(screen)
        else:
            original_enemy_hp = selected_enemy.e_health_point.hp
            selected_enemy.take_dmg(player.health_point.hp)
            if not selected_enemy.e_health_point.still_alive():
                print("Enemy defeated!")
                selected_enemy.kill()
                player.health_point.hp += original_enemy_hp #add player's hp
                if len(enemy_group) > 0:
                # # Ensure selected index is still valid
                #     selected_enemy_index = selected_enemy_index % len(enemy_group)
                # else:
                    selected_enemy_index = 0
    attack_status = False

    get_background()  
    
    #player 
    player.update()
    player.draw(screen)
    player.draw_hp(screen)
    
    #enemy
    for enemy in enemy_group:
        enemy.draw(screen)
        enemy.draw_hp(screen)
    
    # let's draw some highlight around enemy babyyyyyyyyy    
    if len(enemy_group) > 0:  
        selected_enemy = enemy_group.sprites()[selected_enemy_index]
        pygame.draw.rect(screen, (255, 0, 0), selected_enemy.rect.inflate(10, 10), 2)  
    
    #Jack the cowboy text
    screen.blit(text_showed,(text_showed_rect))
    
    pygame.display.update()
    clock.tick(60) #control Framerates