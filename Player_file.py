import pygame

W = 150
H = 150

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
        self.jump_strength = 150 #'''how high you jump'''
        self.still_on_ground = True
        self.ground_level = 500 #'''ground level'''
        self.health_point = Healthpoint(hp)
        
        
    def draw(self,screen):
        screen.blit(self.character, (self.x,self.y))
        
    def update(self):
        self.velX = 0
        self.velY = 0
        
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
    
# if __name__ == "__main__":
#     # Create player and enemy with different health points
#     player = Player(x=100, y=500, hp=100)
#     enemy = Player(x=200, y=500, hp=50)
    
#     # Before attack
#     print("Before attack:")
#     print("Player HP:", player.health_point.hp)
#     print("Enemy HP:", enemy.health_point.hp)
    
#     # Player attacks enemy
#     player.atk(enemy)
    
#     # After attack
#     print("After attack:")
#     print("Player HP:", player.health_point.hp)
#     print("Enemy HP:", enemy.health_point.hp)
    
#     # Check if enemy is alive
#     if enemy.health_point.still_alive():
#         print("Enemy is still alive.")
#     else:
#         print("Enemy is defeated.")