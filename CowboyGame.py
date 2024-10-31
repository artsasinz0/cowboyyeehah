import pygame
from sys import exit
from Player_file import Player

#game_setting
pygame.init()
pygame.display.set_caption('Jack The Cowboy from Downtown')
clock = pygame.time.Clock()

#screen_ssetting
WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#fonts
fonts = pygame.font.Font('fonts/Pixeltype.ttf',90)
text_showed = fonts.render('Jack the Cowboy',False,'Red')

#img
cat_img = pygame.image.load("img_graphic/test2.png")

#player_file
player = Player(WIDTH // 2, 500)

def get_background():
    background_image = pygame.image.load("img_graphic/test1.png")
    background_image = pygame.transform.scale(background_image,(1080,720))
    screen.blit(background_image,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        
        keys = pygame.key.get_pressed()
        player.left_pressed = keys[pygame.K_a]
        player.right_pressed = keys[pygame.K_d]
        player.space_pressed = keys[pygame.K_SPACE]
                     
    get_background()   
    player.update()
    player.draw(screen)
    
    screen.blit(text_showed,(WIDTH//3.5,50))

    pygame.display.update()
    clock.tick(120)