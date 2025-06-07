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
            window: Window = None
        ) -> None:
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
        sleep(0.01)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
