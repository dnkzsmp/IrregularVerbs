import random


def verbs():
    with open('verbs.txt', encoding='utf-8') as f:
        strokes = f.readlines()
    lines = [line.strip() for line in strokes]
    words = random.choice(lines).split()
    rus = words[0]
    inf = words[1]
    pasts = words[2]
    pastp = words[3]
    return rus, inf, pasts, pastp


def correct_all(wrong, correct):
    wrong += 0
    correct += 3
    return wrong, correct


def correct_one(wrong, correct):
    wrong += 2
    correct += 1
    print(wrong)
    return wrong, correct


def correct_two(wrong, correct):
    wrong += 1
    correct += 2
    return wrong, correct


def wrong_all(wrong, correct):
    wrong += 3
    correct += 0
    return wrong, correct


def counter(ch):
    count = int(ch)
    return count