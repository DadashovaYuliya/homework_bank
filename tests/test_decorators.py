from src.decorators import log


@log(filename="")
def my_function(x: int, y: int) -> int:
    """Функция, суммирующая два числа"""
    return x + y


def test_my_fuction(capsys):
    """Положительный тест функции с правильным вводом"""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_my_fuction_error(capsys):
    """Тест функции при неправильном вводе"""
    my_function(1, "2")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Input: (1, '2'), {}\n\n"
    )
