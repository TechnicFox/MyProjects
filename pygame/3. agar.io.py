import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Параметри вікна
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Полювання за об\'єктами')

# Кольори
white = (255, 255, 255)
red = (255, 0, 0)

# Параметри гравця і їжі
player_radius = 20
food_radius = 10

# Початкові координати гравця
player_x, player_y = window_width // 2, window_height // 2


# Функція для створення нової їжі на екрані
def spawn_food():
    return random.randint(food_radius, window_width - food_radius), random.randint(food_radius,
                                                                                   window_height - food_radius)


# Початкова їжа
food_x, food_y = spawn_food()

# Основний цикл гри
clock = pygame.time.Clock()
score = 0
running = True

while running:
    window.fill(white)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання координат миші
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Рух гравця до миші
    dx = mouse_x - player_x
    dy = mouse_y - player_y
    player_x += dx * 0.1
    player_y += dy * 0.1

    # Малювання гравця
    pygame.draw.circle(window, red, (int(player_x), int(player_y)), player_radius)

    # Малювання їжі
    pygame.draw.circle(window, red, (food_x, food_y), food_radius)

    # Перевірка колізії з їжею
    distance = ((player_x - food_x) ** 2 + (player_y - food_y) ** 2) ** 0.5
    if distance < player_radius + food_radius:
        # Якщо гравець зіткнувся з їжею, створюємо нову їжу та збільшуємо рахунок
        food_x, food_y = spawn_food()
        score += 1

        player_radius += 1

    # Вивід рахунку на екран
    font = pygame.font.Font(None, 36)
    text = font.render(f'Рахунок: {score}', True, red)
    window.blit(text, (10, 10))

    # Оновлення екрану
    pygame.display.update()

    # Обмеження кількості кадрів в секунду
    clock.tick(60)

# Завершення Pygame
pygame.quit()
