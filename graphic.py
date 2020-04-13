from tkinter import *
from verbs import *


rus = ''
inf = ''
pasts = ''
pastp = ''
count = ''
wron = 0
corr = 0
gap = 1


def restart_app():
    global count
    global wron
    global corr
    global gap
    win1 = Tk()
    count = ''
    wron = 0
    corr = 0
    gap = 1
    StartMenu(win1)
    win1.mainloop()
    win2 = Tk()
    Graphic(win2)
    win2.mainloop()
    win3 = Tk()
    Result(win3)
    win3.mainloop()


class StartMenu:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry('600x230+560+340')
        self.parent.title('Тренажер форм глагола "IrregularVerbs"')
        self.parent.config(bg='#FFE1F9')
        self.parent.resizable(False, False)
        self.hello1 = Label(self.parent, text='Добро пожаловать в тренажер', bg='#FFE1F9')
        self.hello1.config(font=('Arial', 13, 'bold'))
        self.hello2 = Label(self.parent, text='форм неправильного глагола "IrregularVerbs"\n', bg='#FFE1F9')
        self.hello2.config(font=('Arial', 13, 'bold'))
        self.hello3 = Label(self.parent, text='Введите кол-во глаголов для тренировки(от 1 до 10)', bg='#FFE1F9')
        self.hello3.config(font=5)
        self.verbs_entry = Entry(self.parent, bd=4)
        self.start = Button(self.parent, text='Начать', command=self.start_check)
        self.start.config(font=2)
        self.Exit = Button(self.parent, text='Выйти', command=self.exit_app)
        self.Exit.config(font=2)
        self.PS = Label(self.parent, text='', fg='#FFE1F9', bg='#FFE1F9')
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
        global rus
        global pasts
        global inf
        global pastp
        ch = self.verbs_entry.get()
        if ch.isdigit():
            s = int(ch)
            if s > 10:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*максимальное число: 10', font=3, fg='red')
            if s == 0:
                self.verbs_entry.delete(0, 'end')
                self.PS.config(text='\n*минимальное число: 1', fg='red')
            elif 1 <= s <= 10:
                count = counter(ch)
                self.verbs_entry.delete(0, 'end')
                self.parent.destroy()
        else:
            self.verbs_entry.delete(0, 'end')
            self.PS.config(text='\n*надо вести число число от 1 до 10', fg='red')

    def exit_app(self):
        self.parent.destroy()
        sys.exit()


