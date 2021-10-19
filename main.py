import sys
import pygame
import requests
from sys import exit
from grid import Grid

pygame.init()

WIDTH = 550
HEIGHT = 550
BACKGROUND_COLOR = (255, 255, 255)
FONT = pygame.font.SysFont("Comic Sans MS", 35)
ORIG_GRID_ELEM_CLR = (52, 31, 151)
BUFFER = 5
BLACK = (0, 0, 0)

grid = Grid.get_puzzle_grid()
original_grid = Grid.get_original_grid()


class Sudoku:
    def draw_window(win):
        pygame.display.set_caption("Sudoku")
        win.fill(BACKGROUND_COLOR)

    def add_grid(win):
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(win, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                pygame.draw.line(win, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

            pygame.draw.line(win, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(win, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    # def get_puzzle_grid():
    #     response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    #     grid = response.json()["board"]

    #     return grid

    # def get_original_grid():
    #     grid = Sudoku.get_puzzle_grid()
    #     original_grid = [
    #         [grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))
    #     ]

    #     return original_grid

    def get_game_numbers(win):
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if 0 < grid[i][j] < 10:
                    value = FONT.render(str(grid[i][j]), True, ORIG_GRID_ELEM_CLR)
                    win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

    def enter_number(win, pos):
        i, j = pos[1], pos[0]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if original_grid[i - 1][i - 1] != 0:
                        return
                    if event.key == pygame.K_0:  # checking to see if 0 and delete box
                        grid[i - 1][j - 1] = event.key
                        pygame.draw.rect(
                            win,
                            BACKGROUND_COLOR,
                            (
                                pos[0] * 50 + BUFFER,
                                pos[1] * 50 + BUFFER,
                                50 - 2 * BUFFER,
                                50,
                            ),
                        )
                        pygame.display.update()
                    if 0 < event.key - 48 < 10:  # checking for valid input
                        pygame.draw.rect(
                            win,
                            BACKGROUND_COLOR,
                            (
                                pos[0] * 50 + BUFFER,
                                pos[1] * 50 + BUFFER,
                                50 - 2 * BUFFER,
                                50,
                            ),
                        )
                        value = FONT.render(str(event.key - 48), True, BLACK)
                        win.blit(value, (pos[0] * 50 + 15, pos[1] * 50))
                        grid[i - 1][j - 1] = event.key - 48
                        pygame.display.update()
                    return

    def game_loop():
        win = pygame.display.set_mode((WIDTH, HEIGHT))

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    Sudoku.enter_number(win, (pos[0] // 50, pos[1] // 50))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys.exit()

            Sudoku.draw_window(win)
            Sudoku.add_grid(win)
            Sudoku.get_game_numbers(win)
            pygame.display.update()


if __name__ == "__main__":
    Sudoku.game_loop()
