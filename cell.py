from graphics import Window, Line, Point


class Cell:
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, start_point: Point, end_point: Point, fill_color: str = "black") -> None:
        if self.__win is None:
            return

        self.__x1 = start_point.x
        self.__x2 = end_point.x
        self.__y1 = start_point.y
        self.__y2 = end_point.y

        if self.has_left_wall:
            point1 = Point(self.__x1, self.__y1)
            point2 = Point(self.__x1, self.__y2)
            self.__win.draw_line(Line(point1, point2), fill_color=fill_color)

        if self.has_right_wall:
            point1 = Point(self.__x2, self.__y1)
            point2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(point1, point2), fill_color=fill_color)

        if self.has_top_wall:
            point1 = Point(self.__x1, self.__y1)
            point2 = Point(self.__x2, self.__y1)
            self.__win.draw_line(Line(point1, point2), fill_color=fill_color)

        if self.has_bottom_wall:
            point1 = Point(self.__x1, self.__y2)
            point2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(point1, point2), fill_color=fill_color)

    def center_point(self):
        x_center = abs(self.__x1 + self.__x2) // 2
        y_center = abs(self.__y1 + self.__y2) // 2
        return Point(x_center, y_center)

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        fill_color = "red" if not undo else "grey"

        current_cell_center_point = self.center_point()
        to_cell_center_point = to_cell.center_point()

        line = Line(current_cell_center_point, to_cell_center_point)
        self.__win.draw_line(line, fill_color)
