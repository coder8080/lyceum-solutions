import pygame

file = open('points.txt', 'rt', encoding='utf-8')
points = [[float(num.replace(',', '.')) for num in el[1:-1].split(';')]
          for el in file.readline().split(', ')]
print(points)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Zoom')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    is_running = True
    scaling_coef = 10
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEWHEEL:
                scaling_coef += event.y * 0.5
        screen.fill('black')
        half_width = width // 2
        half_height = height // 2
        last_point = points[0]
        for point in points[1:]:
            startx = last_point[0] * scaling_coef + half_width
            starty = last_point[1] * scaling_coef * -1 + half_height
            endx = point[0] * scaling_coef + half_width
            endy = point[1] * scaling_coef * -1 + half_height
            pygame.draw.line(
                screen, "white", (startx, starty), (endx, endy), 1)
            last_point = point

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
