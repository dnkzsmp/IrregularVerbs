import sys


def open_file(path):
    try:
        file = open(path, encoding='utf-8')
        file.close()
        return True
    except IOError:
        return False


def main():
    path = '../verbs.txt'
    check = open_file(path)
    if check is True:
        with open('../verbs.txt', encoding='utf-8') as fin:
            strokes = fin.readlines()
        lines = [line.strip() for line in strokes]
        fin.close()
        app = StartWindow(lines)
        app.mainloop()
    else:
        print('Файл не открыт. Завершена работа программы.')


if __name__ == '__main__':
    sys.path.append('..')
    from rise.startwindow import StartWindow
    main()
