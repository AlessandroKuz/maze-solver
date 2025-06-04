from graphics import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)
    cell = Cell(window)
    point1 = Point(100, 100)
    point2 = Point(200, 200)
    cell.draw(point1, point2, fill_color="coral")


    c = Cell(window)
    c.has_left_wall = False
    c.draw(Point(50, 50), Point(100, 100))

    c = Cell(window)
    c.has_right_wall = False
    c.draw(Point(125, 125), Point(200, 200))

    c = Cell(window)
    c.has_bottom_wall = False
    c.draw(Point(225, 225), Point(250, 250))

    c = Cell(window)
    c.has_top_wall = False
    c.draw(Point(300, 300), Point(500, 500))


    window.wait_for_close()


if __name__ == '__main__':
    main()