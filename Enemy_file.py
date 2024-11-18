from typing import Any
import pygame

#size of enemy
W = 48
H = 64

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()

        self.target_size = (W, H)
        
        # Load idle frames
        self.enemy_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/BossIdle01.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/BossIdle02.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/BossIdle03.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/BossIdle04.png'), self.target_size),
        ]
        
        # Load death frames
        self.enemy_dead_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/die1.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/die2.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/die3.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/die4.png'), self.target_size),
        ]
        
        self.dying = False
        self.died_index = 0
        self.died_speed = 0.3
        
        self.animation_index = 0
        self.animation_speed = 0.1
        
        self.enemy = self.enemy_frames[0]  # Initial frame
        self.image = self.enemy
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = int(x)
        self.y = int(y)
        self.e_health_point = E_Healthpoint(hp)
        self.defeat_time = None

    def draw(self, screen):
        screen.blit(self.enemy, (self.x, self.y))

    def draw_hp(self, screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf', 35)
        hp_text = fonts.render(f'HP: {self.e_health_point.hp}', False, 'Red')
        hp_rect = hp_text.get_rect(center=(self.x+27, self.y-15))
        screen.blit(hp_text, hp_rect)

    def take_dmg(self, dmg):
        self.e_health_point.take_dmg(dmg)
        if not self.e_health_point.still_alive():
            self.dying = True
    
    def update(self):
        if self.dying:
            self.enemy = self.enemy_frames[int(self.died_index)]
            self.died_index += self.died_speed
            if self.died_index >= len(self.enemy_dead_frames):
                self.died_index = 0 
        elif not self.dying:
            self.enemy = self.enemy_frames[int(self.animation_index)]
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.enemy_frames):
                self.animation_index = 0 


class Enemy01(pygame.sprite.Sprite):
    def __init__(self,x,y,hp):
        super().__init__()
        
        self.target_size = (W,H)
        
        self.enemy_frames = [
            pygame.transform.scale(pygame.image.load('img_graphic/w_left1.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/w_left2.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/w_left3.png'), self.target_size),
            pygame.transform.scale(pygame.image.load('img_graphic/w_left4.png'), self.target_size),
        ]
        
        self.dead = False
        self.animation_index = 0
        self.animation_speed = 0.1
        self.enemy = self.enemy_frames[0]
        self.image = self.enemy
        self.rect = self.image.get_rect(topleft=(x,y))
        self.x = int(x)
        self.y = int(y)
        self.e_health_point = E_Healthpoint(hp)
        self.defeat_time = None
    
    def draw(self, screen):
        screen.blit(self.enemy,(self.x,self.y))
        
    def draw_hp(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',35)
        hp_text = fonts.render(f'HP: {self.e_health_point.hp}',False,'Red')
        hp_rect = hp_text.get_rect(center=(self.x,self.y)) 
        screen.blit(hp_text, hp_rect)
        
    def take_dmg(self, dmg):
        self.e_health_point.take_dmg(dmg)
        if not self.e_health_point.still_alive():
            self.kill()

    def update(self):
        self.enemy = self.enemy_frames[int(self.animation_index)]
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.enemy_frames):
            self.animation_index = 0

    
class E_Healthpoint():
    def __init__(self,hp):
        self.hp = hp
        
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            
    def still_alive(self):
        return self.hp > 0 