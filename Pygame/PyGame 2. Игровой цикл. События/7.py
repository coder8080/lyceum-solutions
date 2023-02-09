import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Прямоугольники с Ctrl+Z')
    size = width, height = 500, 400
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    rects = []
    start_x = 0
    start_y = 0
    is_dragging = False
    current_layer = None
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = event.pos
                is_dragging = True
                current_layer = pygame.Surface(screen.get_size())
            elif event.type == pygame.MOUSEMOTION:
                if not is_dragging:
                    continue
                current_layer = pygame.Surface(screen.get_size())
                x, y = event.pos
                pygame.draw.rect(current_layer, 'white',
                                 (start_x, start_y, x - start_x, y - start_y), 3, 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos

                is_dragging = False
                rects.append((start_x, start_y, x - start_x, y - start_y))
                current_layer = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if len(rects) > 0:
                        rects = rects[:-1]
        screen.fill('black')
        if current_layer:
            screen.blit(current_layer, (0, 0))
        for rect in rects:
            pygame.draw.rect(screen, 'white',
                             rect, 3, 3)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
