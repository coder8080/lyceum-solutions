from math import ceil
import pygame
from random import choice


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[choice(['red', 'blue'])
                       for j in range(width)] for i in range(height)]
        self.next = 'red'
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen: pygame.Surface):

        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    screen, 'white', (self.left + x * self.cell_size,
                                      self.top + y * self.cell_size,
                                      self.cell_size, self.cell_size), 1)
                color = self.board[y][x]
                if color == 'red':
                    pygame.draw.circle(screen, 'red', (int(
                        self.left + (x + 0.5) * self.cell_size),
                        int(self.top + (y + 0.5) * self.cell_size)), (self.cell_size // 2) - 4, 0)
                elif color == 'blue':
                    pygame.draw.circle(screen, 'blue', (int(
                        self.left + (x + 0.5) * self.cell_size),
                        int(self.top + (y + 0.5) * self.cell_size)), (self.cell_size // 2) - 4, 0)
                else:
                    print('unknown color')

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        result_x = ceil(x / self.cell_size) - 1
        result_y = ceil(y / self.cell_size) - 1
        if result_x < 0 or result_x > self.width - 1 or result_y < 0 or result_y > self.height - 1:
            return None
        return result_y, result_x

    def on_click(self, cell_coords):
        if cell_coords is None:
            return
        y, x = cell_coords
        for y1 in range(self.height):
            self.board[y1][x] = self.next
        for x1 in range(self.width):
            self.board[y][x1] = self.next
        self.next = 'blue' if self.next == 'red' else 'red'

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        self.on_click(cell_coords)


if __name__ == '__main__':
    try:
        n = int(input())
        side_size = 50 * n + 100
        size = side_size, side_size
        screen = pygame.display.set_mode(size)
        board = Board(n, n)
        board.set_view(50, 50, 50)
        running = True
        pygame.display.set_caption('Недореверси')
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
            screen.fill((0, 0, 0))
            board.render(screen)
            pygame.display.flip()
    except ValueError:
        print('Неверный формат ввода')
