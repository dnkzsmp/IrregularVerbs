from tkinter import *


class EndWindow(Tk):
    def __init__(self, wrong, append):
        super().__init__()
        self.wrong = wrong
        self.correct = append
        self.label = Label(self)
        self.look = Button(self)
        self.exit = Button(self)
        self.finish = Label(self)
        self.label.pack()
        self.look.pack()
        self.exit.pack()
        self.finish.pack()
        self.initUI()

    def initUI(self):
        self.title('Тренажер IrregularVerbs')
        self.config(bg='#FFE1F9')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW",
                      self.exit_app)
        self.label.config(text='Спасибо, что приняли участие в тренажере\n'
                               'IrregularVerbs. Надеемся, что ваши знания\n'
                               'по английскому стали лучше\n'
                               '"Результаты" - посмотреть результаты тренажера\n'
                               '"Выйти" - выйти из приложения', fg='black',
                          font=('Arial', 13, 'bold'), bg='#FFE1F9')
        self.look.config(text='Результаты', command=self.results)
        self.exit.config(text='Выйти', command=self.exit_app)
        self.finish.config(text='', bg='#FFE1F9')

    def results(self):
        if self.wrong:
            lb_wrong = Listbox()
            for i in self.wrong:
                lb_wrong.insert(END, i)
                lb_wrong.config(fg='red')
            if self.correct:
                lb_wrong.pack(pady=15, side=LEFT)
            else:
                lb_wrong.pack(pady=15)
        if self.correct:
            lb_correct = Listbox()
            for j in self.correct:
                lb_correct.insert(END, j)
                lb_correct.config(fg='green')
            if self.wrong:
                lb_correct.pack(pady=15, side=RIGHT)
            else:
                lb_correct.pack(pady=15)
        else:
            self.finish.config(text='Нету правильных', fg='red')
        self.look.config(state=DISABLED)

    def exit_app(self):
        self.destroy()
        sys.exit()
