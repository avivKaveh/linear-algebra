from vectors import add


def test_add():
    assert add([1, 2], [3, 4]) == [4, 6]


def test_add_negative():
    assert add([-1, 2], [5, -2]) == [4, 0]
