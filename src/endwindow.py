# -*- coding: utf-8 -*-
from tkinter import Tk, PhotoImage
from tkinter import Label, Button, Listbox
from tkinter import DISABLED, LEFT, RIGHT, END
import os
import sys


class EndWindow(Tk):
    def __init__(self, wrong, append, verbs):
        super().__init__()
        self.wrong = wrong
        self.correct = append
        self.verbs = verbs
        self.label1 = Label(self)
        self.label2 = Label(self)
        self.look = Button(self)
        self.rest = Button(self)
        self.exit = Button(self)
        self.finish = Label(self)
        self.label1.pack()
        self.label2.pack()
        self.look.pack()
        self.rest.pack()
        self.exit.pack()
        self.finish.pack()
        self.initUI()

    def initUI(self):
        self.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0],
                                                          '../style/icon.png')))
        self.title('Тренажер IrregularVerbs')
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))
        self.config(bg='#3A3A3A')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW",
                      self.exit_app)
        self.label1.config(bg='#3A3A3A')
        self.finish.config(bg='#3A3A3A')
        self.label1.config(text='Спасибо, что приняли участие в тренажере\n'
                                'IrregularVerbs. Надеемся, что ваши знания\n'
                                'по английскому стали лучше.\n',
                           fg='#DADADA', font=('Arial', 13, 'italic'),
                           bg='#3A3A3A')
        self.label2.config(text='"Результаты" - посмотреть результаты '
                                'тренажера\n'
                                '"Заново" - начать заново\n'
                                '"Выйти" - выйти из приложения\n',
                           fg='#FFD000')
        self.label2.config(bg='#3A3A3A')
        self.look.config(text='Результаты', command=self.results)
        self.exit.config(text='Выйти', command=self.exit_app)
        self.rest.config(text='Заново', command=self.restart)
        self.finish.config(text='', bg='#3A3A3A', fg='#DADADA')

    def results(self):
        if self.wrong:
            lb_wrong = Listbox()
            lb_wrong.insert(END, '    [НЕПРАВИЛЬНО]:')
            lb_wrong.insert(END, '')
            for i in self.wrong:
                lb_wrong.insert(END, i)
                lb_wrong.config(fg='#FF79E8', bg='#4D4D4D')
            if self.correct:
                lb_wrong.pack(pady=15, side=LEFT)
            else:
                lb_wrong.pack(pady=15)
        if self.correct:
            lb_correct = Listbox()
            lb_correct.insert(END, '      [ПРАВИЛЬНО]:')
            lb_correct.insert(END, '')
            for j in self.correct:
                lb_correct.insert(END, j)
                lb_correct.config(fg='#11FF00', bg='#4D4D4D')
            if self.wrong:
                lb_correct.pack(pady=15, side=RIGHT)
            else:
                lb_correct.pack(pady=15)
        else:
            self.finish.config(text='Нету правильных', fg='#FF79E8')
        self.look.config(state=DISABLED)

    def restart(self):
        sys.path.append('..')
        from src.startwindow import StartWindow
        self.destroy()
        app = StartWindow(self.verbs)
        app.mainloop()

    def exit_app(self):
        self.destroy()
        sys.exit()
