from math import ceil
from random import randint
import pygame


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.next = 'red'
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left: int, top: int, cell_size: int):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen: pygame.Surface):
        font = pygame.font.Font(None, self.cell_size - 7)
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    screen, 'white', (self.left + x * self.cell_size,
                                      self.top + y * self.cell_size,
                                      self.cell_size, self.cell_size), 1)
                cell = self.board[y][x]
                if cell == 10:
                    pygame.draw.rect(screen, 'red', (self.left + x * self.cell_size,
                                                     self.top + y * self.cell_size,
                                                     self.cell_size, self.cell_size), 0)
                elif cell != -1:
                    text = font.render(str(cell), True, 'green')
                    text_x = self.left + x * self.cell_size + 3
                    text_y = self.top + y * self.cell_size + 3
                    screen.blit(text, (text_x, text_y))

    def get_cell(self, mouse_pos: '(int, int)'):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        result_x = ceil(x / self.cell_size) - 1
        result_y = ceil(y / self.cell_size) - 1
        if result_x < 0 or result_x > self.width - 1 or result_y < 0 or result_y > self.height - 1:
            return None
        return result_y, result_x

    def get_click(self, mouse_pos: tuple[int, int]):
        cell_coords = self.get_cell(mouse_pos)
        if self.on_click and cell_coords:
            self.on_click(cell_coords)


class Minesweeper(Board):
    def __init__(self, width: int, height: int, mines_count: int):
        super().__init__(width, height)
        if mines_count >= width * height:
            self.board = [[10] * width for _ in range(height)]
        else:
            self.board = [[-1] * width for _ in range(height)]
            used = set()
            while len(used) < mines_count:
                x, y = randint(0, width - 1), randint(0, height - 1)
                used.add(f'{y}-{x}')
                self.board[y][x] = 10

    def open_cell(self, y: int, x: int, parentx: int | None = None, parenty: int | None = None):
        mines_around = 0
        left = x - 1 if x > 0 else None
        right = x + 1 if x < self.width - 1 else None
        top = y - 1 if y > 0 else None
        bottom = y + 1 if y < self.height - 1 else None
        if top is not None and left is not None and top is not None and left is not None and self.board[top][left] == 10:
            mines_around += 1
        if top is not None and self.board[top][x] == 10:
            mines_around += 1
        if top is not None and right is not None and self.board[top][right] == 10:
            mines_around += 1
        if right is not None and self.board[y][right] == 10:
            mines_around += 1
        if bottom is not None and right is not None and self.board[bottom][right] == 10:
            mines_around += 1
        if bottom and self.board[bottom][x] == 10:
            mines_around += 1
        if bottom is not None and left is not None and self.board[bottom][left] == 10:
            mines_around += 1
        if left is not None and self.board[y][left] == 10:
            mines_around += 1

        self.board[y][x] = mines_around
        if mines_around == 0:
            if top is not None and left is not None and self.board[top][left] == -1:
                self.open_cell(top, left)
            if top is not None and self.board[top][x] == -1:
                self.open_cell(top, x)
            if top is not None and right is not None and self.board[top][right] == -1:
                self.open_cell(top, right)
            if right is not None and self.board[y][right] == -1:
                self.open_cell(y, right)
            if bottom is not None and right is not None and self.board[bottom][right] == -1:
                self.open_cell(bottom, right)
            if bottom is not None and self.board[bottom][x] == -1:
                self.open_cell(bottom, x)
            if bottom is not None and left is not None and self.board[bottom][left] == -1:
                self.open_cell(bottom, left)
            if left is not None and self.board[y][left] == -1:
                self.open_cell(y, left)

    def on_click(self, cell_coords: tuple[int, int]):
        self.open_cell(*cell_coords)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Дедушка сапёра')
    size = width, height = 440, 440
    screen = pygame.display.set_mode(size)
    board = Minesweeper(10, 10, 10)
    board.set_view(20, 20, 40)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
        clock.tick(60)
