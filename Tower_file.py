class Tower:
    def __init__(self, tower_id, enemies, items=None, position_x=0):
        self.tower_id = tower_id
        self.enemies = enemies
        self.items = items if items is not None else []
        self.position_x = position_x
    
    def is_cleared(self):
        return all(not enemy.e_health_point.still_alive() for enemy in self.enemies)
    
    def draw(self, screen):
        # Draw each enemy in the tower
        for enemy in self.enemies:
            enemy.draw(screen)  # Assuming your Enemy class has a draw method
        
        # Draw each item in the tower
        for item in self.items:
            item.draw(screen)
            
    def get_all_objects(self):
        # Combine enemies and items into one list
        return self.enemies + self.items