from StartMenu import *
from tkinter import *


def main():
    global app1
    global app2
    root = Tk()
    app1 = StartMenu(root)
    root.mainloop()
    window = Tk()
    app2 = Graphic(window)
    window.mainloop()


if __name__ == '__main__':
    main()
