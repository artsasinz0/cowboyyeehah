class Castal(pygame.sprite.Sprite):
    """ Castle platform the user can jump on """

    def __init__(self, width, height):
        """ Castle constructor. """

        super().__init__()

        # เปลี่ยนเป็นการโหลดรูปภาพแทนการสร้าง Surface
        self.image = pygame.image.load("castle.png").convert_alpha()  # โหลดรูป "castle.png" (คุณต้องใส่รูปไว้ในโฟลเดอร์เดียวกับโค้ดหรือระบุ path)
        
        # ปรับขนาดรูปให้ตรงกับ width และ height ที่ส่งเข้ามา
        self.image = pygame.transform.scale(self.image, (width, height))

        # กำหนดขอบเขตของ Castle
        self.rect = self.image.get_rect()


