#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Level(object):
    def __init__(self,player):
        self.castel_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.player = player
        
        #Background image
        self.background = None
        
        #how far for L/R
        self.world_shift = 0
        self.level_limit = -100
        
    def update(self):
        """Update everything on this level"""
        self.castal_list.update()
        self.enemy_list.update()
        self.item_list.update()
    
    def draw(self, screen):
        """Draw everything on this level"""
        # Draw the background
        screen.fill()#change image
        
        #Draw all the sprite lists that we have
        self.castal_list.draw(screen)
        self.enemy_list.draw(screen)
        self.item_list.draw(screen)
        
    def shift_world(self, shift_x):
        """When move to L/R & scroll everything"""
        #Keep track of the shift amount
        self.word_shift += shift_x
        
        #Go throught all th sprite lists and shift
        for castal in self.castal_list:
            castal.rect.x += shift_x
            
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        
        for item in self.item_list:
            item.rect.x += shift_x
    
        
         


# In[ ]:


class Level_01(Level):
    def __init__(self, player):
        Level.(self, player)
        
        self.level_limit = -1500
        
        #Array with width, hight, x, y of castal
        level = [[210, 70, 500, 500],[],[] ] #position castal
        
        #Go though the array above and add castal
        for castal in level:
            block = Castal(castal[0],castal[1])
            block.rest.x = castal[2]
            block.rest.y = castal[3]
            block.player = self.player
            
            
            
        


# In[ ]:




