import pygame

#size of player
W = 70
H = 90

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        
        self.target_size = (W, H) 
        
        self.right_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking01.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking02.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking03.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking04.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking05.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking06.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking07.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking08.png'), self.target_size)
            
        ]
        self.left_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking011.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking022.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking033.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking044.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking055.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking066.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking077.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyWalking088.png'), self.target_size)
            
        ]
        self.idle = [
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle01.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle02.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle03.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle04.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle05.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle06.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyIdle07.png'), self.target_size),
        ]
        
        self.attack_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyShoot01.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyShoot02.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyShoot03.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyShoot04.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyShoot05.png'), self.target_size)
        ]
        
        self.item_applied_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff01.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff02.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff03.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff04.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff05.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff06.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff07.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/CowboyBuff08.png'), self.target_size)
        ]
        
        self.attacking = False
        self.attack_index = 0
        self.attack_speed = 0.3
        self.attack_finished = False
        
        self.applied = False
        self.applied_index = 0
        self.applied_speed = 0.2
        self.applied_finished = False
        
        self.animation_index = 0
        self.animation_speed = 0.3
        self.character = self.idle[0] 
        self.image = self.character
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.x = int(x)
        self.y = int(y)
        self.velX = 0 
        self.velY = 0 
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        self.speed = 5
        self.gravity = 10
        self.jump_strength = 150
        self.still_on_ground = True
        self.ground_level = 550
        self.health_point = Healthpoint(hp)
        
    def draw(self, screen):
        screen.blit(self.character, (self.x, self.y))
        
    def draw_hp(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',40)
        hp_text = fonts.render(f'HP:{self.health_point.hp}',False,'Green')
        hp_rect = hp_text.get_rect(center=(self.x+35,self.y-20))
        screen.blit(hp_text, hp_rect)
        
    def gameover(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',80)
        gameover_text = fonts.render('Game Over',False,'Red')
        gameover_rect = gameover_text.get_rect(center=(self.rect.centerx, self.rect.centery)) #center the text at player's center
        screen.blit(gameover_text, gameover_rect)
        pygame.display.update()
        pygame.time.wait(1500)
        pygame.quit()
        exit()
        
    def attack(self):
        if not self.attacking:  
            self.attacking = True
            self.attack_index = 0
            self.attack_finished = False
            
    def item_applied(self):
        if not self.applied:
            self.applied = True
            self.applied_index = 0
            self.applied_finished = False
        
    def update(self, screen):
        self.velX = 0
        self.velY = 0
        
        if not self.health_point.still_alive():
            self.gameover(screen)
            
        if self.attacking:
            self.character = self.attack_frames[int(self.attack_index)]
            self.attack_index += self.attack_speed
            if self.attack_index >= len(self.attack_frames):
                self.attack_index = 0
                self.attacking = False
                self.attack_finished = True
                
        elif self.applied:
            self.character = self.item_applied_frames[int(self.applied_index)]
            self.applied_index += self.applied_speed
            if self.applied_index >= len(self.item_applied_frames):
                self.applied_index = 0
                self.applied = False
                self.applied_finished = True
                
        elif self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            self.character = self.left_frames[int(self.animation_index)]
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.left_frames):
                self.animation_index = 0
        elif self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            self.character = self.right_frames[int(self.animation_index)]
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.right_frames):
                self.animation_index = 0
        else:
            self.animation_index += self.animation_speed 
            if self.animation_index >= len(self.idle):  
                self.animation_index = 0  
            self.character = self.idle[int(self.animation_index)]
        
        # Jumping logic
        if self.space_pressed and self.still_on_ground:
            self.velY = -self.jump_strength
            self.still_on_ground = False
        if not self.still_on_ground:
            self.velY += self.gravity
        self.y += self.velY
        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.velY = 0
            self.still_on_ground = True
        
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