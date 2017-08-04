import pygame
import random
import Blob
import Blobs_Manager
import thread

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



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

def main():
    pygame_init()
    blobs = []

    red_blob = Blob.Blob(RED,'Left')
    blue_blob = Blob.Blob(BLUE,'Right')
    green_blob = Blob.Blob(GREEN)
    red_blob2 = Blob.Blob(RED,'Right')
    blue_blob2 = Blob.Blob(BLUE,'Left')
    green_blob2 = Blob.Blob(GREEN)
    red_blob3 = Blob.Blob(RED,'Right')
    blue_blob3 = Blob.Blob(BLUE)
    green_blob3 = Blob.Blob(GREEN,'Left')
    blobs.append(red_blob)
    blobs.append(blue_blob)
    blobs.append(green_blob)
    blobs.append(red_blob2)
    blobs.append(blue_blob2)
    blobs.append(green_blob2)
    blobs.append(red_blob3)
    blobs.append(blue_blob3)
    blobs.append(green_blob3)
    global blobs_manager
    blobs_manager = Blobs_Manager.blobs_manager(blobs)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)

if __name__ == '__main__':
    main()