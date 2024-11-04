import pygame

#size of player
W = 150
H = 150

#png
character_face_left = pygame.image.load('img_graphic/cowboy1.png')
character_face_left = pygame.transform.scale(character_face_left,(W,H))

character_face_right = pygame.image.load('img_graphic/cowboy2.png')
character_face_right = pygame.transform.scale(character_face_right,(W,H))

class Player:
    def __init__(self,x,y,hp):
        self.x = int(x)
        self.y = int(y)
        self.character = character_face_right
        self.rect = self.character.get_rect(topleft=(x,y))
        self.velX = 0 
        self.velY = 0 
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        self.f_pressed = False
        self.speed = 6
        self.gravity = 10
        self.jump_strength = 150 #'''how high player can jump'''
        self.still_on_ground = True
        self.ground_level = 500 #'''set the ground level'''
        self.health_point = Healthpoint(hp)
        
    def gameover(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',110)
        gameover_text = fonts.render('Game Over',False,'Red')
        gameover_rect = gameover_text.get_rect(center=(self.rect.centerx, self.rect.centery)) #center the text at player's center
        screen.blit(gameover_text, gameover_rect)
        pygame.display.update()
        pygame.time.wait(1500)
        pygame.quit()
        exit() 
        
    def draw(self,screen):
        screen.blit(self.character, (self.x,self.y))
    
    def draw_hp(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',50)
        hp_text = fonts.render(f'HP:{self.health_point.hp}',False,'Green')
        hp_rect = hp_text.get_rect(center=(self.x+W,self.y))
        screen.blit(hp_text, hp_rect)
        
    def update(self):
        self.velX = 0
        self.velY = 0
        
        if not self.health_point.still_alive():
            self.gameover()
            
        #'''WASD'''
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            self.character = character_face_left
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            self.character = character_face_right
            
        #'''Jumping'''
        if self.space_pressed and self.still_on_ground:
            self.velY = -self.jump_strength
            self.still_on_ground = False    
            print("jumped") #check
        if not self.still_on_ground:
            self.velY += self.gravity   
        self.y += self.velY
        if self.y >= self.ground_level:
            self.y = self.ground_level  # <------------------------------'''self.y in this line should be ground cordinates(pos_y)'''
            self.velY = 0  
            self.still_on_ground = True 
            # print("landed") #check
        self.x += self.velX
        
        self.rect.topleft = (self.x, self.y)
              
class Healthpoint:
    def __init__(self, hp):
        self.hp = hp
       
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        
    def still_alive(self):
        return self.hp > 0