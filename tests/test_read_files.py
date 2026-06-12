from unittest.mock import Mock, mock_open, patch

import pytest

from src.read_files import read_csv_file, read_excel_file


@pytest.fixture
def logger_mock():
    return Mock()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_cvs_file_not_found(mock_open):
    """Тест обработки ошибки отсутствия файла."""
    result = read_csv_file("nonexistent.cvs")
    # вернула пустой список
    assert result == []
    # попытка открыть файл была
    assert mock_open.called


patch("builtins.open", mock_open(read_data="некорректный cvs {]"))


def test_cvs_decode_error():
    """Тест обработки некорректного cvs."""
    result = read_csv_file("test_invalid.cvs")
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_exls_file_not_found(mock_open):
    """Тест обработки ошибки отсутствия файла."""
    result = read_excel_file("nonexistent.exls")
    # вернула пустой список
    assert result == []
    # попытка открыть файл была
    assert mock_open.called


patch("builtins.open", mock_open(read_data="некорректный exls {]"))


def test_exls_decode_error():
    """Тест обработки некорректного cvs."""
    result = read_excel_file("test_invalid.exls")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_handles_pandas_errors(mock_read_excel):
    # Arrange
    mock_read_excel.side_effect = Exception("Симуляция ошибки")
    fake_path = "/fake/path/to/file.xlsx"
    result = read_excel_file(fake_path)
    assert result == []
    mock_read_excel.assert_called_once_with(fake_path)


@patch("pandas.read_excel")
def test_read_excel_errors(mock_read_excel):
    # Arrange
    mock_read_excel.side_effect = Exception("Симуляция ошибки")
    fake_path = "/fake/path/to/file.xlsx"
    result = read_excel_file(fake_path)
    assert result == []
    mock_read_excel.assert_called_once_with(fake_path)


def test_read_excel_true():
    mock_read_excel = Mock(
        return_value=[
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    result = mock_read_excel()
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


patch("read_files.logger")  # ЗАМЕНИТЕ 'your_module' на имя вашего файла


@patch("src.read_files.logger")
@patch("src.read_files.pd.read_excel")
def test_read_excel_file_success(mock_read_excel, mock_logger):
    import pandas as pd

    # Arrange: Настраиваем мок для read_excel
    # Создаем фейковый DataFrame, который вернет read_excel
    fake_df = pd.DataFrame([{"id": 101, "name": "Ivan", "amount": 500}, {"id": 102, "name": "Maria", "amount": 700}])
    mock_read_excel.return_value = fake_df
    result = read_excel_file("test.xlsx")
    # Assert: Проверяем результат функции
    expected_result = [{"id": 101, "name": "Ivan", "amount": 500}, {"id": 102, "name": "Maria", "amount": 700}]
    assert result == expected_result
    # Assert: Проверяем, что read_excel был вызван с правильным путем
    mock_read_excel.assert_called_once_with("test.xlsx")
    # Assert: Проверяем логирование успешного завершения (строка из красного блока)
    mock_logger.info.assert_called_with("read_excel_file завершение функции")
