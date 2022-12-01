import time

import pygame
from constants import *
pygame.init()




# function which creates a rectangle to act as a button
def create_button(text,pos, font_size):
    font = pygame.font.SysFont('Arial', font_size)
    x, y = pos # saves x and y with the position of wanted button
    buttontext = font.render(text, True, (0, 0, 0), (255, 69, 0))
    textrect = buttontext.get_rect() #Gets area of button
    textrect.center = (x, y)  # buttons center becomes x and y
    return screen.blit(buttontext, textrect)  # returns created button to screen


# function that draws the sudoku
def draw_grid(difficulty):

    # draws top and bottom border
    pygame.draw.line(screen, BLACK, (1,1), (800, 1), 4)
    pygame.draw.line(screen, BLACK, (0, 560), (800, 560), 4)

    # draws left and right border
    pygame.draw.line(screen, BLACK, (0,0), (0, 560), 4)
    pygame.draw.line(screen, BLACK, (798, 0), (798, 560), 4)
    # creates horizontal grid lines
    for i in range(1, 9):
        pygame.draw.line(screen, GREY, (0, i * (screeny-30)//9), (800, i * (screeny-30)//9), 4)
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, i * (screeny - 30) // 9), (800, i * (screeny - 30) // 9), 4)


    # creates vertical lines
    for j in range(1, 9):
        pygame.draw.line(screen, GREY, (j * (screenx // 9), 0), (j * (screenx // 9), 560), 4)
        if j % 3 == 0:
            pygame.draw.line(screen, BLACK, (j * (screenx // 9), 0), (j * (screenx // 9), 560), 4)


    pygame.draw.line(screen, (0,0,0), (0,560), (800,560),)
#creates text on screen
def screen_text(text, pos, font_size):
    font = pygame.font.SysFont('Ariel', font_size)
    text = font.render(text, True, (0, 0, 0))
    textrect = text.get_rect()
    textrect.center = (pos)
    return screen.blit(text, textrect) # returns created text on to screen


def main():
    while True:
        # sets background image to sudoku background
        background = pygame.image.load('sudoku-background.jpg')

        #Creates screen with size 800x600
        global screen, screenx, screeny
        screenx = 800
        screeny = 600
        screen = pygame.display.set_mode((screenx,screeny))

        # sets caption of window to Sudoku
        pygame.display.set_caption('Sudoku')

        # sets background to background chosen
        screen.blit(background, (0,0))


        # updates display to screen
        pygame.display.flip()


        running = True  # variable that allows screen to continue playing
        easy_button = create_button('Easy',(250, 500), 40)
        medium_button = create_button('Medium',(400, 500), 40)
        hard_button = create_button('Hard',(550, 500), 40)
        screen_text('Welcome to Sudoku', (400, 100), 64)  # Creates Welcome Text
        screen_text('Select a difficulty', (400, 450),40)

        while running:  # while loop that allows screen to display
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # If user clicks the exit button, program ends
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: # If user clicks on screen, loop begins
                    if pygame.mouse.get_pressed()[0]:
                        if easy_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the easy button, easy board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset',(300, 580), 32)
                            restart_button = create_button('Restart',(400,580), 32)
                            exit_button = create_button('Exit',(500, 580), 32)
                            draw_grid('easy')
                            pygame.display.update()

                        elif medium_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the medium button, medium board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset', (300, 580), 32)
                            restart_button = create_button('Restart', (400, 580), 32)
                            exit_button = create_button('Exit', (500, 580), 32)
                            draw_grid('medium')
                            pygame.display.update()

                        if hard_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the hard button, hard board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset', (300, 580), 32)
                            restart_button = create_button('Restart', (400, 580), 32)
                            exit_button = create_button('Exit', (500, 580), 32)
                            draw_grid('hard')
                            pygame.display.update()

                        if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks again on second screen
                            if exit_button.collidepoint(pygame.mouse.get_pos()): #if user clicks exit button, game is close
                                pygame.quit()
                            if reset_button.collidepoint(pygame.mouse.get_pos()): #if user clicks reset button, game board will reset
                               pass
                                #fixme
                                # find a way to reset board

                            if restart_button.collidepoint(pygame.mouse.get_pos()): #if player clicks restart button, they're returned to main screen
                                main()


            pygame.display.flip()



if __name__ == '__main__':
    main()