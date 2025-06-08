import sys
import time

from graphics import Window
from maze import Maze


def main():
    margin = 50
    # num_rows = 20
    # num_cols = 35
    # num_rows = 40
    # num_cols = 70
    # num_rows = 144
    # num_cols = 256
    # screen_x = 1920
    # screen_y = 1080
    num_rows = 20
    num_cols = 25
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)
    window = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    # print("maze created")
    maze.solve()
    # is_solvable = maze.solve()
    # if not is_solvable:
    #     print("maze can not be solved!")
    # else:
    #     print("maze solved!")

    window.wait_for_close()


if __name__ == '__main__':
    main()