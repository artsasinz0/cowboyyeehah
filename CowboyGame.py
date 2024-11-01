import pygame
from sys import exit
from Player_file import Player
from Enemy_file import Enemy

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
text_showed_rect = text_showed.get_rect(center=(WIDTH//2,70)) 

#gameover
gameover = False
gameover_text = fonts.render('Game Over',False,'Red')
gameover_rect = gameover_text.get_rect(center=(WIDTH//2,HEIGHT//2)) #center the text

#img
cat_img = pygame.image.load("img_graphic/test2.png")

#Player_file
player = Player(x = WIDTH // 4, y = 500, hp=12)

#Emeny_file
enemy_group = pygame.sprite.Group()
enemy1 = Enemy(x=500, y=550, hp=10)
enemy2 = Enemy(x=600, y=550, hp=8)   
enemy3 = Enemy(x=700, y=550, hp=13)  
enemy4 = Enemy(x=800, y=550, hp=6)
enemy_group.add(enemy1,enemy2,enemy3,enemy4)

def get_background():
    background_image = pygame.image.load("img_graphic/test1.png")
    background_image = pygame.transform.scale(background_image,(1080,720))
    screen.blit(background_image,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        
    #player_movement
    keys = pygame.key.get_pressed()
    player.left_pressed = keys[pygame.K_a]
    player.right_pressed = keys[pygame.K_d]
    player.space_pressed = keys[pygame.K_SPACE]
        
    #player_attack
    player.f_pressed = keys[pygame.K_f]
    if player.f_pressed:
        for enemy in enemy_group:
            if player.rect.colliderect(enemy.rect):
                if player.health_point.hp < enemy.health_point.hp:
                    gameover = True
                    print("Game over") #check
                else:
                    enemy.take_dmg(player.health_point.hp)  
                    print("Enemy died") #check 
        
    get_background()   
    player.update()
    player.draw(screen)
    
    #enemy
    for enemy in enemy_group:
        enemy.draw(screen)
        
    screen.blit(text_showed,(text_showed_rect))
    
    if gameover:
        screen.blit(gameover_text, (gameover_rect))
    
    pygame.display.update()
    clock.tick(30) #control Framerates