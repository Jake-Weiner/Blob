
import pygame
import random
import Blob
import Blobs_Manager
import thread
import msvcrt

from multiprocessing import Process, Queue

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def curse(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)

def pygame_init():
    global game_display
    global clock
    game_display = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Blob World')
    clock = pygame.time.Clock()

def draw_environment(blobs):
    game_display.fill(WHITE)
    for blob in blobs_manager.get_blobs():

        pygame.draw.circle(game_display, blob.colour, [blob.x, blob.y], blob.size)
        # blob_logic(blob)
        blob.move()

    blobs_manager.check_clash()
    pygame.display.update()

def create_blobs():
    blobs = []
    red_blob = Blob.Blob(RED, 'Left')
    blue_blob = Blob.Blob(BLUE, 'Right')
    green_blob = Blob.Blob(GREEN)
    red_blob2 = Blob.Blob(RED, 'Right')
    blue_blob2 = Blob.Blob(BLUE, 'Left')
    green_blob2 = Blob.Blob(GREEN)
    red_blob3 = Blob.Blob(RED, 'Right')
    blue_blob3 = Blob.Blob(BLUE)
    green_blob3 = Blob.Blob(GREEN, 'Left')
    blobs.append(red_blob)
    blobs.append(blue_blob)
    # blobs.append(green_blob)
    # blobs.append(red_blob2)
    # blobs.append(blue_blob2)
    # blobs.append(green_blob2)
    # blobs.append(red_blob3)
    # blobs.append(blue_blob3)
    # blobs.append(green_blob3)
    global blobs_manager
    blobs_manager = Blobs_Manager.blobs_manager(blobs)

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs_manager.get_blobs())
        clock.tick(60)

def kbfunc():
    while True:
        key_hit = msvcrt.kbhit()
        if key_hit == True:
            key_char = msvcrt.getch()
            if ord(key_char) == 224:
                key_char = msvcrt.getch()
                if ord(key_char) == 80:
                    print 'down'
                elif ord(key_char) == 77:
                    print 'right'
                elif ord(key_char) == 75:
                    print 'left'
                elif ord(key_char) == 72:
                    print 'up'
            # print ord(k)
            # if (ord(k)) == '224\n80':
            #     print 'found it'

            # if ord(k) == int(0x26):
            #     print "up"
            # elif k == 40:
            #     print "down"
            # elif k == 39:
            #     print 'right'
            # elif k == 37:
            #     print "left"




def main():
    # pygame_init()
    # create_blobs()
    # q = Queue()
    # run_game = Process(target=draw_environment, args=(q,))
    # run_game.start()
    # print(q.get())  # prints "[42, None, 'hello']"
    # p.join()
    # thread.start_new(run_game,())
    # thread.start_new(kbfunc,())
    kbfunc()


    # while 1:
    #     pass


if __name__ == '__main__':
    main()
