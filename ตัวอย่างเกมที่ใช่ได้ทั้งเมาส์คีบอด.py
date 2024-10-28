import pygame
import sys

# เริ่มต้น Pygame
pygame.init()

# ตั้งค่าหน้าจอ
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Addition Game")

# กำหนดสี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# กำหนดฟอนต์
font = pygame.font.Font(None, 50)

# ค่าคงที่สำหรับแต่ละระดับ
levels = {
    1: (3, 2, 11),   # ระดับ 1: (B, C, D)
    2: (16, 19, 51), # ระดับ 2: (B, C, D)
    3: (86, 99, 200)  # ระดับ 3: (B, C, D)
}

# ฟังก์ชันสำหรับรีเซ็ตเกม
def reset_game(level):
    global option_b, option_c, option_d, game_over, message, selected_options, selected_option_index
    option_b, option_c, option_d = levels[level]  # ดึงค่าจาก dictionary levels
    game_over = False
    message = ""
    selected_options = []  # ใช้ติดตามตัวเลือกที่เลือก
    selected_option_index = None  # ดัชนีของตัวเลือกที่ถูกเลือกในขณะนี้

# การตั้งค่าเริ่มต้นของเกม
number_a = 10  # ตั้งค่าเริ่มต้นของ A เป็น 10
level = 1
reset_game(level)
next_level = False  # ใช้ติดตามว่าผู้เล่นพร้อมไปยังระดับถัดไปหรือไม่
next_count = 0  # นับจำนวนครั้งที่ผู้เล่นไปถึงระดับถัดไป
running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # ตรวจสอบการคลิกเมาส์ที่ตัวเลือก
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # ตัวเลือก B
            if 'B' not in selected_options and option_b_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_b:  # ตรวจสอบว่า A มีค่ามากกว่าหรือเท่ากับ
                    selected_options.append('B')
                    number_a += option_b  # เพิ่มค่าให้กับ number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # สิ้นสุดเกม

            # ตัวเลือก C
            elif 'C' not in selected_options and option_c_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_c:  # ตรวจสอบว่า A มีค่ามากกว่าหรือเท่ากับ
                    selected_options.append('C')
                    number_a += option_c  # เพิ่มค่าให้กับ number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # สิ้นสุดเกม

            # ตัวเลือก D
            elif 'D' not in selected_options and option_d_rect.collidepoint(mouse_x, mouse_y):
                if number_a >= option_d:  # ตรวจสอบว่า A มีค่ามากกว่าหรือเท่ากับ
                    selected_options.append('D')
                    number_a += option_d  # เพิ่มค่าให้กับ number_a
                else:
                    message = "Game Over! Press R to Restart."
                    game_over = True  # สิ้นสุดเกม

            # ตรวจสอบเงื่อนไขการชนะ
            if len(selected_options) == 3 and not game_over:
                next_count += 1  # เพิ่มตัวนับระดับถัดไป
                if next_count == 3:  # ชนะเมื่อผ่าน 3 ระดับ
                    message = "Win! Press R to Restart."
                    game_over = True  # สิ้นสุดเกม
                else:
                    message = "Next! Click to proceed to the next level."
                    next_level = True  # ตั้งค่าสำหรับให้ผู้เล่นไปยังระดับถัดไป

        # ตรวจสอบการคลิกสำหรับระดับถัดไป
        if next_level and event.type == pygame.MOUSEBUTTONDOWN:
            level += 1  # เพิ่มระดับใหม่สำหรับค่าที่กำหนด
            if level <= len(levels):
                reset_game(level)  # สร้างหมายเลขใหม่สำหรับระดับถัดไป
            next_level = False  # รีเซ็ตธงระดับถัดไป

        # ตรวจสอบการกดปุ่มเพื่อรีสตาร์ท
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # ตรวจสอบว่ากด R หรือไม่
                number_a = 10  # รีเซ็ต A เป็น 10
                level = 1  # รีเซ็ตระดับเป็น 1
                reset_game(level)  # รีเซ็ตเกม
                next_count = 0  # รีเซ็ตตัวนับระดับถัดไป
                message = ""  # เคลียร์ข้อความ
                game_over = False  # รีเซ็ตธงเกมโอเวอร์

        # ตรวจสอบการเลือกด้วยคีย์บอร์ด
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:  # เลือกตัวเลือก B
                selected_option_index = 0
            elif keys[pygame.K_2]:  # เลือกตัวเลือก C
                selected_option_index = 1
            elif keys[pygame.K_3]:  # เลือกตัวเลือก D
                selected_option_index = 2
            
            if keys[pygame.K_x] and selected_option_index is not None:
                if selected_option_index == 0 and 'B' not in selected_options:
                    if number_a >= option_b:
                        selected_options.append('B')
                        number_a += option_b
                    else:
                        message = "Game Over! Press R to Restart."
                        game_over = True
                elif selected_option_index == 1 and 'C' not in selected_options:
                    if number_a >= option_c:
                        selected_options.append('C')
                        number_a += option_c
                    else:
                        message = "Game Over! Press R to Restart."
                        game_over = True
                elif selected_option_index == 2 and 'D' not in selected_options:
                    if number_a >= option_d:
                        selected_options.append('D')
                        number_a += option_d
                    else:
                        message = "Game Over! Press R to Restart."
                        game_over = True

                # ตรวจสอบเงื่อนไขการชนะ
                if len(selected_options) == 3 and not game_over:
                    next_count += 1
                    if next_count == 3:
                        message = "Win! Press R to Restart."
                        game_over = True
                    else:
                        message = "Next! Click to proceed to the next level."
                        next_level = True

    # แสดงหมายเลขและตัวเลือก
    number_a_text = font.render(f"A: {number_a}", True, BLACK)
    message_text = font.render(message, True, RED if game_over else BLACK)

    screen.blit(number_a_text, (50, HEIGHT // 4))  # ย้าย A ไปที่ด้านซ้าย

    # แสดงตัวเลือกทั้งหมด โดยซ่อนตัวเลือกที่เลือกแล้ว
    if 'B' not in selected_options:
        option_b_text = font.render(f"B: {option_b}", True, GREEN)
        option_b_rect = screen.blit(option_b_text, (WIDTH // 4, HEIGHT // 2))
        if selected_option_index == 0:
            pygame.draw.rect(screen, YELLOW, option_b_rect.inflate(20, 20), 3)

    if 'C' not in selected_options:
        option_c_text = font.render(f"C: {option_c}", True, GREEN)
        option_c_rect = screen.blit(option_c_text, (WIDTH // 2 - 50, HEIGHT // 2))
        if selected_option_index == 1:
            pygame.draw.rect(screen, YELLOW, option_c_rect.inflate(20, 20), 3)

    if 'D' not in selected_options:
        option_d_text = font.render(f"D: {option_d}", True, GREEN)
        option_d_rect = screen.blit(option_d_text, (3 * WIDTH // 4 - 50, HEIGHT // 2))
        if selected_option_index == 2:
            pygame.draw.rect(screen, YELLOW, option_d_rect.inflate(20, 20), 3)

    # แสดงข้อความสำหรับการไปยังระดับถัดไปหรือการรีสตาร์ท
    if next_level or game_over:
        screen.blit(message_text, (WIDTH // 2 - 250, 3 * HEIGHT // 4))
    else:
        screen.blit(message_text, (WIDTH // 2 - 150, 3 * HEIGHT // 4))

    pygame.display.flip()

# ปิด Pygame
pygame.quit()
sys.exit()
