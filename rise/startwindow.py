from tkinter import *
from process.graphic import Graphic


class StartWindow(Tk):
    def __init__(self, lines):
        super().__init__()
        self.s = 0
        self.verbs = lines
        self.geometry('600x230+560+340')
        self.resizable(False, False)
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
        self.title('Тренажер форм глагола "IrregularVerbs"')
        self.config(bg='#FFE1F9')
        self.hello1.config(text='Добро пожаловать в тренажер', bg='#FFE1F9', font=('Arial', 13, 'bold'))
        self.hello2.config(text='форм неправильного глагола "IrregularVerbs"\n', bg='#FFE1F9',
                           font=('Arial', 13, 'bold'))
        self.hello3.config(text='Введите кол-во глаголов для тренировки(от 1 до 10)', bg='#FFE1F9', font=5)
        self.start.config(font=2)
        self.PS.config(text='', fg='#FFE1F9', bg='#FFE1F9')

    def start_check(self):
        if self.verbs_entry.get().isdigit() and not self.verbs_entry.get().isspace():
            self.s = int(self.verbs_entry.get())
            if self.s > 10:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*максимальное число: 10',
                               font=3, fg='red')
            if self.s == 0:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*минимальное число: 1',
                               fg='red')
            elif 1 <= self.s <= 10:
                self.destroy()
                root = Graphic(self.s, self.verbs)
                root.mainloop()
        elif not self.verbs_entry.get().isdigit() or self.verbs_entry.get().isspace():
            self.verbs_entry.delete(0, 'end')
            self.PS.config(text='\n*надо вести число '
                                'число от 1 до 10', fg='red')
        self.start.invoke()

    def exit_app(self):
        self.destroy()
        self.Exit.invoke()
        sys.exit()
