import pygame
from sys import exit

#game_setting
pygame.init()
pygame.display.set_caption('Jack The Cowboy from Downtown')
clock = pygame.time.Clock()

#screen_ssetting
screen = pygame.display.set_mode((1080,720))

#fonts
fonts = pygame.font.Font('fonts/Pixeltype.ttf',90)
text_showed = fonts.render('Jack the Cowboy',False,'Red')

#backgroundthingthing
background_image = pygame.image.load("img_graphic/test1.png")
background_image = pygame.transform.scale(background_image,(1080,720))

#img
cat_img = pygame.image.load("img_graphic/test2.png")
cowboy0_1 = pygame.image.load("img_graphic/cowboy0_1.png")
cowboy0_2 = pygame.image.load("img_graphic/cowboy0_2.png")
cowboy1 = pygame.image.load("img_graphic/cowboy1.png")
cowboy2 = pygame.image.load("img_graphic/cowboy2.png")

#position
pos_x_cowboy = 750
pos_y_cowboy = 575
pos_x_cowboy0 = 1000

#qte
qte_active = False
qte_starttime = 0
qte_duration = 2000
qte_success = False

def get_background():
    screen.blit(background_image,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if qte_active:
            if event.type == pygame.K_SPACE:
                if event.key == pygame.K_SPACE:
                    qte_success = True
                    qte_active = False
                else:
                    qte_success= False
                    qte_active = False
                    
    get_background()    
    
    if pos_x_cowboy == 800 and qte_active == False:
        qte_active = True
        qte_starttime = pygame.time.get_ticks()
        
    if qte_active == True:
        qte_txt = fonts.render('Press SPACE',False,'Black')
        screen.blit(qte_txt,(300,200))
        
        if qte_active and pygame.time.get_ticks() - qte_starttime > qte_duration:
            qte_txt0 = fonts.render("QTE Time Expired!",False,'Blue')
            screen.blit(qte_txt0,(300,300))
            qte_active = False
            
    if qte_active == True:
        if qte_success is True:
            qte_txt = fonts.render('YES', False, 'Black')
            screen.blit(qte_txt, (300, 300))
        else:
            if qte_success is False:
                qte_txt = fonts.render('NO', False, 'Black')
                screen.blit(qte_txt, (300, 300))
        # Reset the success flag for next QTE
        qte_success = None
        
    # '''show_text'''
    screen.blit(text_showed,(320,50))
    
    # '''animated_test'''
    screen.blit(cowboy0_2,((pos_x_cowboy0),500))
    if pos_x_cowboy0 > 0:
        pos_x_cowboy0 -= 6
    elif pos_x_cowboy0 <= 0:
        pos_x_cowboy0 = 1000
        
    # '''walk wasd'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pos_x_cowboy -= 4
        character = screen.blit(cowboy1, (pos_x_cowboy,pos_y_cowboy))
        
    elif keys[pygame.K_d]:
        pos_x_cowboy += 4
        character = screen.blit(cowboy2, (pos_x_cowboy,pos_y_cowboy))
    
    else:
        character = screen.blit(cowboy1, (pos_x_cowboy,pos_y_cowboy))
    
    pygame.display.update()
    clock.tick(60)