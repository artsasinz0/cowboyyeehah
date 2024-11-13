class Level_01(Level):

    def __init__(self, player):

        Level.__init__(self, player)
        
        self.level_limit = -1500
        
        #Array with width, hight, x, y of castle
        level = [[210, 70, 500, 500],[],[] ] #position castal
        
        #Go though the array above and add castal
        for castle in level:
            block = Castle(castle[0],castle[1])
            block.rest.x = castle[2]
            block.rest.y = castle[3]
            block.player = self.player
            self.castle_list.add(block)

class Level_02(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Level-specific properties
        self.level_limit = -2000
        
        # Array with width, height, x, y of castles for Level 2
        level = [
            [150, 50, 300, 450],
            [100, 30, 700, 350],
            [180, 60, 1100, 250],
            [90, 40, 1500, 200]
        ]
        
        # Go through the array and add castles
        for castle in level:
            block = Castle(castle[0], castle[1])
            block.rect.x = castle[2]
            block.rect.y = castle[3]
            block.player = self.player
            self.castle_list.add(block)


class Level_03(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Level-specific properties
        self.level_limit = -2500
        
        # Array with width, height, x, y of castles for Level 3
        level = [
            [200, 60, 400, 500],
            [120, 40, 900, 350],
            [160, 70, 1300, 300],
            [100, 50, 1700, 150]
        ]
        
        # Go through the array and add castles
        for castle in level:
            block = Castle(castle[0], castle[1])
            block.rect.x = castle[2]
            block.rect.y = castle[3]
            block.player = self.player
            self.castle_list.add(block)