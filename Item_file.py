import pygame

#size of item.png
W = 70
H = 70

#png
item_img = pygame.image.load('img_graphic/gow.png')
# item_img = pygame.transform.scale(item_img,(W,H))

class Item(pygame.sprite.Sprite):
    def __init__(self,name,x,y,value,req):
        super().__init__()
        self.item_img = item_img
        self.rect = self.item_img.get_rect(topleft=(x, y))
        self.name = name
        self.x = x
        self.y = y
        self.value = value
        self.req = req
        
    def requirement(self,player):
        return player.health_point.hp >= self.req
        
    def apply_item(self,player):
        player.health_point.hp += self.value
    
    def draw(self,screen):
        screen.blit(item_img,(self.x,self.y))
        fonts = pygame.font.Font('fonts/Pixeltype.ttf',30)
        req_text = fonts.render(f'Requirement:{self.req} | Got hp:{self.value}',False,'Red')
        req_rect = req_text.get_rect(center=(self.x+30 ,self.y - 10))
        screen.blit(req_text, req_rect)
        
    
        