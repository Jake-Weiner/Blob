import random
WIDTH = 800
HEIGHT = 600

class Blob:
    def __init__(self, colour,orientation=None):
        self.colour = colour
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,14)
        if orientation is None:
            self.move_x = random.randrange(-2,2)
            self.move_y = random.randrange(-2,2)
        elif orientation == 'Right':
            self.move_x = random.randrange(-2, 4)
            self.move_y = random.randrange(-2, 4)
        elif orientation == 'Left':
            self.move_x = random.randrange(-4, 2)
            self.move_y = random.randrange(-4, 2)
        else:
            print 'incorrect direction'
            quit()

    def move(self):

        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

    def blob_grow(self,size):
        self.size += size

