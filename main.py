from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__is_running = False


if __name__ == '__main__':
    # win = Window(800, 600)
    # win.wait_for_close()
    window = Window(800, 600)
    window._Window__canvas.create_rectangle(50, 50, 150, 150, fill="blue")
    window.wait_for_close()
