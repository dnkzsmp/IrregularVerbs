import verbs


def test_correct_all():
    assert verbs.correct_all(0, 3) == 0, 6


def test_correct_two():
    assert verbs.correct_two(0, 0) == 1, 2


def test_correct_one():
    assert verbs.correct_one(0, 0) == 2, 1


def test_wrong_all():
    assert verbs.wrong_all(0, 0) == 3, 0


def test_counter():
    assert verbs.counter('5') == 5


def test_check_sum():
    assert verbs.check_sum(12, 18, 10) == 0
