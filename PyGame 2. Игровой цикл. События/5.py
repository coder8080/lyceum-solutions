import pygame
from random import randint

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('К щелчку')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    is_running = True
    circle_x = 250
    circle_y = 250
    is_going = False
    speed = 1
    aim_x = 0
    aim_y = 0
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                aim_x = x
                aim_y = y
                is_going = True
                speed = randint(2, 10)
        if is_going:
            x_diff = abs(aim_x - circle_x)
            if x_diff <= speed:
                circle_x = aim_x
            else:
                if circle_x < aim_x:
                    circle_x += speed
                elif circle_x > aim_x:
                    circle_x -= speed

            y_diff = abs(aim_y - circle_y)
            if y_diff <= speed:
                circle_y = aim_y
            else:
                if circle_y < aim_y:
                    circle_y += speed
                elif circle_y > aim_y:
                    circle_y -= speed
        screen.fill('black')
        pygame.draw.circle(screen, 'red', (circle_x, circle_y), 20, 0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
