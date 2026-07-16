from vectors import add, scalar_multiply, dot

# add tests.
def test_add():
    assert add([1, 2], [3, 4]) == [1+3, 2+4]

def test_add_negative():
    assert add([-1, 2], [5, -2]) == [-1+5, 2-2]

# multiply tests.
def test_scalar_multiply():
    assert scalar_multiply(3, [1, 2]) == [3*1, 3*2]

def test_scalar_multiply_negative():
    assert scalar_multiply(-2, [1, -3]) == [-2*1, -2*-3]

# dot tests.
def test_dot():
    assert dot([1, 2], [3, 4]) == 11


def test_dot_zero():
    assert dot([1, 2], [0, 0]) == 0


def test_dot_negative():
    assert dot([-1, 2], [5, -2]) == -9