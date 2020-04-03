from tkinter import *
from verbs import verbs


class StartMenu:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry('600x230+560+340')
        self.parent.title('Тренажер форм глагола "IrregularVerbs"')
        self.parent.config(bg='pink')
        self.parent.resizable(False, False)
        self.hello1 = Label(self.parent, text='Добро пожаловать в тренажер', bg='pink')
        self.hello1.config(font=('Arial', 13, 'bold'))
        self.hello2 = Label(self.parent, text='форм неправильного глагола "IrregularVerbs"\n', bg='pink')
        self.hello2.config(font=('Arial', 13, 'bold'))
        self.hello3 = Label(self.parent, text='Введите кол-во глаголов для тренировки(от 1 до 10)', bg='pink')
        self.hello3.config(font=5)
        self.verbs_entry = Entry(self.parent, bd=4)
        self.start = Button(self.parent, text='Начать', command=self.start_check)
        self.start.config(font=2)
        self.Exit = Button(self.parent, text='Выйти', command=self.exit_app)
        self.Exit.config(font=2)
        self.PS = Label(self.parent, text='', fg='pink', bg='pink')
        self.hello1.pack()
        self.hello2.pack()
        self.hello3.pack()
        self.verbs_entry.pack()
        self.start.pack()
        self.Exit.pack()
        self.PS.pack()
        self.parent.protocol("WM_DELETE_WINDOW", self.exit_app)

    def start_check(self):
        global count
        ch = self.verbs_entry.get()
        count = self.verbs_entry.get()
        if ch.isdigit():
            s = int(ch)
            if s > 10:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*максимальное число: 10', font=3, fg='red')
            if s == 0:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*минимальное число: 1', fg='red')
            elif 1 <= s <= 10:
                self.verbs_entry.delete(0, 'end')
                self.parent.destroy()
                verbs()
        else:
            self.verbs_entry.delete(0, 'end')
            self.PS.config(text='\n*надо вести число число от 1 до 10', fg='red')

    def exit_app(self):
        self.parent.destroy()
        sys.exit()