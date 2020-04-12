import random


def verbs():
    with open('verbs.txt', encoding='utf-8') as f:
        strokes = f.readlines()
    lines = [line.strip() for line in strokes]
    words = random.choice(lines).split()
    f.close()
    return words[0], words[1], words[2], words[3]


def correct_all(wrong, correct):
    if wrong <= 30 or correct <= 30:
        return wrong + 0, correct + 3


def correct_one(wrong, correct):
    if wrong <= 30 or correct <= 30:
        return wrong + 2, correct + 1


def correct_two(wrong, correct):
    if wrong <= 30 or correct <= 30:
        return wrong + 1, correct + 2


def wrong_all(wrong, correct):
    if wrong <= 30 or correct <= 30:
        return wrong + 3, correct + 0


def counter(ch):
    count = int(ch)
    if 1 <= count <= 10:
        return count
    else:
        return 1


def check_sum(wrong, correct, count):
    if count == (wrong + correct) / 3 and wrong % 3 == 0 and correct % 3 == 0:
        return 0
    else:
        return 1
