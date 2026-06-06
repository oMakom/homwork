import os
from dotenv import load_dotenv
from unittest.mock import Mock, patch

from src.external_api import exchange_rate


@patch('requests.get')
def test_exchange_rate_rub_currency_returns_1(mock_get):
    """Тест для валюты RUB — должен вернуть 1.0 без вызова API."""
    result = exchange_rate("RUB")
    assert result == 1.0
    mock_get.assert_not_called()


@patch('requests.get')
def test_exchange_rate_successful_usd_rate(mock_get):
    """Тест успешного получения курса для USD."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": {"USDRUB": "70.5"}
    }
    mock_get.return_value = mock_response
    result = exchange_rate("USD")
    assert result == "70.5"
    load_dotenv()
    Api_Key = os.getenv("API_KEY")
    mock_get.assert_called_once_with(f"https://currate.ru/api/?get=rates&pairs=USDRUB&key={Api_Key}")


@patch('requests.get')
def test_exchange_rate_not_found_in_api(mock_get):
    """Тест для валюты, отсутствующей в ответе API."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "Valute": {
            "UD": {"Value": 70.5}
        }
    }
    mock_get.return_value = mock_response
    result = exchange_rate("USD")
    assert result == 1
    load_dotenv()
    Api_Key = os.getenv("API_KEY")
    mock_get.assert_called_once_with(f"https://currate.ru/api/?get=rates&pairs=USDRUB&key={Api_Key}")
