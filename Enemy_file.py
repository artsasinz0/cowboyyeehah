import pygame

W = 100
H = 100

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,hp):
        super().__init__()
        
        self.enemy = pygame.image.load('img_graphic/test2.png')
        self.enemy = pygame.transform.scale(self.enemy,(W,H))
        
        self.rect = self.enemy.get_rect(topleft=(x,y))
        self.x = x
        self.y = y
        self.health_point = Healthpoint(hp)
    
    def draw(self, screen):
        screen.blit(self.enemy,(self.x,self.y))
        
    def take_dmg(self, dmg):
        self.health_point.take_dmg(dmg)
        if not self.health_point.still_alive():
            self.kill()
            print("Enemy defeated.") #check
            
class Healthpoint():
    def __init__(self,hp):
        self.hp = hp
        
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            
    def still_alive(self):
        return self.hp > 0 