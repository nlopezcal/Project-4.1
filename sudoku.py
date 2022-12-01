import time

import pygame
from constants import *
#from sudoku_generator import *
pygame.init()


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row - 1
        self.col = col - 1
        self.screen = screen

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value
        pass

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.value = value
        pass

    def draw(self):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
        self.x = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.col + SQUARE_SIZE // 2

        if self.value in range(10):
            return screen_text(f'{self.value}', (self.x, self.y), 65)




class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    # function that draws the sudoku
    def draw_grid(self):

        # draws top and bottom border
        pygame.draw.line(screen, BLACK, (1, 1), (600, 1), 4)
        pygame.draw.line(screen, BLACK, (0, 600), (600, 600), 4)

        # draws left and right border
        pygame.draw.line(screen, BLACK, (0, 0), (0, 600), 4)
        pygame.draw.line(screen, BLACK, (600, 0), (600, 600), 4)
        # creates horizontal grid lines
        for i in range(1, 9):
            pygame.draw.line(screen, GREY, (0, i * SQUARE_SIZE), (800, i * SQUARE_SIZE), 4)
            if i % 3 == 0:
                pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (800, i * SQUARE_SIZE), 4)

        # creates vertical lines
        for j in range(1, 9):
            pygame.draw.line(screen, GREY, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, 600), 4)
            if j % 3 == 0:
                pygame.draw.line(screen, BLACK, (j * SQUARE_SIZE, 0,), (j * SQUARE_SIZE, 600), 4)

        pygame.draw.line(screen, (0, 0, 0), (0, 600), (600, 600), )

    def select(self, row, col, color= RED):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        row -= 1
        col -= 1
        row = SQUARE_SIZE * row
        col = SQUARE_SIZE * col
        pygame.draw.rect(screen, color, pygame.Rect(row, col, 66, 66))
        Board(self.difficulty).draw_grid()
        return row and col


        pass

    def click(self, x, y):
        # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.
        self.x, self.y = x, y
        return self.x, self.y

    def clear(self, row, cell):
        # Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and  sketched  value  that  are
        # filled by themselves.
        Board(self.difficulty).select(row, cell, WHITE)
        pass

    def sketch(self, value, row, col):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        row -= 1
        col -= 1
        x = (SQUARE_SIZE * row) + 10
        y = (SQUARE_SIZE * col) + 15
        return screen_text(f'{value}', (x, y), 30, GREY)
        pass


    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        screen.fill(WHITE)
        Board(self.difficulty).draw_grid()
        #place random numbers
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        #fixme
        pass

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        #fixme
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        #fixme
        pass

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        #fixme
        pass




# function which creates a rectangle to act as a button
def create_button(text,pos, font_size):
    font = pygame.font.SysFont('Arial', font_size)
    x, y = pos # saves x and y with the position of wanted button
    buttontext = font.render(text, True, (0, 0, 0), (255, 69, 0))
    textrect = buttontext.get_rect() #Gets area of button
    textrect.center = (x, y)  # buttons center becomes x and y
    return screen.blit(buttontext, textrect)  # returns created button to screen

# creates text on screen
def screen_text(text, pos, font_size, color = BLACK):
    font = pygame.font.SysFont('Ariel', font_size)
    text = font.render(text, True, color)
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
        screen = pygame.display.set_mode((600,650))

        # sets caption of window to Sudoku
        pygame.display.set_caption('Sudoku')

        # sets background to background chosen
        screen.blit(background, (0,0))


        # updates display to screen
        pygame.display.flip()


        running = True  # variable that allows screen to continue playing
        easy_button = create_button('Easy',(200, 600), 40)
        medium_button = create_button('Medium',(300, 600), 40)
        hard_button = create_button('Hard',(400, 600), 40)
        screen_text('Welcome to Sudoku', (300, 100), 64)  # Creates Welcome Text
        screen_text('Select a difficulty', (300, 550),40)


        while running:  # while loop that allows screen to display
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # If user clicks the exit button, program ends
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: # If user clicks on screen, loop begins
                    if pygame.mouse.get_pressed()[0]:
                        if easy_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the easy button, easy board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset',(200, 620), 32)
                            restart_button = create_button('Restart',(300,620), 32)
                            exit_button = create_button('Exit',(400, 620), 32)
                            easy_board = Board('easy')
                            easy_board.draw_grid()
                            pygame.display.update()
                            game = 'easy'



                        elif medium_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the medium button, medium board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset', (200, 620), 32)
                            restart_button = create_button('Restart', (300, 620), 32)
                            exit_button = create_button('Exit', (400, 620), 32)
                            medium_board = Board('medium')
                            medium_board.draw_grid()
                            pygame.display.update()
                            game = 'medium'

                        if hard_button.collidepoint(pygame.mouse.get_pos()): # if user clicks the hard button, hard board will display
                            # displays board
                            screen.fill(WHITE)
                            reset_button = create_button('Reset', (200, 620), 32)
                            restart_button = create_button('Restart', (300, 620), 32)
                            exit_button = create_button('Exit', (400, 620), 32)
                            hard_board = Board('hard')
                            hard_board.draw_grid()

                            game = 'hard'

                            pygame.display.update()

                        time.sleep(0.01) # makes sures the buttons on second screen activated accidentally


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