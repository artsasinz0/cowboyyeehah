import pygame

#size of item.png
W = 50
H = 50

#png
item_img = pygame.image.load('img_graphic/gow.png')
item_img = pygame.transform.scale(item_img,(W,H))

class Item(pygame.sprite.Sprite):
    def __init__(self,name,x,y,value,effect_type):
        super().__init__()
        self.image = item_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name
        self.x = x
        self.y = y
        self.value = value
        self.effect_type = effect_type
        
    def apply_item(self,player):
        if self.effect_type == "add":
            player.health_point.hp += self.value
        elif self.effect_type == "multi":
            player.health_point.hp *= self.value
            player.health_point.hp = int(player.health_point.hp)
        elif self.effect_type == "div":
            player.health_point.hp //= self.value
        if player.health_point.hp < 0:
            player.health_point.hp = 0
            
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',35)
        if self.effect_type == 'add':
            req_text = fonts.render(f'+ {self.value}',False,'Red')
        elif self.effect_type == 'multi':
            req_text = fonts.render(f'x {self.value}',False,'Red')
        elif self.effect_type == 'div':
            req_text = fonts.render(f'/ {self.value}',False,'Red')
        req_rect = req_text.get_rect(center=(self.x+25 ,self.y - 15))
        screen.blit(req_text, req_rect)
        
    
        