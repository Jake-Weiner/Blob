import random
WIDTH = 800
HEIGHT = 600

class Blob:
    def __init__(self, colour,orientation=None,type = 'Computer'):
        self.colour = colour

        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.user = False
        if type == 'Computer':
            self.size = random.randrange(4, 14)
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
        else:
            self.size = 8
            self.user = True


    def move(self, input_dir = None):

        if self.user == False:
            if input_dir is None:
                self.x += self.move_x
                self.y += self.move_y
        else:
            if input_dir == 'left':
                self.x += -3
            elif input_dir == 'right':
                self.x += 3
            elif input_dir == 'up':
                self.y += -3
            elif input_dir == 'down':
                self.y += 3

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

