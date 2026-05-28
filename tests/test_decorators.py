from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def test_func(x, y):
        return x / y + x

    test_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "test_func ok\n"
    test_func(3, 0)
    captured = capsys.readouterr()
    assert captured.out == "test_func error: division by zero. Inputs: args=(3, 0), kwargs={}\n"
    test_func("3", 0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "test_func error: unsupported operand type(s) for /: 'str' and 'int'. Inputs: args=('3', 0), kwargs={}\n"
    )
