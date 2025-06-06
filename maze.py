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
            window: Window
        ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.__cells = []
        self.__create_cells()

    def __create_cells(self) -> None:
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                col_cells.append(Cell(self.window))
            self.__cells.append(col_cells)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, column: int, row: int) -> None:
        start_x = self.x1 + (self.cell_size_x * column)
        start_y = self.y1 + (self.cell_size_y * row)
        start_point = Point(start_x, start_y)
        end_x = self.x1 + (self.cell_size_x * (column + 1))
        end_y = self.y1 + (self.cell_size_y * (row + 1))
        end_point = Point(end_x, end_y)
        self.__cells[column][row].draw(start_point, end_point)
        self.__animate()

    def __animate(self) -> None:
        if self.window is None:
            return
        self.window.redraw()
        sleep(0.05)
