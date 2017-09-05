
import pygame
import random
import Blob
import Blobs_Manager
import thread
import msvcrt
from Queue import Queue
from threading import Thread
import time
import os
import sys
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


my_blob = Blob.Blob(RED, None,'User')

def pygame_init():
    global game_display
    global clock
    game_display = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Blob World')
    clock = pygame.time.Clock()


def draw_environment():
    global clock
    clock.tick(120)

    game_display.fill(WHITE)
    # for blob in blobs_manager.get_blobs():
    pygame.draw.circle(game_display, my_blob.colour, [my_blob.x, my_blob.y], my_blob.size)
        # blob_logic(blob)


    # blobs_manager.check_clash()
    pygame.display.update()

def create_blobs():
    blobs = []
    red_blob = Blob.Blob(RED, None,'User')
    # blue_blob = Blob.Blob(BLUE, 'Right')
    # green_blob = Blob.Blob(GREEN)
    # red_blob2 = Blob.Blob(RED, 'Right')
    # blue_blob2 = Blob.Blob(BLUE, 'Left')
    # green_blob2 = Blob.Blob(GREEN)
    # red_blob3 = Blob.Blob(RED, 'Right')
    # blue_blob3 = Blob.Blob(BLUE)
    # green_blob3 = Blob.Blob(GREEN, 'Left')
    blobs.append(red_blob)
    # blobs.append(blue_blob)
    # blobs.append(green_blob)
    # blobs.append(red_blob2)
    # blobs.append(blue_blob2)
    # blobs.append(green_blob2)
    # blobs.append(red_blob3)
    # blobs.append(blue_blob3)
    # blobs.append(green_blob3)
    global blobs_manager
    blobs_manager = Blobs_Manager.blobs_manager(blobs)

def update_user_blob(command):
    if command is not None:
        my_blob.move(command)

# def update_comp_blobs():

# def blob_updates(command):
#
#     if command is not None:

def run_game(in_q):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exits the loop. Not sure if 'exit()' was defined
                break
        # pygame.event.wait()
        if not in_q.empty():
            a = in_q.get()
            update_user_blob(a)

        draw_environment()




def kbfunc(out_q):
    while True:
        key_sensor = msvcrt.kbhit()
        key_hit = None
        if key_sensor:
            key_char = msvcrt.getch()
            if ord(key_char) == 224:
                key_char = msvcrt.getch()
                if ord(key_char) == 80:
                    key_hit = 'down'
                elif ord(key_char) == 77:
                    key_hit = 'right'
                elif ord(key_char) == 75:
                    key_hit = 'left'
                elif ord(key_char) == 72:
                    key_hit = 'up'

            elif ord(key_char) == 113:
                os._exit(1)

        if key_hit is not None:
            out_q.put(key_hit)

def main():
    pygame_init()
    # create_blobs()

    # Create the shared queue and launch both threads
    q = Queue()
    game_thread = Thread(target=run_game, args=(q,))
    keyboard_thread = Thread(target=kbfunc, args=(q,))
    game_thread.start()
    keyboard_thread.start()

if __name__ == '__main__':
    main()
