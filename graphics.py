from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # New root widget as a private member
        self.__root = Tk()                   
        self.__root.title("Maze Gazer")
        # New canvas using root widget and class size as parameters.
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Method to redraw all graphics in the window.
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # Redraw graphics as long as state of window is running otherwise wait for the close call.
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    # Set running state to False, close the window and stop program.
    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fil_color="black"):
        canvas.create_line(self.p1.)










    
