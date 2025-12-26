import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))

player = pygame.Rect(280, 180, 40, 40)

enemies = []
for i in range(7):
    enemies.append(pygame.Rect(random.randint(0, 560), random.randint(0, 360), 30, 30))

score = 0
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 560)
            enemy.y = random.randint(0, 360)

    pygame.draw.rect(screen, (0, 0, 255), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()