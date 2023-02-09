from math import ceil
from random import randint
import pygame


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [['none'] * width for i in range(height)]
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
                color = self.board[y][x]
                if color != 'none':
                    pygame.draw.circle(
                        screen, color, (self.left + (x + 0.5) * self.cell_size,
                                        self.top + (y + 0.5) * self.cell_size), self.cell_size // 2 - 1, 0)
                pygame.draw.rect(
                    screen, 'white', (self.left + x * self.cell_size,
                                      self.top + y * self.cell_size,
                                      self.cell_size, self.cell_size), 1)

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
        if hasattr(self, 'on_click') and self.on_click and cell_coords:
            self.on_click(cell_coords)


class Lines(Board):
    def __init__(self, *args):
        super().__init__(*args)
        self.is_animating = False
        self.frame_duration = 6
        self.time_left = self.frame_duration
        self.current_animating_index = 0
        self.animating_points = []

    def has_path(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        levels = [[-1] * self.width for _ in range(self.height)]

        def handle_point(y: int, x: int, level: int = 0, current_path: list[tuple[int, int]] = []):
            levels[y][x] = current_path

            left = x - 1 if x > 0 else None
            right = x + 1 if x < self.width - 1 else None
            top = y - 1 if y > 0 else None
            bottom = y + 1 if y < self.height - 1 else None

            new_path = current_path + [(y, x)]
            if top is not None and self.board[top][x] == 'none' and (levels[top][x] == -1 or len(levels[top][x]) > level + 1):
                handle_point(top, x, level + 1, new_path)
            if right is not None and self.board[y][right] == 'none' and (levels[y][right] == -1 or len(levels[y][right]) > level + 1):
                handle_point(y, right, level + 1, new_path)
            if bottom is not None and self.board[bottom][x] == 'none' and (levels[bottom][x] == -1 or len(levels[bottom][x]) > level + 1):
                handle_point(bottom, x, level + 1, new_path)
            if left is not None and self.board[y][left] == 'none' and (levels[y][left] == -1 or len(levels[y][left]) > level + 1):
                handle_point(y, left, level + 1, new_path)
        handle_point(y1, x1)
        result = levels[y2][x2]
        return result if result != -1 else False

    def on_click(self, cell_coords: tuple[int, int]):
        if self.is_animating:
            return
        y, x = cell_coords
        current = self.board[y][x]
        if current == 'none':
            has_red = False
            red_coords = None
            for ty in range(self.height):
                if has_red:
                    break
                for tx in range(self.width):
                    if self.board[ty][tx] == 'red':
                        has_red = True
                        red_coords = tx, ty
                        break
            if not has_red:
                self.board[y][x] = 'blue'
            else:
                result = self.has_path(*red_coords, x, y)
                if result:
                    self.is_animating = True
                    self.time_left = self.frame_duration
                    self.animating_points = result + [(y, x)]
                    self.current_animating_index = 0

                    # self.board[red_coords[1]][red_coords[0]] = 'none'
                    # self.board[y][x] = 'blue'
        elif current == 'blue':
            self.board[y][x] = 'red'
        elif current == 'red':
            self.board[y][x] = 'blue'

    def tick(self):
        if not self.is_animating:
            return
        self.time_left -= 1
        if self.time_left <= 0:
            self.time_left = self.frame_duration
            y1, x1 = self.animating_points[self.current_animating_index]
            self.board[y1][x1] = 'none'
            self.current_animating_index += 1
            y, x = self.animating_points[self.current_animating_index]
            self.board[y][x] = 'red'
            if self.current_animating_index >= len(self.animating_points) - 1:
                self.board[y][x] = 'blue'
                self.is_animating = False


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Линеечки')
    size = width, height = 540, 540
    screen = pygame.display.set_mode(size)
    board = Lines(10, 10)
    board.set_view(20, 20, 50)
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
        screen.fill('black')
        board.render(screen)
        board.tick()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
