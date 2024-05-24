import asyncio
import unittest

import pytest
from unittest.mock import AsyncMock
from binance import AsyncClient
from unittest.mock import AsyncMock, patch

from services import get_top_list
from services.binance_api import get_info_currency, get_account_info


# @pytest.mark.asyncio
# async def test_get_info_currency_success():
#     symbol = 'BTC'
#     mock_client = AsyncMock(spec=AsyncClient)
#     mock_client.get_ticker.return_value = {'lastPrice': '30000.0'}
#     symbol_info, last_price = await get_info_currency(symbol)
#     assert last_price >= '30000.0'
#
#
# @pytest.mark.asyncio
# async def test_get_account_info():
#     # Создаем mock для функции get_client
#     mock_client = AsyncMock()
#     mock_client.get_account = AsyncMock(return_value=asyncio.Future())
#     mock_client.get_account.return_value.set_result({'account_id': '12345', 'balance': 1000})
#
#     with patch('services.binance_api.get_client', return_value=mock_client):
#         # Вызываем тестируемую функцию
#         account_info = await get_account_info()
#
#         # Проверяем, что результат соответствует ожидаемому
#         assert account_info == {'account_id': '12345', 'balance': 1000}
#         # Проверяем, что get_account был вызван один раз
#         mock_client.get_account.assert_awaited_once()


class TestMainFunction(unittest.TestCase):
    @patch('requests.get')
    def test_main(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'symbol': 'BTCUSDT', 'quoteVolume': '100', 'askPrice': '50000', 'priceChangePercent': '5'},
            {'symbol': 'ETHUSDT', 'quoteVolume': '50', 'askPrice': '2000', 'priceChangePercent': '3'},
            # Add more mock data as needed
        ]

        expected_output = (
            "1. BTCUSDT - Price: 50000 USDT, Change in 24h: 5%\n"
            "2. ETHUSDT - Price: 2000 USDT, Change in 24h: 3%\n"
            # Add more expected output as needed
        )

        self.assertEqual(get_top_list.main().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
