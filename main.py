from StartMenu import *
from tkinter import *


def main():
    root = Tk()
    StartMenu(root)
    root.mainloop()
    window = Tk()
    Graphic(window)
    window.mainloop()
    result = Tk()
    Result(result)
    result.mainloop()


if __name__ == '__main__':
    main()
