import pygame
from math import sin, cos, pi

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Вентилятор')
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    is_running = True
    rotate_angle = 360 - 15
    speed = 0
    fps = 60
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    speed += 50
                elif event.button == 1:
                    speed -= 50
        points = list()
        for k in range(1, 13):
            points.append(
                (
                    int(cos((2 * pi * (k + rotate_angle / 30)) / 12) * 70 + 100),
                    int(sin(2 * pi * (k + rotate_angle / 30) / 12) * 70 + 100)
                )
            )
        rotate_angle += speed / fps
        while rotate_angle < 0:
            rotate_angle += 360
        while rotate_angle >= 360:
            rotate_angle %= 360
        screen.fill('black')
        pygame.draw.polygon(
            screen, 'white', ((100, 100), points[0], points[1]))
        pygame.draw.polygon(
            screen, 'white', ((100, 100), points[4], points[5]))
        pygame.draw.polygon(
            screen, 'white', ((100, 100), points[8], points[9]))
        pygame.draw.circle(screen, 'white', (100, 100), 10)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
