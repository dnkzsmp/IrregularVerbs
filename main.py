from StartMenu import *
from tkinter import *



def main():
    global app1
    global count
    count = 0
    root = Tk()
    app1 = StartMenu(root)
    root.mainloop()


if __name__ == '__main__':
    rus = ''
    inf = ''
    pasts = ''
    pastp = ''
    main()