class Graphic:
    def __init__(self, parent1):
        global rus
        global inf
        global pasts
        global pastp
        rus, inf, pasts, pastp = verbs(rus, inf, pasts, pastp)
        self.parent1 = parent1
        self.parent1.geometry('550x360+630+240')
        self.parent1.title('Тренажер форм глагола "IrregularVerbs"')
        self.parent1.config(bg='#FFE1F9')
        self.parent1.resizable(False, False)
        self.word = Label(self.parent1, text='Ваше слово: ' + rus + '\n', bg='#FFE1F9', fg='black')
        self.word.config(font=('Arial', 20, 'bold'))
        self.inf1 = Label(self.parent1, text='Введите Infinitive', bg='#FFE1F9')
        self.infi = Entry(self.parent1, bd=4)
        self.ps1 = Label(self.parent1, text='Введите Past Simple', bg='#FFE1F9')
        self.ps2 = Entry(self.parent1, bd=4)
        self.pp1 = Label(self.parent1, text='Введите Past Participle', bg='#FFE1F9')
        self.pp2 = Entry(self.parent1, bd=4)
        self.word.pack()
        self.inf1.pack()
        self.infi.pack()
        self.ps1.pack()
        self.ps2.pack()
        self.pp1.pack()
        self.pp2.pack()
        self.check = Button(self.parent1, text='Проверить', command=self.checking)
        self.check.pack()
        self.next = Button(self.parent1, text='Следующее', command=self.rechange)
        self.next.config(state=DISABLED)
        self.next.pack()
        self.status = Label(self.parent1, text='\n\n*вводить надо в единственном числе'
                                               '\n*использовать только строчные английские буквы', bg='#FFE1F9')
        self.status.pack()
        self.parent1.protocol("WM_DELETE_WINDOW", self.exit_app)

    def checking(self):
        global wron
        global corr
        global rus
        global inf
        global pasts
        global pastp
        i = self.infi.get()
        ps = self.ps2.get()
        pp = self.pp2.get()
        if inf == i and pasts == ps and pastp == pp:
            self.status.config(text='\n\nВы правильно ввели все 3 формы!', fg='green')
            wron, corr = correct_all(wron, corr)
        if inf != i and pasts == ps and pastp == pp:
            self.status.config(text='\n\nВы ввели неправильно Infinitive(правильное слово: ' + inf + ')', fg='red')
            wron, corr = correct_two(wron, corr)
        elif pasts != ps and inf == i and pastp == pp:
            self.status.config(text='\n\nВы ввели неправильно Past Simple(правильное слово: ' + pasts + ')', fg='red')
            wron, corr = correct_two(wron, corr)
        elif pastp != pp and inf == i and pasts == ps:
            self.status.config(text='\n\nВы ввели неправильно Past Participle(правильное слово: ' + pastp + ')',
                               fg='red')
            wron, corr = correct_two(wron, corr)
        if inf != i and pasts != ps and pastp == pp:
            self.status.config(text='\n\nВы ввели неправильно Infinitive(правильное слово: ' + inf + ')\n' +
                                    'Вы ввели неправильно Past Simple(правильное слово: ' + pasts + ')', fg='red')
            wron, corr = correct_one(wron, corr)
        elif inf != i and pastp != pp and pasts == ps:
            self.status.config(text='\n\nВы ввели неправильно Infinitive(правильное слово: ' + inf + ')\n' +
                                    'Вы ввели неправильно Past Participle(правильное слово: ' + pastp + ')', fg='red')
            wron, corr = correct_one(wron, corr)
        elif pasts != ps and pastp != pp and inf == i:
            self.status.config(text='\n\nВы ввели неправильно Past Simple(правильное слово: ' + pasts + ')\n' +
                                    'Вы ввели неправильно Past Participle(правильное слово: ' + pastp + ')', fg='red')
            wron, corr = correct_one(wron, corr)
        if inf != i and pasts != ps and pastp != pp:
            self.status.config(text='\n\nВы неправильно ввели все 3 формы\n'
                                    '(правильные слова: ' + inf + ', ' + pasts + ', ' + pastp + ')', fg='red')
            wron, corr = wrong_all(wron, corr)
        self.check.config(state=DISABLED)
        self.next.config(state=NORMAL)

    def rechange(self):
        global gap
        global count
        global rus
        global inf
        global pasts
        global pastp
        if gap < int(count):
            gap += 1
            rus, inf, pasts, pastp = verbs(rus, inf, pasts, pastp)
            self.word.config(text='Ваше слово: ' + rus + '\n')
            self.status.config(fg='black', text='\n\n*вводить надо в единственном числе'
                                                '\n*использовать только строчные английские буквы')
            self.next.config(state=DISABLED)
            self.check.config(state=NORMAL)
            self.infi.delete(0, 'end')
            self.ps2.delete(0, 'end')
            self.pp2.delete(0, 'end')
        else:
            check_sum(wron, corr, count)
            self.parent1.destroy()

    def exit_app(self):
        self.parent1.destroy()
        sys.exit()


class Result:
    def __init__(self, parent2):
        global wron
        global corr
        self.parent2 = parent2
        self.parent2.geometry('550x220+610+300')
        self.parent2.title('Тренажер форм глагола "IrregularVerbs"')
        self.parent2.config(bg='#FFE1F9')
        self.parent2.resizable(False, False)
        self.result = Label(self.parent2, text='Ваши результаты:\n', bg='#FFE1F9', fg='black')
        self.result.config(font=('Arial', 20, 'bold'))
        self.correct = Label(self.parent2, text='Правильно: ' + str(corr) + '\n', fg='#006015', bg='#FFE1F9')
        self.correct.config(font='bold')
        self.wrong = Label(self.parent2, text='Неправильно: ' + str(wron) + '\n', fg='red', bg='#FFE1F9')
        self.wrong.config(font='bold')
        self.restart = Button(self.parent2, text='Начать заново', command=self.restart)
        self.exit = Button(self.parent2, text='Выйти', command=self.exit_app)
        self.result.pack()
        self.correct.pack()
        self.wrong.pack()
        self.restart.pack()
        self.exit.pack()

    def exit_app(self):
        self.parent2.destroy()
        sys.exit()

    def restart(self):
        self.parent2.destroy()
        restart_app()
