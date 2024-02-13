import pygame
import sys
import random

# Константи
SIZE_BLOKS = 20 # Розмір блоку
FRAME_COLOR = [0, 255, 204] # Колір фрейму
WHITE = (255, 255, 255) # Білий колір
BLUE = (204, 255, 255) # Блакитний колір
RED = (224, 0, 0) # Червоний колір
HEADER_COLOR = (0, 204, 153) # Колір заголовка
SNAKE_COLOR = (0, 102, 0) # Колір змійки
COUNT_BLOCKS = 20 # Кількість блоків в рядку / стовпці
HEADER_MARGIN = 70 # Висота заголовка
MARGIN = 1 # Відступ між блоками

# Розмір екрану
size = [SIZE_BLOKS * COUNT_BLOCKS + 2 * SIZE_BLOKS + MARGIN * COUNT_BLOCKS,
        SIZE_BLOKS * COUNT_BLOCKS + 2 * SIZE_BLOKS + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

# Ініціалізація Pygame
pygame.init()

# Створення екрану
screen = pygame.display.set_mode(size)

# Встановлення заголовка вікна
pygame.display.set_caption('Snake_Game')

# Створення таймера
timer = pygame.time.Clock()

# Звук, який грає після того, як змійка з'їсть яблуко
apple_eat = pygame.mixer.Sound('poedanie-ukus-yabloka.wav')

# Звук, який грає, коли гра закінчена
game_over_sound = pygame.mixer.Sound('zvuk-game-over-4158.wav')

# Створення шрифту
font = pygame.font.SysFont(None, 48)

# Завантаження зображення яблука
apple_img = pygame.image.load('apple.png')

# Зміна розміру зображення яблука
apple_img = pygame.transform.scale(apple_img, (SIZE_BLOKS * 2, SIZE_BLOKS * 2))

# Функція, яка повертає блок з координатами (x, y)
def snake_block(x,y):
    return [x, y]

# Функція, яка перевіряє, чи знаходиться блок всередині границь екрану
def is_inside(head):
    return 0 <= head[0] < SIZE_BLOKS and 0 <= head[1] < SIZE_BLOKS

def get_random_block():
    # Вибираємо випадкову порожню клітину
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = snake_block(x, y)
    # Перевіряємо, чи вибрана клітинка не належить вже змійці
    while empty_block in snake_blocks:
        empty_block[0] = random.randint(0, COUNT_BLOCKS - 1)
        empty_block[1] = random.randint(0, COUNT_BLOCKS - 1)
    # Повертаємо вибрану порожню клітинку
    return empty_block


def draw_block(color, row, column, what):
    # Малюємо блок або яблуко в залежності від параметру what
    if what == 'block':
        pygame.draw.rect(screen, color, [SIZE_BLOKS + column * SIZE_BLOKS
                                         + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOKS +
                                         row * SIZE_BLOKS + MARGIN * (row + 1),
                                     SIZE_BLOKS, SIZE_BLOKS])
    else:
        screen.blit(apple_img, [SIZE_BLOKS + column * SIZE_BLOKS +
                                MARGIN * (column + 1) - SIZE_BLOKS * 0.5,
                            HEADER_MARGIN + SIZE_BLOKS + row * SIZE_BLOKS
                                + MARGIN * (row + 1) - SIZE_BLOKS * 0.5])


snake_blocks = [snake_block(9, 8),snake_block(9, 9), snake_block(9, 10)]
apple = get_random_block()

d_row = 0
d_col = 1
total = 0
speed = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Виходимо з гри
            print('exit')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Змінюємо напрямок руху змійки в залежності від натиснутої клавіші
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    # формуємо текст для виведення на екран
    text_t = "Total: " + str(total)
    text_s = "Speed: " + str(speed)

    # створюємо об'єкти тексту із шрифтом та кольором
    text_total = font.render(text_t, True, WHITE)
    text_speed = font.render(text_s, True, WHITE)

    # виводимо текст на екран
    screen.blit(text_total, (SIZE_BLOKS, SIZE_BLOKS))
    screen.blit(text_speed, (SIZE_BLOKS + 230, SIZE_BLOKS))

    # робимо прохід по всіх блоках, щоб відобразити їх на екрані
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            # викликаємо функцію, що малює блок
            draw_block(color, row, column, 'block')

    # отримуємо голову змії
    head = snake_blocks[-1]

    # перевіряємо, чи зіткнулася голова змії зі своїм тілом
    if head in snake_blocks[:-1]:
        print("YYYPPS")
        pygame.quit()
        sys.exit()

    # перевіряємо, чи голова змії виходить за межі гри
    if not is_inside(head):
        game_over_sound.play()
        pygame.time.wait(3000)
        print('crash')
        pygame.quit()
        sys.exit()

    # малюємо яблуко на екрані
    draw_block(RED, apple[0], apple[1], 'apple')

    # малюємо блоки змії на екрані
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block[0], block[1], 'block')

    # перевіряємо, чи змія з'їла яблуко
    if apple == head:
        apple_eat.play()
        total += 1
        speed = total // 5 + 1
        snake_blocks.insert(0, apple)
        apple = get_random_block()

    # створюємо нову голову змії
    new_head = snake_block(head[0] + d_row, head[1] + d_col)

    # додаємо нову голову до кінця списку блоків змії
    snake_blocks.append(new_head)

    # видаляємо блок з хвоста змії
    snake_blocks.pop(0)

    # оновлюємо екран
    pygame.display.flip()

    # задаємо частоту оновлення екрану залежно від швидкості гри
    timer.tick(3 + speed)
