from graphics import Window, Line, Point


def main():
    window = Window(800, 600)
    window.draw_line(Line(Point(100, 100), Point(200, 200)), "red")
    window.draw_line(Line(Point(200, 100), Point(100, 200)), "blue")
    window.draw_line(Line(Point(100, 100), Point(200, 100)), "black")
    window.draw_line(Line(Point(100, 200), Point(200, 200)), "black")
    window.draw_line(Line(Point(100, 100), Point(100, 200)), "black")
    window.draw_line(Line(Point(200, 100), Point(200, 200)), "black")
    window.wait_for_close()


if __name__ == '__main__':
    main()