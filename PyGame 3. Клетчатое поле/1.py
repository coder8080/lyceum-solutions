import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen: pygame.Surface):
        white = pygame.Color('white')
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    screen, white, (self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size), 1)


if __name__ == '__main__':
    size = width, height = 400, 500
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    board.set_view(40, 40, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
