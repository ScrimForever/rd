from multiprocess import main_process


def test_main_square_true():
    result = main_process([5, 2, 3])
    assert result == [25, 4, 9]

def test_main_square_false():
    result = main_process([5, 2, 3])
    assert result != [1, 3, 4]
