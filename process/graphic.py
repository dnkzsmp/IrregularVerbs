from tkinter import Tk, PhotoImage
from tkinter import Label, Entry, Button
from tkinter import NORMAL, DISABLED
import os
import sys
import random

sys.path.append('..')

from end.endwindow import EndWindow


class Graphic(Tk):
    def __init__(self, s, verbs):
        super().__init__()
        self.repeat = []
        self.wron = 0
        self.corr = 0
        self.gap = 1
        self.list = verbs
        self.verbs = random.choice(self.list).split()
        self.count = s
        self.corr = []
        self.wrong = []

        self.word = Label(self)
        self.label1 = Label(self)
        self.inf = Entry(self, bd=4)
        self.label2 = Label(self)
        self.ps = Entry(self, bd=4)
        self.label3 = Label(self)
        self.pp = Entry(self, bd=4)
        self.check = Button(self,
                            text='Отправить',
                            command=self.checking)
        self.check.pack()
        self.check.config(state=NORMAL)
        self.next = Button(self,
                           text='Следующее',
                           command=self.change)
        self.next.config(state=DISABLED)
        self.next.pack()
        self.status = Label(self)
        self.status.pack()
        self.protocol("WM_DELETE_WINDOW",
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
        self.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0],
                                                          '../style/icon.png')))
        self.config(bg='#3A3A3A')
        self.geometry('400x360')
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))
        self.resizable(False, False)
        self.title('Тренажер форм глагола '
                   '"IrregularVerbs"')
        self.inf.config(bg='#DADADA')
        self.ps.config(bg='#DADADA')
        self.pp.config(bg='#DADADA')
        self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n',
                         bg='#3A3A3A', fg='#DADADA',
                         font=('Arial', 20, 'bold'))
        self.label1.config(text='Введите Infinitive',
                           bg='#3A3A3A', fg='#DADADA')
        self.label2.config(text='Введите Past Simple',
                           bg='#3A3A3A', fg='#DADADA')
        self.label3.config(text='Введите Past Participle',
                           bg='#3A3A3A', fg='#DADADA')
        self.status.config(text='\n\n*вводить надо '
                                'в единственном числе'
                                '\n*использовать только '
                                'строчные английские буквы',
                           bg='#3A3A3A', fg='#FFD000')

    def checking(self):
        w1 = self.inf.get()
        w2 = self.ps.get()
        w3 = self.pp.get()
        inf = check_word(w1)
        ps = check_word(w2)
        pp = check_word(w3)
        sravn = [inf, ps, pp]
        if all(i.isalpha() for i in sravn):
            count = check_lists(sravn, self.verbs)
            if count is True:
                self.corr.append(self.verbs[0])
            else:
                self.wrong.append(self.verbs[0])
            self.status.config(fg='#11FF00',
                               text='\n\nНажмите "Следующее"\n')
            self.next.config(state=NORMAL)
            self.check.config(state=DISABLED)
            self.inf.config(state=DISABLED)
            self.ps.config(state=DISABLED)
            self.pp.config(state=DISABLED)
        else:
            self.status.config(fg='#FF79E8', text='\n\nОшибка ввода\n'
                                                  'Введите еще раз')
            self.inf.delete(0, 'end')
            self.ps.delete(0, 'end')
            self.pp.delete(0, 'end')

    def change(self):
        self.repeat.append(self.verbs[0])
        if self.gap < self.count:
            self.gap += 1
            self.verbs = random.choice(self.list).split()
            for i in range(len(self.repeat)):
                if i == self.verbs[0]:
                    self.verbs = random.choice(self.list).split()
                    break
            self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n')
            self.status.config(fg='#FFD000', text='\n\n*вводить надо в '
                                                  'единственном числе'
                                                  '\n*использовать только '
                                                  'строчные английские буквы')
            self.next.config(state=DISABLED)
            self.check.config(state=NORMAL)
            self.inf.config(state=NORMAL)
            self.ps.config(state=NORMAL)
            self.pp.config(state=NORMAL)
            self.inf.delete(0, 'end')
            self.ps.delete(0, 'end')
            self.pp.delete(0, 'end')
        else:
            self.destroy()
            win = EndWindow(self.wrong, self.corr)
            win.mainloop()

    def exit_app(self):
        self.destroy()
        sys.exit()


def check_lists(words, verbs):
    sravn = []
    for i in range(len(words)):
        if words[i] == verbs[i + 1]:
            sravn.append(True)
        else:
            sravn.append(False)
    counter = sravn.count(True)
    if counter == 3:
        return True
    return False


def check_word(word):
    if word:
        if not word.startswith(' ') and \
                not word.endswith(' ') and word.islower():
            return word
        return '-1'
    return '-1'
