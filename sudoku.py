import pygame
from constants import *
pygame.init()


class Button:
    def __init__(self, text, height, width, pos, font_size):
        self.x, self.y = pos
        self.font = pygame.font.SysFont('Arial', font_size)
        self.width = width
        self.height = height
        self.text = self.font.render(text, 1, pygame.Color('White'))

    def show_button(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill('orange')
        self.surface.blit(self.text, (0,0))
        screen.blit(self.surface, (self.x, self.y))


def draw_grid():
    # creates horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 60), (WIDTH, i * 60), LINE_WIDTH)

    # creates vertical lines
    for j in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (0, j * 60), (WIDTH, j * 60), LINE_WIDTH)



def main():

    # sets background image to sudoku background
    background = pygame.image.load('sudoku-background.jpg')

    #Creates screen with size 800x600
    global screen
    screen = pygame.display.set_mode((800,600))

    # sets caption of window to Sudoku
    pygame.display.set_caption('Sudoku')

    # sets background to background chosen
    screen.blit(background, (0,0))

    # updates display to screen
    pygame.display.flip()


    running = True  # variable that allows screen to continue playing

    while running:  # while loop that allows screen to display
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
        button1.show_button()
        button2.show_button()
        button3.show_button()
        pygame.display.update()



button1 = Button('   Easy', 40, 100, (200, 500), 30)
button2 = Button(' Medium', 40, 100, (350, 500), 30)
button3 = Button('   Hard', 40, 100, (500, 500), 30)

if __name__ == '__main__':
    main()