import random

from cell import Cell
from graphics import Window, Line, Point
from time import sleep


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window = None,
        seed: int = None,
    ) -> None:
        if seed is not None:
            random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited_status()

    def __create_cells(self) -> None:
        for col in range(self.__num_cols):
            col_cells = []
            for row in range(self.__num_rows):
                col_cells.append(Cell(self.__window))
            self.__cells.append(col_cells)

        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, column: int, row: int) -> None:
        start_x = self.__x1 + (self.__cell_size_x * column)
        start_y = self.__y1 + (self.__cell_size_y * row)
        start_point = Point(start_x, start_y)
        end_x = self.__x1 + (self.__cell_size_x * (column + 1))
        end_y = self.__y1 + (self.__cell_size_y * (row + 1))
        end_point = Point(end_x, end_y)
        self.__cells[column][row].draw(start_point, end_point)
        self.__animate()

    def __animate(self) -> None:
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(1 / (self.__num_cols * self.__num_rows))
        # sleep(0.00000005)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, column: int, row: int) -> None:
        self.__cells[column][row].visited = True
        while True:
            cells_to_visit = []

            adjacent_cells = [(column-1, row), (column, row-1), (column+1, row), (column, row+1)]
            adjacent_cells = list(filter(lambda coord: coord[0] >= 0 and coord[1] >= 0, adjacent_cells))
            adjacent_cells = list(filter(lambda coord: coord[0] < self.__num_cols and coord[1] < self.__num_rows, adjacent_cells))
            adjacent_cells = list(filter(lambda coord: not self.__cells[coord[0]][coord[1]].visited, adjacent_cells))
            for adjacent_cell in adjacent_cells:
                cells_to_visit.append(adjacent_cell)

            if len(cells_to_visit) == 0:
                self.__draw_cell(column, row)
                return

            new_cell_coords = random.choice(cells_to_visit)
            if new_cell_coords[0] == column + 1:
                self.__cells[column][row].has_right_wall = False
                self.__draw_cell(column, row)
                self.__cells[new_cell_coords[0]][new_cell_coords[1]].has_left_wall = False
                self.__draw_cell(new_cell_coords[0], new_cell_coords[1])
            elif new_cell_coords[1] == row + 1:
                self.__cells[column][row].has_bottom_wall = False
                self.__draw_cell(column, row)
                self.__cells[new_cell_coords[0]][new_cell_coords[1]].has_top_wall = False
                self.__draw_cell(new_cell_coords[0], new_cell_coords[1])
            elif new_cell_coords[0] == column - 1:
                self.__cells[column][row].has_left_wall = False
                self.__draw_cell(column, row)
                self.__cells[new_cell_coords[0]][new_cell_coords[1]].has_right_wall = False
                self.__draw_cell(new_cell_coords[0], new_cell_coords[1])
            else:
                self.__cells[column][row].has_top_wall = False
                self.__draw_cell(column, row)
                self.__cells[new_cell_coords[0]][new_cell_coords[1]].has_bottom_wall = False
                self.__draw_cell(new_cell_coords[0], new_cell_coords[1])

            self.__break_walls_r(new_cell_coords[0], new_cell_coords[1])

    def __reset_cells_visited_status(self) -> None:
        for col in self.__cells:
            for cell in col:
                cell.visited = False
