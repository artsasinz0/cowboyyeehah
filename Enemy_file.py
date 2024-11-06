import pygame

#size of enemy
W = 100
H = 100

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,hp):
        super().__init__()
        
        self.enemy = pygame.image.load('img_graphic/test2.png')
        self.enemy = pygame.transform.scale(self.enemy,(W,H))
        
        self.image = self.enemy
        self.rect = self.enemy.get_rect(topleft=(x,y))
        self.x = int(x)
        self.y = int(y)
        self.e_health_point = E_Healthpoint(hp)
    
    def draw(self, screen):
        screen.blit(self.enemy,(self.x,self.y))
        
    def draw_hp(self,screen):
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',35)
        hp_text = fonts.render(f'HP: {self.e_health_point.hp}',False,'Red')
        hp_rect = hp_text.get_rect(center=(self.x+W,self.y+50)) 
        screen.blit(hp_text, hp_rect)
        
    def take_dmg(self, dmg):
        self.e_health_point.take_dmg(dmg)
        if not self.e_health_point.still_alive():
            self.kill()
            # print("Enemy defeated.") #check
            
class E_Healthpoint():
    def __init__(self,hp):
        self.hp = hp
        
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            
    def still_alive(self):
        return self.hp > 0 