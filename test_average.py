def test_add_three():
    from average import add_three
    s = add_three(4, 5, 6)
    assert s == 15


def test_divide_three():
    from average import divide_three
    a = divide_three(15, 3)
    assert a == 5
