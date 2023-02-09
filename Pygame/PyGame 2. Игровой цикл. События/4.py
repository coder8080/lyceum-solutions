import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Я слежу за тобой!")
    count = 1
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.WINDOWHIDDEN:
                count += 1
        screen.fill('black')
        font = pygame.font.Font(None, 100)
        text = font.render(str(count), True, 'red')
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
