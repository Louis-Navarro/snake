import random

import pygame as pg

###########
# CLASSES #
###########


class Snake:
    def __init__(self, x, y, size, s_dir='right'):
        self.pos = [[x, y]]
        self.size = size
        self.dir = s_dir

    def move_tail(self):
        for pos_index in range(1, len(self.pos))[::-1]:
            self.pos[pos_index] = self.pos[pos_index - 1].copy()

    def change_dir(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.dir = 'right'
        elif keys[pg.K_LEFT]:
            self.dir = 'left'

        elif keys[pg.K_UP]:
            self.dir = 'up'
        elif keys[pg.K_DOWN]:
            self.dir = 'down'

    def move_head(self):
        if self.dir == 'right':
            self.pos[0][0] += self.size

        elif self.dir == 'left':
            self.pos[0][0] -= self.size

        elif self.dir == 'up':
            self.pos[0][1] -= self.size

        elif self.dir == 'down':
            self.pos[0][1] += self.size

    def move(self):
        self.move_tail()
        self.move_head()

    def draw(self, win):
        for pos in self.pos:
            pg.draw.rect(win, (255, 255, 255),
                         (pos[0], pos[1], self.size, self.size))

    def check_dead(self):
        if self.pos.count(self.pos[0]) > 1:
            return True

        return False


class Food:
    def __init__(self, x, y, size):
        self.pos = [x, y]
        self.size = size

    def draw(self, win):
        pg.draw.rect(win, (255, 0, 0),
                     (self.pos[0], self.pos[1], self.size, self.size))

    def check_eaten(self):
        if self.pos == snake.pos[0]:
            return True

        return False


#############
# VARIABLES #
#############

# Window
win_height = 500
win_width = 500
win = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('Snake')

# Snake
size = 10
x = random.randint(0, (win_width - size) / size) * size
y = random.randint(0, (win_height - size) / size) * size
snake = Snake(x, y, size)

# Food
x = random.randint(0, (win_width - size) / size) * size
y = random.randint(0, (win_height - size) / size) * size
food = Food(x, y, size)

#############
# MAIN LOOP #
#############

clock = pg.time.Clock()
run = True
while run:
    clock.tick(20)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    win.fill(0)
    snake.change_dir()
    snake.move()
    snake.draw(win)
    food.draw(win)
    if snake.check_dead():
        x = random.randint(0, (win_width - size) / size) * size
        y = random.randint(0, (win_height - size) / size) * size
        snake = Snake(x, y, size)

    if food.check_eaten():
        x = random.randint(0, win_width / size) * size
        y = random.randint(0, win_height / size) * size
        food = Food(x, y, size)

        snake.pos.append([x, y])

    pg.display.flip()
