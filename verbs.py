import random


def verbs():
    global rus
    global inf
    global pasts
    global pastp
    with open('verbs.txt', encoding='utf-8') as f:
        strokes = f.readlines()
    lines = [line.strip() for line in strokes]
    words = random.choice(lines).split()
    rus = words[0]
    inf = words[1]
    pasts = words[2]
    pastp = words[3]
