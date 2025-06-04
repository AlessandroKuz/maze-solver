from graphics import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)

    # Forward move
    from_cell = Cell(window)
    to_cell = Cell(window)
    from_cell.draw(Point(400, 400), Point(500, 500))
    to_cell.draw(Point(500, 400), Point(600, 500))
    from_cell.draw_move(to_cell)

    # Undo move
    from_cell = Cell(window)
    to_cell = Cell(window)
    from_cell.draw(Point(200, 200), Point(300, 300))
    to_cell.draw(Point(300, 200), Point(400, 300))
    from_cell.draw_move(to_cell, undo=True)

    window.wait_for_close()


if __name__ == '__main__':
    main()