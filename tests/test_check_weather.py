import sys
import os
import unittest
from unittest.mock import patch, Mock

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import check_weather


class TestCheckWeather(unittest.TestCase):

    @patch('functions.check_weather.speak')
    @patch('functions.check_weather.requests.get')
    @patch('functions.check_weather.os.getenv', return_value='test_api_key')
    def test_get_weather(self, mock_getenv, mock_get, mock_speak):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 300.15, 'humidity': 50},
            'weather': [{}]
        }
        mock_get.return_value = mock_response
        
        check_weather.get_weather('test_city')
        
        mock_speak.assert_called_once_with("Температура сьогодні 27.0°C, а вологість 50%")


if __name__ == '__main__':
    unittest.main()
