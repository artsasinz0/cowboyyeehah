import pygame
from sys import exit
from Player_file import Player
from Enemy_file import Enemy
from Item_file import Item
# from Camera_file import Camera

#game_setting
pygame.init()
pygame.display.set_caption('Jack The Cowboy from Downtown')
clock = pygame.time.Clock()
FPS = 30

#screen_setting
WIDTH, HEIGHT = 1440, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# camera = Camera(500,720)

#fonts
fonts = pygame.font.Font('fonts/Pixeltype.ttf',90)
text_showed0 = fonts.render('Jack the Cowboy',False,'Red')
text_showed_rect = text_showed0.get_rect(center=(WIDTH//2,60)) 

#img
cat_img = pygame.image.load("img_graphic/test2.png")

#Player_file
player = Player(x=WIDTH//4, y=500, hp=12)
attack_status = False

#Emeny_file
enemy_group = pygame.sprite.Group()
enemies = [
    Enemy(x=600,y=100,hp=89), 
    Enemy(x=600,y=200,hp=186),
    Enemy(x=600,y=300,hp=40),
    Enemy(x=600,y=400,hp=22),
    Enemy(x=600,y=500,hp=11) 
]
for enemy in enemies:
    enemy_group.add(enemy)

#Item_file
item_group = pygame.sprite.Group()
items = [
    Item(name="Health Potion I", x=400, y=200, value=10,req=140), 
    Item(name="Health Potion II", x=400, y=300, value=5,req=80)
]
for item in items:
    item_group.add(item)
    
###################### '''selecting setting''' #######################
selected_enemy_index = 0
selected_items_index = 0
selecting_items  = False

########################## '''background''' ###########################
background_image = pygame.image.load("img_graphic/test1.png")
background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))
def get_background():
    screen.blit(background_image,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
            
        ############ '''press "|E|" to switch mode''' ############
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                selecting_items = not selecting_items
                
            ########################### '''enemy_selection''' ###########################
            if selecting_items != True and len(enemy_group) > 0:
                if event.key == pygame.K_w and len(enemy_group) > 0:
                    selected_enemy_index = (selected_enemy_index-1) % len(enemy_group)
                elif event.key == pygame.K_s and len(enemy_group) > 0:
                    selected_enemy_index = (selected_enemy_index+1) % len(enemy_group)
                elif event.key == pygame.K_f and len(enemy_group) > 0:
                    attack_status = True
                
            ########################### '''items_selection''' ###########################
            if selecting_items == True and len(items) > 0:
                if event.key == pygame.K_w:
                    selected_items_index = (selected_items_index-1) % len(item_group)
                elif event.key == pygame.K_s:
                    selected_items_index = (selected_items_index+1) % len(item_group)
                elif event.key == pygame.K_f:
                    if 0 <= selected_items_index < len(items):
                        selected_item = items[selected_items_index]
                        if selected_item.requirement(player):
                            selected_item.apply_item(player)
                            item_group.remove(selected_item)  
                            items.remove(selected_item)
                            selected_items_index = 0
                        else:
                            print("Invalid item selection index.") #check

    ############################################# '''player_movement''' #############################################
    keys = pygame.key.get_pressed()
    player.left_pressed = keys[pygame.K_a]
    player.right_pressed = keys[pygame.K_d]
    player.space_pressed = keys[pygame.K_SPACE]
            
    ############################################### '''player_attack''' #############################################
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
                enemy_group.remove(selected_enemy)
                selected_enemy.kill()
                player.health_point.hp += original_enemy_hp # add player's hp when enemy defeated.
                if len(enemy_group) > 0:
                    selected_enemy_index = 0
    attack_status = False
    
    get_background()  
        
    ################################################ '''draw player''' ################################################
    player.update(screen)
    # screen.blit(player.character, camera.apply(player))
    player.draw(screen)
    player.draw_hp(screen)   
    ################################################# '''draw enemy''' ################################################
    for enemy in enemy_group:
        # screen.blit(enemy.image, camera.apply(enemy))
        enemy.draw(screen)
        enemy.draw_hp(screen)
    ################################################# '''draw item''' #################################################
    for item in items:
        # screen.blit(item.item_img, camera.apply(item))
        item.draw(screen)
            
    # let's draw some highlight around things babyyyyyyyyy 
    if selecting_items and len(items) > 0:
        selected_item = items[selected_items_index]
        pygame.draw.rect(screen, (0, 255, 0), selected_item.rect.inflate(10, 10), 2)
    if not selecting_items and len(enemy_group) > 0:  
        selected_enemy = enemy_group.sprites()[selected_enemy_index]
        pygame.draw.rect(screen, (255, 0, 0), selected_enemy.rect.inflate(10, 10), 2)  
            
    #Jack the cowboy text
    screen.blit(text_showed0,(text_showed_rect))
        
    pygame.display.update()
    clock.tick(FPS) # '''controls the Framerates'''