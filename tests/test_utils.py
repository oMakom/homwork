from unittest.mock import mock_open, patch

from src.utils import transaction_amount, transaction_json_in_python


@patch("builtins.open", side_effect=FileNotFoundError)
def test_transaction_json_in_python_file_not_found(mock_open):
    """Тест обработки ошибки отсутствия файла."""
    result = transaction_json_in_python("nonexistent.json")
    # вернула пустой список
    assert result == []
    # попытка открыть файл была
    assert mock_open.called


@patch("builtins.open", mock_open(read_data="некорректный json {]"))
def test_json_decode_error():
    """Тест обработки некорректного JSON."""
    result = transaction_json_in_python("test_invalid.json")
    assert result == []


@patch("src.external_api.exchange_rate")
def test_transaction_amount(mock_rate):
    """Тест обработки корректности с параметром валюы 50"""
    mock_rate.return_value = 50
    assert (
        transaction_amount(
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            }
        )
        == 2844177
    )
    mock_rate.assert_called_once_with("USD")
