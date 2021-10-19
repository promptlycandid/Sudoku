import numpy as np
from grid import Grid

grid = Grid.get_puzzle_grid()

# print(np.matrix(grid))


class Solver:
    def possible(x, y, n):
        for i in range(0, 9):
            if grid[y][i] == n:
                return False
        for i in range(0, 9):
            if grid[i][x] == n:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[y0 + i][x0 + j] == n:
                    return False
        return True

    def solve():
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if Solver.possible(y, x, n):
                            grid[y][x] = n
                            Solver.solve()
                            grid[y][x] = 0
                    # return

        # input("Try Again?")


if __name__ == "__main__":
    Solver.solve()
    print(np.matrix(grid))
