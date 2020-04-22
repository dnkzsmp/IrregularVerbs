from tkinter import *
from end.endwindow import EndWindow
import random


class Graphic:
    def __init__(self, s, verbs, root):
        self.wron = 0
        self.corr = 0
        self.gap = 1
        self.list = verbs
        self.verbs = random.choice(self.list).split()
        self.count = s
        self.corr = []
        self.wrong = []

        self.root = root
        self.root.geometry('400x360+630+240')
        self.root.resizable(False, False)
        self.word = Label(self.root)
        self.label1 = Label(self.root)
        self.inf = Entry(self.root, bd=4)
        self.label2 = Label(self.root)
        self.ps = Entry(self.root, bd=4)
        self.label3 = Label(self.root)
        self.pp = Entry(self.root, bd=4)
        self.check = Button(self.root,
                            text='Отправить',
                            command=self.checking)
        self.check.pack()
        self.check.config(state=NORMAL)
        self.next = Button(self.root,
                           text='Следующее',
                           command=self.change)
        self.next.config(state=DISABLED)
        self.next.pack()
        self.status = Label(self.root)
        self.status.pack()
        self.root.protocol("WM_DELETE_WINDOW",
                           self.exit_app)
        self.word.pack()
        self.label1.pack()
        self.inf.pack()
        self.label2.pack()
        self.ps.pack()
        self.label3.pack()
        self.pp.pack()
        self.initUI()

    def initUI(self):
        self.root.title('Тренажер форм глагола '
                        '"IrregularVerbs"')
        self.root.config(bg='#FFE1F9')
        self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n',
                         bg='#FFE1F9', fg='black', font=('Arial', 20, 'bold'))
        self.label1.config(text='Введите Infinitive',
                           bg='#FFE1F9')
        self.label2.config(text='Введите Past Simple',
                           bg='#FFE1F9')
        self.label3.config(text='Введите Past Participle',
                           bg='#FFE1F9')
        self.status.config(text='\n\n*вводить надо '
                                'в единственном числе'
                                '\n*использовать только '
                                'строчные английские буквы',
                           bg='#FFE1F9')

    def checking(self):
        inf = self.inf.get()
        ps = self.ps.get()
        pp = self.pp.get()
        count = 0
        if inf and ps and pp:
            sravn = [inf, ps, pp]
            if inf.isalpha() and ps.isalpha() and pp.isalpha() and \
                    not inf.isspace() and not ps.isspace() and not pp.isspace() and \
                    not inf.startswith(' ') and not ps.startswith(' ') and not pp.startswith(' ') and \
                    not inf.endswith(' ') and not ps.endswith(' ') and not pp.endswith(' '):
                for i in range(len(sravn)):
                    if sravn[i] != self.verbs[i + 1]:
                        count += 1
                if count == 0:
                    self.corr.append(self.verbs[0])
                else:
                    self.wrong.append(self.verbs[0])
                    self.status.config(fg='black', text='\n\nНажмите "Следующее"\n')
                self.next.config(state=NORMAL)
                self.check.config(state=DISABLED)
            else:
                self.status.config(fg='red', text='\n\nОшибка ввода\nВведите еще раз')
                self.inf.delete(0, 'end')
                self.ps.delete(0, 'end')
                self.pp.delete(0, 'end')
        else:
            self.status.config(fg='red', text='\n\nОшибка ввода\nВведите еще раз')
            self.inf.delete(0, 'end')
            self.ps.delete(0, 'end')
            self.pp.delete(0, 'end')

    def change(self):
        if self.gap < self.count:
            self.gap += 1
            self.verbs = random.choice(self.list).split()
            self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n')
            self.status.config(fg='black', text='\n\n*вводить надо в единственном числе'
                                                '\n*использовать только '
                                                'строчные английские буквы')
            self.next.config(state=DISABLED)
            self.check.config(state=NORMAL)
            self.inf.delete(0, 'end')
            self.ps.delete(0, 'end')
            self.pp.delete(0, 'end')
        else:
            self.root.destroy()
            win = Tk()
            EndWindow(win, self.wrong, self.corr)
            win.mainloop()

    def exit_app(self):
        self.root.destroy()
        sys.exit()
