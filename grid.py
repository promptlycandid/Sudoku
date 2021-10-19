import requests


class Grid:
    def get_puzzle_grid():
        response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
        grid = response.json()["board"]

        return grid

    def get_original_grid():
        grid = Grid.get_puzzle_grid()
        original_grid = [
            [grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))
        ]

        return original_grid
