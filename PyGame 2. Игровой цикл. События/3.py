import pygame

if __name__ == '__main__':
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    is_grabbed = False
    square_x = 0
    square_y = 0
    delta_x = 0
    delta_y = 0
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = event.pos
                delta_x = posx - square_x
                delta_y = posy - square_y
                if delta_x > - 0 and delta_x <= 100 and delta_x >= 0 and delta_y <= 100:
                    is_grabbed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                is_grabbed = False
            elif event.type == pygame.MOUSEMOTION:
                if not is_grabbed:
                    continue
                posx, posy = event.pos
                square_x = posx - delta_x
                square_y = posy - delta_y
        screen.fill('black')
        pygame.draw.rect(screen, 'green', (square_x, square_y, 100, 100), 0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
