import pygame
from random import randint

speed = 100 / 60
plus = ((speed ** 2) / 2) ** 0.5


class Circle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.direction = 0
        self.window_width = width
        self.window_height = height

    def update_coords(self):
        if self.direction == 0:
            self.x -= plus
            self.y -= plus
        elif self.direction == 1:
            self.x -= plus
            self.y += plus
        elif self.direction == 2:
            self.x += plus
            self.y += plus
        elif self.direction == 3:
            self.x += plus
            self.y -= plus

    def draw(self, screen: pygame.Surface):
        x1, y1 = self.x - 10, self.y - 10
        if x1 < 0:
            if self.direction == 0:
                self.direction = 3
            elif self.direction == 1:
                self.direction = 2
        if y1 < 0:
            if self.direction == 0:
                self.direction = 1
            elif self.direction == 3:
                self.direction = 2
        if x1 + 20 > self.window_width:
            if self.direction == 3:
                self.direction = 0
            elif self.direction == 2:
                self.direction = 1
        if y1 + 20 > self.window_height:
            if self.direction == 1:
                self.direction = 0
            elif self.direction == 2:
                self.direction = 3
        self.update_coords()
        pygame.draw.circle(screen, 'white', (self.x, self.y), 10, 0)


circles = []

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = randint(300, 500), randint(300, 500)
    screen = pygame.display.set_mode(size)
    finished = False
    clock = pygame.time.Clock()
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circles.append(Circle(*event.pos, width, height))
        screen.fill((0, 0, 0))
        for circle in circles:
            circle.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
