#  initialising pygame
import pygame

pygame.init()
pygame.display.set_caption('BattleShip-AI')

#  loop to keep the game running
game_running = True
game_paused = False

#  global variables used throughout the code ; change them here
background_color = (6, 65, 75)
screen_width = 1366
screen_height = 768
square_length = screen_height/22
screen = pygame.display.set_mode((screen_width, screen_height))

grid_color = (255, 255, 255)


#  functions used throughout the code

#  drawing a grid
def draw_board(left, top):
    for i in range(100):
        x = (i % 10) * square_length
        y = (i // 10) * square_length
        square = pygame.Rect(x, y, square_length, square_length)
        pygame.draw.rect(screen, grid_color, square, width=2)


#  constantly checking for user inputs
while game_running == True:
    for event in pygame.event.get():

        #  Closing the window
        if event.type == pygame.K_ESCAPE:
            game_running = False

        #  Pausing, Resuming the game
        if event.type == pygame.K_SPACE:
            game_paused = not game_paused

    # if running
    if game_paused == False:
        #  create game boards
        screen.fill(background_color)
        draw_board(left = 0, top = 0)
        pygame.display.flip()
