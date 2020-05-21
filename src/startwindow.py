# -*- coding: utf-8 -*-
import sys
import os
from tkinter import Label, Entry, Button
from tkinter import Tk, PhotoImage


class StartWindow(Tk):
    def __init__(self, lines):
        super().__init__()
        self.s = 0
        self.verbs = lines
        self.hello1 = Label(self)
        self.hello2 = Label(self)
        self.hello3 = Label(self)
        self.verbs_entry = Entry(self, bd=4)
        self.start = Button(self, text='Начать',
                            command=self.start_check)
        self.Exit = Button(self, text='Выйти',
                           command=self.exit_app)
        self.Exit.config(font=2)
        self.PS = Label(self)
        self.hello1.pack()
        self.hello2.pack()
        self.hello3.pack()
        self.verbs_entry.pack()
        self.start.pack()
        self.Exit.pack()
        self.PS.pack()
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.initUI()

    def initUI(self):
        self.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0],
                                                          '../style/icon.png')))
        self.geometry('600x230')
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))
        self.resizable(False, False)
        self.title('Тренажер форм глагола "IrregularVerbs"')
        self.config(bg='#3A3A3A')
        self.verbs_entry.config(bg='#DADADA')
        self.start.config(bg='#DADADA')
        self.Exit.config(bg='#DADADA')
        self.hello1.config(text='Добро пожаловать в тренажер', bg='#3A3A3A',
                           font=('Arial', 13, 'bold'), fg='#DADADA')
        self.hello2.config(text='форм неправильного глагола '
                                '"IrregularVerbs"\n', bg='#3A3A3A',
                           font=('Arial', 13, 'bold'), fg='#DADADA')
        self.hello3.config(text='Введите кол-во глаголов для тренировки'
                                '(от 1 до 10)', bg='#3A3A3A', font=5,
                           fg='#11FF00')
        self.start.config(font=2)
        self.PS.config(text='', fg='#00FF38', bg='#3A3A3A')

    def start_check(self):
        if self.verbs_entry.get().isdigit() and \
                not self.verbs_entry.get().isspace():
            self.s = int(self.verbs_entry.get())
            if self.s > 10:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*максимальное число: 10',
                               font=3, fg='#FF79E8')
            if self.s == 0:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*минимальное число: 1',
                               fg='#FF79E8', font=3)
            elif 1 <= self.s <= 10:
                sys.path.append('..')
                from src.graphic import Graphic
                self.destroy()
                root = Graphic(self.s, self.verbs)
                root.mainloop()
        elif not self.verbs_entry.get().isdigit() or \
                self.verbs_entry.get().isspace():
            self.verbs_entry.delete(0, 'end')
            self.PS.config(text='\n*надо вести число '
                                'число от 1 до 10', fg='#FF79E8', font=2)

    def exit_app(self):
        self.destroy()
        sys.exit()
