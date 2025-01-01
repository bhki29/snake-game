import pygame
import random

# Inisialisasi pygame
pygame.init()

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Dimensi layar
width = 800
height = 600

# Membuat layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Ular')

# Kecepatan ular
clock = pygame.time.Clock()
initial_snake_speed = 15

# Ukuran blok ular
block_size = 10

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_display(score):
    value = score_font.render("Skor: " + str(score), True, green)
    screen.blit(value, [10, 10])

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])

def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    msg_rect = msg_surface.get_rect(center=(width // 2, height // 3))
    screen.blit(msg_surface, msg_rect)

def gameLoop():
    snake_speed = initial_snake_speed  # Kecepatan awal ular
    game_over = False

    while True:  # Loop utama permainan
        game_close = False

        x1 = width / 2
        y1 = height / 2
        x1_change = 0
        y1_change = 0
        snake_list = []
        length_of_snake = 1
        foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

        while not game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -block_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = block_size
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -block_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        y1_change = block_size
                        x1_change = 0

            # Cek tabrakan dengan batas layar
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            screen.fill(white)
            pygame.draw.rect(screen, green, [foodx, foody, block_size, block_size])
            snake_head = [x1, y1]
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Cek tabrakan kepala dengan tubuh
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True

            snake(block_size, snake_list)
            score_display(length_of_snake - 1)

            pygame.display.update()

            # Cek jika makanan dimakan
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
                foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
                length_of_snake += 1
                snake_speed += 0.5  # Tambah kecepatan tiap kali ular makan

            clock.tick(snake_speed)

        # Tampilkan layar kalah
        screen.fill(blue)
        message("Kalah! Tekan C untuk main lagi atau Q untuk keluar", red)
        score_display(length_of_snake - 1)
        pygame.display.update()

        while True:  # Tunggu input untuk restart/keluar
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        break  # Keluar dari loop dan restart game
            else:
                continue
            break

gameLoop()
