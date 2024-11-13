class Level(object):
    def __init__(self,player):
        self.castle_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.player = player
        
        #Background image
        self.background = None
        
        #how far for L/R
        self.world_shift = 0
        self.level_limit = -1000
        
    def update(self):
        """Update everything on this level"""
        self.castle_list.update()
        self.enemy_list.update()
        self.item_list.update()
    
    def draw(self, screen):
        """Draw everything on this level"""
        # Draw the background
        screen.fill()#change image
        
        #Draw all the sprite lists that we have
        self.castle_list.draw(screen)
        self.enemy_list.draw(screen)
        self.item_list.draw(screen)
        
    def shift_world(self, shift_x):
        """When move to L/R & scroll everything"""
        #Keep track of the shift amount
        self.word_shift += shift_x
        
        #Go throught all th sprite lists and shift
        for castle in self.castle_list:
            castle.rect.x += shift_x
            
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        
        for item in self.item_list:
            item.rect.x += shift_x




